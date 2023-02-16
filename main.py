import telebot
import random
from telebot import types


f = open('список квартир.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

f = open('адреса.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()

bot = telebot.TeleBot('6100884985:AAHSHjdl47WLZi4DPVYVY6rNKEv25sHoDcU')

@bot.message_handler(commands=["start"])
def start(m, res=False):

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Квартира")
        item2=types.KeyboardButton("Адрес")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nКвартира для получения названия квартиры\nАдрес для получения адреса ',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):

    if message.text.strip() == 'Квартира' :
            answer = random.choice(facts)

    elif message.text.strip() == 'Адрес':
            answer = random.choice(thinks)

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)