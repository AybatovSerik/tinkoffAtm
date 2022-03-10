import telebot
import time
from myToken import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


@bot.message_handler(commands=["gogo"])
def gogo(message):
    for i in range(10):
        bot.send_message(message.chat.id, 'Ждём ' + str(i))
        time.sleep(2)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)