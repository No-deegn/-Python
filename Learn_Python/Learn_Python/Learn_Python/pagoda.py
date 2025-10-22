from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.owm import OWM

from colorama import init
from colorama import Fore, Back, Style

owm = OWM('066afe6bc8508677626186303ec95850')
mgr = owm.weather_manager()



place = input("Введите город/страну: ")

observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]

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