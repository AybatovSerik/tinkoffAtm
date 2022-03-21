import telebot
import time
from myToken import token
from requestToTinkoffApi import makeRequest, makeRequestWork
from atm import parseATM
from conf import interestedIds, workIds

bot = telebot.TeleBot(token)
notification_dict = {}

request_freq = 60
everyTime = 60

@bot.message_handler(commands=["now"])
def now(m):
    try:
        makeRequest()
    except:
        bot.send_message(m.chat.id, "Request Problem!")
    atms = parseATM("requestResponse.txt")
    for atm in atms:
        if atm.id in interestedIds:
            bot.send_message(m.chat.id, str(atm))


@bot.message_handler(commands=["nowwork"])
def nowWork(m):
    try:
        makeRequestWork()
    except:
        bot.send_message(m.chat.id, "Request Problem!")
    atms = parseATM("requestResponseWork.txt")
    for atm in atms:
        if atm.id in workIds:
            bot.send_message(m.chat.id, str(atm))

@bot.message_handler(commands=["stop"])
def stop(m):
    notification_dict[m.chat.id] = False

@bot.message_handler(commands=["noteme"])
def noteMe(m):
    old_dict = {}
    notification_dict[m.chat.id] = True
    currentTime = 0
    while notification_dict[m.chat.id]:
        try:
            makeRequest()
        except:
            bot.send_message(m.chat.id, "Request Problem!")
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
                elif old_dict[atm.id].usd != new_dict[atm.id].usd:
                    bot.send_message(m.chat.id, "UPDATE")
                    bot.send_message(m.chat.id, str(atm))
                else:
                    pass

        for key in new_dict.keys():
            old_dict[key] = new_dict[key]
        currentTime += 1
        if currentTime == everyTime:
            currentTime = 0
            bot.send_message(m.chat.id, "Notification is working!")
        time.sleep(request_freq)

@bot.message_handler(commands=["notemework"])
def noteMeWork(m):
    old_dict = {}
    notification_dict[m.chat.id] = True
    currentTime = 0
    while notification_dict[m.chat.id]:
        try:
            makeRequestWork()
        except:
            bot.send_message(m.chat.id, "Request Problem!")
        atms = parseATM("requestResponseWork.txt")
        new_dict = {}
        for atm in atms:
            if atm.id in workIds:
                new_dict[atm.id] = atm
                if atm.usd > 1000:
                    bot.send_message(m.chat.id, "!!!!!!~USD~!!!!!!!")
                    bot.send_message(m.chat.id, str(atm))
                elif (len(old_dict) == 0)|(currentTime==-1):
                    bot.send_message(m.chat.id, str(atm))
                elif old_dict[atm.id].usd != new_dict[atm.id].usd:
                    bot.send_message(m.chat.id, "UPDATE")
                    bot.send_message(m.chat.id, str(atm))
                else:
                    pass

        for key in new_dict.keys():
            old_dict[key] = new_dict[key]
        currentTime += 1
        if currentTime == everyTime:
            currentTime = 0
            bot.send_message(m.chat.id, "Notification is working!")
        time.sleep(request_freq)        


# Запускаем бота
bot.polling(none_stop=True, interval=0)
