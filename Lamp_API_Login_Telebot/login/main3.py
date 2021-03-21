#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
import requests
from datetime import datetime
import _csv
#from .models import Subscriber

bot = telebot.TeleBot("959589789:AAHrmywTywnK3C-vVLUFFsC67FlLCk2ddaE")

#bot = telebot.TeleBot("1342473956:AAF-9R_QfDYwgev8fssd2c58RLT7Oc28L4c")
nameID =[]
snID = []
#url = 'http://192.168.0.135:8000/api/v1/lamps/lamps/detail/1/'
#url_1 = 'http://192.168.1.6:8000/api/v1/lamps/lamps/detail/'
url_1 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/'# маленькая
#url_2 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/2/'# Большая лампа
#url_3 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/3/'# Без батареии
#url_4 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/4/'# Лампа у Юли


#url_1 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/1/'# маленькая
#url_2 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/2/'# Большая лампа
#url_3 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/3/'# Без батареии
#url_4 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/4/'# Лампа у Юли


with open('test_csv.csv', 'r', encoding='utf-8') as fp:
    reader = _csv.reader(fp, delimiter=',', quotechar='"')
    for row in reader:
        nameID.append(row[0])
        snID.append(row[1])

@bot.message_handler(commands= ['start'])
def welcome(message):
    with open('test_csv.csv', 'r', encoding='utf-8') as fp:
        reader = _csv.reader(fp, delimiter=',', quotechar='"')
        for row in reader:
            nameID.append(row[0])
            snID.append(row[1])
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Старт')
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! \nЯ {1.first_name} бот создан чтобы быть подопытным '
                                      'кроликом. Для регистрации пройдите http://ce05390-django.tw1.ru/'.format(message.from_user,bot.get_me()),parse_mode='html',
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
    flag = 0
    print(message.from_user.username)
    user = message.from_user.username
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    nameIndex = 0
    #snIndex = 0
    for name in nameID:
        if user == name:
            print("Надено")
            print(user)
            print(nameID.index(message.from_user.username))
            nameIndex = nameID.index(user)
    if user == nameID[nameIndex]:
        url = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/'+str(snID[nameIndex]) + '/'
        #url + str(snID[nameIndex]) + '/'
        response = requests.get(url)
        print(response.json())
        J = response.json()
        print(J["mode"])

        Mode_1 = {
            "id": 10,
            "status": 10,
            "mode": 10,
            "red": 100,
            "green": 100,
            "blue": 100,
        }
        Mode_1['id'] = J["id"]
        Mode_1['status'] = J["status"]
        Mode_1['mode'] = J["mode"]
        Mode_1['red'] = J["red"]
        Mode_1['green'] = J["green"]
        Mode_1['blue'] = J["blue"]
        print(message.from_user.id)
        print(message.from_user.first_name)
        print(message.from_user.last_name)
        print(message.from_user.username)
        file.write(str(dt) + '\n')
        file.write(user + '\n')
        print(message.text)
        if message.text == 'Старт' or message.text == 'Главное меню':
            markup.row("Режимы", "Ручной режим" )
            markup.row("Выключить", "Увлажнитель вкл/выкл")
        if message.text == "Ручной режим":
            markup.row("❤+", "💚+", "💙+")
            markup.row("❤-", "💚-", "💙-")
            markup.row("сброс настроек")
            markup.row("Главное меню")
        if message.text == "Режимы":
            markup.row("💡 Режим 1", "💡 Режим 2", "💡 Режим 3")
            markup.row("💡 Режим 4", "💡 Режим 5")
            markup.row("💡 Выключить")
            markup.row("Главное меню")

        if message.text == "Увлажнитель вкл/выкл":
            print('Изменения значения для увлажнителя')
            print(Mode_1['status'])
            if Mode_1['status'] == "1":
                Mode_1['status'] = 0
                print("Установка = 0")
            if Mode_1['status'] == "0":
                Mode_1['status'] = 1
                print("Установка = 1")
            response = requests.put(url_1 + str(snID[nameIndex]) + '/', json=Mode_1)


        if message.text == '💡 Выключить' or message.text == 'Выключить':
            Mode_1['mode'] = 1
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)

        if message.text == '💡 Режим 1':
            Mode_1['mode'] = 2
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)

        if message.text == '💡 Режим 2':
            Mode_1['mode'] = 3
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)

        if message.text == '💡 Режим 3':
            Mode_1['mode'] = 4
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)

        if message.text == '💡 Режим 4':
            Mode_1['mode'] = 5
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
        if message.text == '💡 Режим 5':
            Mode_1['mode'] = 6
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)

        if message.text == "❤+":
            r = Mode_1.get("red")
            r = int(r) + 25
            Mode_1["red"] = r
            Mode_1['mode'] = 7
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
            bot.send_message(message.chat.id, "🖤", reply_markup=markup)
            bot.send_message(message.chat.id, 'red ' + str(Mode_1['red']), reply_markup=markup)
            bot.send_message(message.chat.id, 'green ' + str(Mode_1['green']), reply_markup=markup)
            bot.send_message(message.chat.id, 'blue ' + str(Mode_1['blue']), reply_markup=markup)
        if message.text == "💚+":
            g = Mode_1.get("green")
            g = int(g) + 25
            Mode_1["green"] = g
            Mode_1['mode'] = 7
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
            bot.send_message(message.chat.id, "🖤", reply_markup=markup)
            bot.send_message(message.chat.id, 'red ' + str(Mode_1['red']), reply_markup=markup)
            bot.send_message(message.chat.id, 'green ' + str(Mode_1['green']), reply_markup=markup)
            bot.send_message(message.chat.id, 'blue ' + str(Mode_1['blue']), reply_markup=markup)
        if message.text == "💙+":
            b = Mode_1.get("blue")
            b = int(b) + 25
            Mode_1["blue"] = b
            Mode_1['mode'] = 7
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
            bot.send_message(message.chat.id, "🖤", reply_markup=markup)
            bot.send_message(message.chat.id, 'red ' + str(Mode_1['red']), reply_markup=markup)
            bot.send_message(message.chat.id, 'green ' + str(Mode_1['green']), reply_markup=markup)
            bot.send_message(message.chat.id, 'blue ' + str(Mode_1['blue']), reply_markup=markup)
        if message.text == "❤-":
            r = Mode_1.get("red")
            r = int(r) - 25
            Mode_1["red"] = r
            Mode_1['mode'] = 7
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
            bot.send_message(message.chat.id, "🖤", reply_markup=markup)
            bot.send_message(message.chat.id, 'red ' + str(Mode_1['red']), reply_markup=markup)
            bot.send_message(message.chat.id, 'green ' + str(Mode_1['green']), reply_markup=markup)
            bot.send_message(message.chat.id, 'blue ' + str(Mode_1['blue']), reply_markup=markup)
        if message.text == "💚-":
            g = Mode_1.get("green")
            g = int(g) - 25
            Mode_1["green"] = g
            Mode_1['mode'] = 7
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
            bot.send_message(message.chat.id, "🖤", reply_markup=markup)
            bot.send_message(message.chat.id, 'red ' + str(Mode_1['red']), reply_markup=markup)
            bot.send_message(message.chat.id, 'green ' + str(Mode_1['green']), reply_markup=markup)
            bot.send_message(message.chat.id, 'blue ' + str(Mode_1['blue']), reply_markup=markup)
        if message.text == "💙-":
            b = Mode_1.get("blue")
            b = int(b) - 25
            Mode_1["blue"] = b
            Mode_1['mode'] = 7
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
            bot.send_message(message.chat.id, "🖤", reply_markup=markup)
            bot.send_message(message.chat.id, 'red ' + str(Mode_1['red']), reply_markup=markup)
            bot.send_message(message.chat.id, 'green ' + str(Mode_1['green']), reply_markup=markup)
            bot.send_message(message.chat.id, 'blue ' + str(Mode_1['blue']), reply_markup=markup)
        if message.text == "сброс настроек":
            Mode_1["blue"] = 100
            Mode_1["green"] = 100
            Mode_1["red"] = 100
            Mode_1['mode'] = 7
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
            bot.send_message(message.chat.id, "🖤", reply_markup=markup)
            bot.send_message(message.chat.id, 'red ' + str(Mode_1['red']), reply_markup=markup)
            bot.send_message(message.chat.id, 'green ' + str(Mode_1['green']), reply_markup=markup)
            bot.send_message(message.chat.id, 'blue ' + str(Mode_1['blue']), reply_markup=markup)
        ###################################################################################################
        if int(Mode_1["blue"]) > 255:
            bot.send_message(message.chat.id, "Вы достигли придельного значения  синего цвета  ", reply_markup=markup)
            Mode_1["blue"] = 255
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
        if int(Mode_1["green"]) > 255:
            bot.send_message(message.chat.id, "Вы достигли придельного значения  зеленого цвета  ", reply_markup=markup)
            Mode_1["green"] = 255
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
        if int(Mode_1["red"]) > 255:
            bot.send_message(message.chat.id, "Вы достигли придельного значения  красного цвета  ", reply_markup=markup)
            Mode_1["red"] = 255
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
        ##############################################################
        if int(Mode_1["blue"]) < 0:
            bot.send_message(message.chat.id, "Вы достигли придельного значения  синего цвета  ", reply_markup=markup)
            Mode_1["blue"] = 0
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
        if int(Mode_1["green"]) < 0:
            bot.send_message(message.chat.id, "Вы достигли придельного значения  зеленого цвета  ", reply_markup=markup)
            Mode_1["green"] = 0
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
        if int(Mode_1["red"]) < 0:
            bot.send_message(message.chat.id, "Вы достигли придельного значения  красного цвета  ", reply_markup=markup)
            Mode_1["red"] = 0
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
        ################################################################
        bot.send_message(message.chat.id, ".", reply_markup=markup)

        ms = message.chat.id
        file.write(str(ms) + '\n')
        #file.write(message.text + '\n')
        file.close()
    else:
        with open('test_csv.csv', 'r', encoding='utf-8') as fp:
            reader = _csv.reader(fp, delimiter=',', quotechar='"')
            for row in reader:
                nameID.append(row[0])
                snID.append(row[1])
        bot.send_message(message.chat.id, 'Вы не зарегистрированные')




bot.polling(none_stop=True)

