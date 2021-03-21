import telebot
from telebot import types
import requests
from datetime import datetime
import _csv
#from .models import Subscriber

#bot = telebot.TeleBot("959589789:AAHrmywTywnK3C-vVLUFFsC67FlLCk2ddaE") # Юки бот

bot = telebot.TeleBot("1342473956:AAF-9R_QfDYwgev8fssd2c58RLT7Oc28L4c") # Тестовый бот

nameID =[] # хранения Ников телеграма

snID = [] # для Серийного номера лампы

################################# для JSON ###################################
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
###################################################################################
#url = 'http://192.168.0.135:8000/api/v1/lamps/lamps/detail/1/'

url_1 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/'# маленькая
#url_2 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/2/'# Большая лампа
#url_3 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/3/'# Без батареии
#url_4 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/4/'# Лампа у Юли

#url_1 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/1/'# маленькая
#url_2 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/2/'# Большая лампа
#url_3 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/3/'# Без батареии
#url_4 = 'http://ce05390-django.tw1.ru/api/v1/lamps/lamps/detail/4/'# Лампа у Юли

# читайм файл с никами и серийниками
with open('test_csv.csv', 'r', encoding='utf-8') as fp:
    reader = _csv.reader(fp, delimiter=',', quotechar='"')
    for row in reader:
        nameID.append(row[0])
        snID.append(row[1])
# запускаем бот в первый раз
@bot.message_handler(commands= ['start'])
def welcome(message):
    # читайм файл с никами и серийниками, на всякий случай хз)
    with open('test_csv.csv', 'r', encoding='utf-8') as fp:
        reader = _csv.reader(fp, delimiter=',', quotechar='"')
        for row in reader:
            nameID.append(row[0]) # сохраняем ник в переменную
            snID.append(row[1])# сохраняем серийный номер
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Обновить')
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


# MAIN бота
@bot.message_handler(content_types=['text'])
def lalala(message):

    file = open(r"test.txt", "a") # для теств, будем дописевать что кто и когда делал.
    dt = datetime.now() # переменна для даты
    print(message.from_user.username)
    user = message.from_user.username
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    nameIndex = 0 # индекс для в списке находится иммя
    #snIndex = 0
    for name in nameID: # перебор списка
        if user == name: # поиск совпадения
            print("Надено")
            print(user)
            print(nameID.index(message.from_user.username))
            nameIndex = nameID.index(user)  # сохраняем ник

    if user == nameID[nameIndex]: # выводим кнопки
        markup.row("Лампа  Режим 1", "Лампа  Режим 2", "Лампа   Режим 3")
        markup.row("Лампа  Режим 4", "Лампа  Режим 5")
        markup.row("Лампа  Выключить")

        print(message.text)
        print(message.from_user.id)
        print(message.from_user.first_name)
        print(message.from_user.last_name)
        print(message.from_user.username)

        if message.text == 'Лампа  Выключить':
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_1)
            print('OFF')
        if message.text == 'Лампа  Режим 1':
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_2)
        if message.text == 'Лампа  Режим 2':
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_3)
        if message.text == 'Лампа   Режим 3':
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_4)
        if message.text == 'Лампа  Режим 4':
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_5)
        if message.text == 'Лампа  Режим 5':
            response = requests.put(url_1 + str(snID[nameIndex])+'/', json=Mode_6)

        bot.send_message(message.chat.id, ".", reply_markup=markup)
        ms = message.chat.id
        file.write(str(ms) + '\n')
        file.close()

    else:
        with open('test_csv.csv', 'r', encoding='utf-8') as fp:
            reader = _csv.reader(fp, delimiter=',', quotechar='"')
            for row in reader:
                nameID.append(row[0])
                snID.append(row[1])
        bot.send_message(message.chat.id, 'Вы не зарегистрированные')




bot.polling(none_stop=True)

