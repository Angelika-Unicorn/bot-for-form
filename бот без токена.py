"""
Бот для формы.
Дублирует любое сообщение, которое ему отправлено.
"""


import telebot
token = "(token here)"


bot = telebot.TeleBot(token)

# upd = bot.get_updates()
# print(upd)
# last_upd = upd[-1]
# massage_from_user = last_upd.massage
# print(massage_from_user)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет. Ну что? Поболтаем?')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True, interval=0)

