# Импортируем модоли которые нам нужны для работы

import telebot

# Модуль погоды
from pyowm import OWM 
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.owm import OWM



# Здесь вводим токен для подключения созданого бота 
bot = telebot.TeleBot("8260256432:AAFtWB94_cql260R4Awn34cOyQbI5ik4mcQ", parse_mode=None)
# Здесь API ключ для того, чтобы взять данные погоды с разных точек мира
owm = OWM('066afe6bc8508677626186303ec95850') 
mgr = owm.weather_manager()

# message.text это то что нам написал пользователь и это мы спользуем


# Декоратор из библиотеки pyTelegramBotAPI. Нужет для того, чтобы бот понимал на какие сообщения ему реагировать или отвечать, и какие функчии выполнять.
@bot.message_handler(commands=['start'])
# Функция которая выполняется если прошла команда /start, и выполняется код прописанный в функции.
def send_welcome(message):
	
    bot.reply_to(message, "Привет! бот по погоде к вашим услугам!\nНапишие город или страну в которой вы хотите узнать погоду. ")
    sticker_id = "CAACAgIAAxkBAANWaPh_Itn8hwVVVMWgneVL1vtpt1oAAh1UAALNyOlKmXrXJfUsEJ02BA"
    bot.send_sticker(message.chat.id, sticker_id)


@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def greet_user(message):
    bot.reply_to(message, "Привет! " + "Я твой помошник по погоде :) Напиши город в котором хочешь узнать погоду, я быстро все сделаю! ^_-")
    
    
@bot.message_handler(content_types=['sticker'])
def get_sticker_id(message):
    print(message.sticker.file_id)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    # Здесь в тэтой переменной хранятся данные о погоде 
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
	
    bot.reply_to(message, "Окей, минутку... ")

    temp = w.temperature('celsius')["temp"]
	

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура в районе "  + str(temp) + " градусов в цельсиях" + "\n\n"
    if temp < 10:
        answer += "Сейчас очень холодно, рекамендуем тепло одется и выпить чаю. :)"
    elif temp < 20:
        answer += "Сейчас прохладно, рекомендуем одется потеплее."
    else:
        answer += "Сейчас тепло, можете одеватся как вам захочется. :)"
        
    # В bot есть функции, это функции можно брать когда нужно через bot.функция котороя нужна(в скобках аргументы)
    


    bot.send_message(message.chat.id, answer)

bot.infinity_polling( none_stop = True )