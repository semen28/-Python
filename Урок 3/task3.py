# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.
def my_func(num1, num2, num3):
    number = [num1, num2, num3]
    number.sort()
    print(f"Наибольшими из введенных аргументов являются: {number[1]} и {number[2]}. Их сумма равна: {number[1] + number[2]}")

my_func(float(input(f"Введите 1-е число ")), float(input(f"Введите 2-е число ")), float(input(f"Введите 3-е число ")))

