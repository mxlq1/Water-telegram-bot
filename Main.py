import telebot
from writer import water_write

with open('bot_key.txt') as file:
    bot = telebot.TeleBot(file.readline())

water_data = []
water_list = ["Ванна", "Горячая", "Холодная", "Кухня", "Горячая", "Холодная", "Туалет", "Горячая", "Холодная"]
counter = 0


@bot.message_handler(commands=['start'])
def start(message):
    global counter
    bot.send_message(message.chat.id, water_list[counter])
    counter += 1
    msg = bot.send_message(message.chat.id, water_list[counter])
    bot.register_next_step_handler(msg, addMsg)


def addMsg(message):
    global counter
    water_data.append(message.text)
    counter += 1
    if counter > 8:
        water_write(water_data)
        f = open('вода_112.txt', 'rb')
        bot.send_document(message.chat.id, f)
        counter = 0
        water_data.clear()
        return
    if counter == 3 or counter == 6:
        bot.send_message(message.chat.id, water_list[counter])
        counter += 1
    msg = bot.send_message(message.chat.id, water_list[counter])
    if counter <= 8:
        bot.register_next_step_handler(msg, addMsg)


bot.infinity_polling()
