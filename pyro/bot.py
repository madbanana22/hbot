import telebot, config, parse

bot: telebot.TeleBot

def init():
    global bot
    bot = telebot.TeleBot(config.cfg["apikey"])

    @bot.message_handler(commands=['fetch'])
    def fetch(message):
        result = parse.parse()
        if type(result) == int:
            bot.send_message(message.chat.id, "Error " + str(result))
        else:
            try:
                bot.send_message(message.chat.id, result)
            except:
                bot.send_message(message.chat.id, "Error sending message, see terminal")
                print(result)

    print("Initialized successfully")

    bot.infinity_polling()