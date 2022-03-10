import telebot
import time
from myToken import token
from requestToTinkoffApi import makeRequest
from atm import parseATM
from conf import interestedIds

bot = telebot.TeleBot(token)
notification_dict = {}


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


@bot.message_handler(commands=["now"])
def now(m):
    makeRequest()
    atms = parseATM("requestResponse.txt")
    for atm in atms:
        if atm.id in interestedIds:
            bot.send_message(m.chat.id, str(atm))

@bot.message_handler(commands=["stop"])
def stop(m):
    notification_dict[m.chat.id] = False

@bot.message_handler(commands=["noteme"])
def noteMe(m):
    old_dict = {}
    notification_dict[m.chat.id] = True
    everyTime = 5
    currentTime = 0
    while notification_dict[m.chat.id]:
        makeRequest()
        atms = parseATM("requestResponse.txt")
        new_dict = {}
        for atm in atms:
            if atm.id in interestedIds:
                new_dict[atm.id] = atm
                if atm.usd > 1000:
                    bot.send_message(m.chat.id, "!!!!!!~USD~!!!!!!!")
                    bot.send_message(m.chat.id, str(atm))
                elif (len(old_dict) == 0)|(currentTime==-1):
                    bot.send_message(m.chat.id, str(atm))
                elif old_dict[atm.id] != new_dict[atm.id]:
                    bot.send_message(m.chat.id, "UPDATE")
                    bot.send_message(m.chat.id, str(atm))
                else:
                    pass

        for key in new_dict.keys():
            old_dict[key] = new_dict[key]
        currentTime += 1
        if currentTime == everyTime:
            currentTime = 0
        time.sleep(120)



# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)