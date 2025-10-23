import random

random_number = random.randint(1, 10)
user_number = int(input("Введите число от 1 до 10: " ))

if random_number == user_number:
    print("Вы выйграли! :)")
else:
    print("Вы проиграли... :(")