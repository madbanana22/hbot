import requests, config, bot

def authorize(username: str = "", password: str = ""):
    headers = {
        'authority': 'pwa.kiasuo.ru',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'sec-fetch-dest': 'document',
        'accept': 'application/json, text/plain, */*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    }

    login_form = f'{commit: "Войти", diary_user: {username: "{config.cfg["user"]}", password: "{config.cfg["pass"]}"}, subdomain: "dnevnik"}'

    link = "https://dnevnik.kiasuo.ru/diary/pwa_login"
    session = requests.session()

    request = session.post(link, json=login_form, headers=headers)

    if request.status_code == 200:
        parsed = request.json()

        if "_edu_session" in request.cookies.keys():
            config.cfg["edu_session"] = request.cookies.get("edu_session")
            bot.log(config.cfg["edu_session"])
        else:
            config.cfg["edu_session"] = "NOSESSION"
            bot.err("Отсутствует печенька _edu_session.")

        if "accessToken" in parsed():
            config.cfg["bearer"] = "Bearer "+parsed()["accessToken"]
            bot.log(parsed["accessToken"])
        else:
            config.cfg["bearer"] = "NOBEARER"
            bot.err("Запрос не содержит accessToken.")
        
        if "refreshToken" in parsed():
            config.cfg["bearer"] = parsed["refreshToken"]
            bot.log(parsed["refreshToken"])
        else:
            config.cfg["refresh"] = "NOREFRESH"
            bot.err("Запрос не содержит refreshToken.")
    else:
        config.cfg["bearer"] = "NOBEARER"
        config.cfg["edu_session"] = "NOSESSION"
        config.cfg["refresh"] = "NOREFRESH"
        bot.err("HTTP "+str(request.status_code)+". \nОтвет: "+request.text)




# def newEduCookie():
#     headers = {
#         'authority': 'dnevnik.kiasuo.ru',
#         'cache-control': 'max-age=0',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
#         'sec-fetch-dest': 'document',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-user': '?1',
#         'accept-language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#     }

#     link = "https://dnevnik.kiasuo.ru/diary/refresh"
#     # если запросить новую печеньку, при этом не предоставив токен сброса,
#     # сайт выдаст новый токен авторизации. его и будем использовать.
#     session = requests.session()

#     request = session.post(link, headers=headers)
    
#     #bot.log(request.text)
#     #bot.log(request.status_code)

#     if "_edu_session" in request.cookies.keys():
#         config.cfg["edu_cookie"] = request.cookies.get("_edu_session")
#     else:
#         config.cfg["edu_cookie"] = "NOCOOKIE"
