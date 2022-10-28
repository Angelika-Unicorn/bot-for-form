"""
Бот для формы.
Дублирует любое сообщение, которое ему отправлено.
"""

import telebot
token = '5519272567:AAHRuITo2hMg_3owJ26UoBWwgEITWKwxOIg'


bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет. Ну что? Поболтаем?')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True, interval=0)
