import telebot, asyncio, config, parse, user

bot: telebot.TeleBot

class NoAccess(Exception):
    pass

def init():
    global bot
    bot = telebot.TeleBot(config.cfg["apikey"])

    if "logchat" in config.cfg.keys():
        bot.send_message(config.cfg["logchat"], "Pyrobot starting up...")

    @bot.message_handler(commands=['fetch'])
    def fetch(message):
        result = parse.parse()
        if type(result) == int:
            err("HTTP "+str(result), message.chat.id)
        else:
            try:
                bot.send_message(message.chat.id, result)
            except:
                err("Слишком длинное сообщение?", message.chat.id)
                print(result)

    # @bot.message_handler(commands=['newedu'])
    # def newedu(message):
    #     try:
    #         refuseIfNotOwner(message)

    #         user.newEduCookie()
    #         if config.cfg["edu_cookie"] == "NOCOOKIE":
    #             err("NOCOOKIE")
    #         else:
    #             log(config.cfg["edu_cookie"])
    #     except:
    #         pass

    @bot.message_handler(commands=['auth'])
    def auth(message):
        try:
            refuseIfNotOwner(message)

            user.authorize()
        except:
            pass

    asyncio.run(bot.polling())

def log(message):
    if "logchat" in config.cfg.keys():
        try:
            bot.send_message(config.cfg["logchat"], "ℹ "+str(message))
        except:
            err("Не удалось отправить лог", config.cfg["logchat"])
            print(str(message))
    else:
        print("Logchat not specified!!! Message: "+str(message))

def err(message, chat = None):
    if chat == None and "logchat" in config.cfg.keys():
        chat = config.cfg["logchat"]
    try:
        bot.send_message(chat, "❌ Ошибка: "+str(message))
    except:
        bot.send_message(chat, "❌ Ошибка при отправке!!")

def checkOwner(user: telebot.types.User):
    if not ("ownerId" in config.cfg.keys()):
        return True
    if str(user.id) == config.cfg["ownerId"]:
        return True
    return False

def refuseIfNotOwner(message: telebot.types.Message):
    if not checkOwner(message.from_user):
        err("Нет доступа", message.chat.id)
        raise NoAccess