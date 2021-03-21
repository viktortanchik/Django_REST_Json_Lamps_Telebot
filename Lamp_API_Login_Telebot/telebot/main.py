# Чтения из csv
import telebot
from telebot import types
import requests
from datetime import datetime
#from ..login.models import Subscriber

#print(Subscriber.objects.get(id=1))



#bot = telebot.TeleBot("959589789:AAHrmywTywnK3C-vVLUFFsC67FlLCk2ddaE")

bot = telebot.TeleBot("1342473956:AAF-9R_QfDYwgev8fssd2c58RLT7Oc28L4c")

Mode_1 = {
    "id": 1,
    "status": "1",
    "mode": "1"
}
Mode_2 = {
    "id": 1,
    "status": "1",
    "mode": "2"
}
Mode_3 = {
    "id": 1,
    "status": "1",
    "mode": "3"
}
Mode_4 = {
    "id": 1,
    "status": "1",
    "mode": "4"
}
Mode_5 = {
    "id": 1,
    "status": "1",
    "mode": "5"
}
Mode_6 = {
    "id": 1,
    "status": "1",
    "mode": "6"
}
#url = 'http://192.168.0.135:8000/api/v1/lamps/lamps/detail/1/'

url_1 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/1/'# маленькая
url_2 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/2/'# Большая лампа
url_3 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/3/'# Без батареии
url_4 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/4/'# Лампа у Юли

@bot.message_handler(commands= ['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Старт')
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! \nЯ {1.first_name} бот создан чтобы быть подопытным '
                                      'кроликом. '.format(message.from_user,bot.get_me()),parse_mode='html',
                     reply_markup=markup)
# artpetry
#674868256
#Viktor
#Tanchik
#viktortanchik
#@Yuliya_Kopylec
#print(Subscriber.objects.get(id=1))

@bot.message_handler(content_types=['text'])
def lalala(message):
    file = open(r"test.txt", "a")
    dt = datetime.now()

    print(message.from_user.username)
    user = message.from_user.username
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if user == 'artpetry' or 'viktortanchik':
        print(message.from_user.id)
        print(message.from_user.first_name)
        print(message.from_user.last_name)
        print(message.from_user.username)
        file.write(str(dt) + '\n')
        file.write(user + '\n')

        markup.row("💡 Лампа 1", "💡 Лампа 2", "💡 Лампа 3")
        if message.text == "💡 Лампа 1":
            markup.row("💡 Лампа 1 Режим 1", "💡  Лампа 1 Режим 2", "💡 Лампа 1  Режим 3")
            markup.row("💡 Лампа 1 Режим 4", "💡  Лампа 1 Режим 5", "💡 Лампа 1  Режим 6")
            markup.row("💡 Лампа 1 Выключить")
        if message.text == "💡 Лампа 2":
            markup.row("💡 Лампа 2 Режим 1", "💡  Лампа 2 Режим 2", "💡 Лампа 2  Режим 3")
            markup.row("💡 Лампа 2 Режим 4", "💡  Лампа 2 Режим 5", "💡 Лампа 2  Режим 6")
            markup.row("💡 Лампа 2 Выключить")
        if message.text == "💡 Лампа 3":
            markup.row("💡 Лампа 3 Режим 1", "💡  Лампа 3 Режим 2", "💡 Лампа 3  Режим 3")
            markup.row("💡 Лампа 3 Режим 4", "💡  Лампа 3 Режим 5", "💡 Лампа 3  Режим 6")
            markup.row("💡 Лампа 3 Выключить")

        if message.text == '💡 Лампа 1 Выключить':
            response = requests.put(url_1, json=Mode_1)
        if message.text == '💡 Лампа 1 Режим 1':
            response = requests.put(url_1, json=Mode_2)
        if message.text == '💡  Лампа 1 Режим 2':
            response = requests.put(url_1, json=Mode_3)
        if message.text == '💡 Лампа 1  Режим 3':
            response = requests.put(url_1, json=Mode_4)
        if message.text == '💡 Лампа 1 Режим 4':
            response = requests.put(url_1, json=Mode_5)
        if message.text == '💡  Лампа 1 Режим 5':
            response = requests.put(url_1, json=Mode_6)

        if message.text == '💡 Лампа 2 Выключить':
            response = requests.put(url_2, json=Mode_1)
        if message.text == '💡 Лампа 2 Режим 1':
            response = requests.put(url_2, json=Mode_2)
        if message.text == '💡  Лампа 2 Режим 2':
            response = requests.put(url_2, json=Mode_3)
        if message.text == '💡 Лампа 2  Режим 3':
            response = requests.put(url_2, json=Mode_4)
        if message.text == '💡 Лампа 2 Режим 4':
            response = requests.put(url_2, json=Mode_5)
        if message.text == '💡  Лампа 2 Режим 5':
            response = requests.put(url_2, json=Mode_6)

        if message.text == '💡 Лампа 3 Выключить':
            response = requests.put(url_3, json=Mode_1)
        if message.text == '💡 Лампа 3 Режим 1':
            response = requests.put(url_3, json=Mode_2)
        if message.text == '💡  Лампа 3 Режим 2':
            response = requests.put(url_3, json=Mode_3)
        if message.text == '💡 Лампа 3  Режим 3':
            response = requests.put(url_3, json=Mode_4)
        if message.text == '💡 Лампа 3 Режим 4':
            response = requests.put(url_3, json=Mode_5)
        if message.text == '💡  Лампа 3 Режим 5':
            response = requests.put(url_3, json=Mode_6)

        bot.send_message(message.chat.id, ".", reply_markup=markup)
        ms = message.chat.id
        file.write(str(ms) + '\n')
        file.close()
    elif user =='Yuliya_Kopylec':#Yuliya_Kopylec
        file.write(str(dt) + '\n')
        file.write(user + '\n')
        markup.row("💡 Режим 1", "💡 Режим 2", "💡 Режим 3")
        markup.row("💡 Режим 4", "💡 Режим 5")
        markup.row("💡 Выключить")
        if message.text == '💡 Выключить':
            response = requests.put(url_4, json=Mode_1)
        if message.text == '💡 Режим 1':
            response = requests.put(url_4, json=Mode_2)
        if message.text == '💡 Режим 2':
            response = requests.put(url_4, json=Mode_3)
        if message.text == '💡 Режим 3':
            response = requests.put(url_4, json=Mode_4)
        if message.text == '💡 Режим 4':
            response = requests.put(url_4, json=Mode_5)
        if message.text == '💡 Режим 5':
            response = requests.put(url_4, json=Mode_6)
        bot.send_message(message.chat.id, message.text , reply_markup=markup)
        ms = message.chat.id
        file.write(str(ms) + '\n')
        file.close()
    else:
        bot.send_message(message.chat.id,'Вы не зарегистрированные')
        file.write(dt)
        file.write(user + '\n')
        file.close()
bot.polling(none_stop=True)

