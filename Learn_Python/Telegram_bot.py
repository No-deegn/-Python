# Импортируем модоли которые нам нужны для работы

import telebot
import numexpr
# Модуль погоды
from pyowm import OWM 
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.owm import OWM



# Здесь вводим токен для подключения созданого бота 
bot = telebot.TeleBot("8260256432:AAFtWB94_cql260R4Awn34cOyQbI5ik4mcQ", parse_mode=None)
# Здесь API ключ для того, чтобы взять данные погоды с разных точек мира

config_dict = config.get_default_config()
config_dict['language'] = 'ru'

owm = OWM('066afe6bc8508677626186303ec95850', config_dict) 
mgr = owm.weather_manager()

# message.text это то что нам написал пользователь и это мы спользуем


# Декоратор из библиотеки pyTelegramBotAPI. Нужет для того, чтобы бот понимал на какие сообщения ему реагировать или отвечать, и какие функчии выполнять.
@bot.message_handler(commands=['start'])
# Функция которая выполняется если прошла команда /start, и выполняется код прописанный в функции.
def send_welcome(message):
	
    bot.reply_to(message, "Привет! бот по погоде к вашим услугам!\nНапишие город или страну в которой вы хотите узнать погоду. ")
    sticker_id = "CAACAgIAAxkBAANtaPnIxXys_9r2clUpPo3xYRXtXL4AArF4AALOTfhJDe_3I4ggf3c2BA"
    bot.send_sticker(message.chat.id, sticker_id)
    bot.send_message(message.chat.id, "Напиши слово 'Команды' и я покажу что умею ")

@bot.message_handler(func=lambda message: message.text.lower() == "команды")
def greet_user(message):
    bot.reply_to(message, "Команды: /calculator, /game")


@bot.message_handler(commands=['game'])
def greet_user(message):
    bot.reply_to(message, "Приветик! Давай сыграем угодай число! напиши мне любое число от 1 до 10")
    @bot.message_handler(content_types=['text'])
    def send_echo(message):
        import random
        
        number = random.randint(1, 10)
        user = message.text

        if number == user:
            print("Молодец! ты выиграл!")
        else:
            print("Блин... не угодал, давай еще!")

@bot.message_handler(commands=['calculator'])
def greet_user(message):
    bot.reply_to(message, "Здравсствуйте! Вы используете функцию каркулятор, пожалуйста прочтите инструкцию к ней.")
    bot.send_message(message.chat.id, "\nИнструкция \nЧтобы использовать каркулятор просто напишите то действие которое вам нужно сделать: \nСложение(+), вычетание(-), умнажение(*), деление(/), деление без остатка(//), Возвести в сепень(**) \n\nПример: 34+3 или 2+4*2**45/4")
    bot.register_next_step_handler(message, cals)
    def cals(message):
    # Создаем пременную чтобы сохранить то, что написал пользоватесь 
      user = str(message.text)
      result = numexpr.evaluate(user)
      bot.send_message(message.chat.id, "Результат: " + result)
    bot.polling()


@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def greet_user(message):
    bot.reply_to(message, "Привет! " + "Я твой помошник по погоде :) Напиши город в котором хочешь узнать погоду, я быстро все сделаю! ^_- \nИли напиши слово \"команды\" и узнай чтоя умею ")
    
    
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
        answer += "Сейчас прохладно, рекомендую одется потеплее."
    else:
        answer += "Сейчас тепло, можете одеватся как вам захочется. :)"
        
    # В bot есть функции, это функции можно брать когда нужно через bot.функция котороя нужна(в скобках аргументы)
    


    bot.send_message(message.chat.id, answer)

bot.infinity_polling( none_stop = True )