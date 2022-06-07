# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def my_func(name, surname, city, email, phone_num):
    print(f"Данные пользователя: имя: {name} {surname}, город: {city}, электронная почта: {email}, телефон: {phone_num}")

user_name = input("Введите имя пользователя ")
user_surname = input("Введите фамилию пользователя ")
user_city = input("Введите город проживания пользователя ")
user_email = input("Введите его email ")
user_phone_num = input("Введите его телефон ")

my_func(surname=user_surname, city=user_city, phone_num=user_phone_num, name=user_name, email=user_email)

