
# Здесь мы импортируем модули для работы нашей программы
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.owm import OWM

from colorama import init
from colorama import Fore, Back, Style 

config_dict = config.get_default_config()
config_dict['language'] = 'ru'

owm = OWM('066afe6bc8508677626186303ec95850', config_dict) 
mgr = owm.weather_manager()



place = input("Введите город/страну: ") # Создали переменную где храница город/страна которую ввел пользователь

observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"] # Здесь из библиотеки берем температуру "temp" {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

print(Fore.YELLOW)
print("В гододе " + place + " сейчас " + w.detailed_status)
print(Fore.BLUE)
print("Сейчас температура в районе "  + str(temp) + " градусов в цельсиях")



if temp < 10:
    print("Сейчас очень холодно, рекамендуем тепло одется и выпить чаю. :)")
elif temp < 20:
    print("Сейчас прохладно, рекомендуем одется по теплее.")
else:
    print("Сейчас тепло, можете одеватся как вам захочется. :)")

input()