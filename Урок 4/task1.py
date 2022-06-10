# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def my_func(hour, rate, sucs_fee):
    try:
        salary = float(hour) * float(rate) + float(sucs_fee)
    except ValueError:
        print ("Вы ввели некорректные данные, попробуйте еще раз!")
        return
    print(f"выработка в часах: {hour}, часовая ставка: {rate}, премия: {sucs_fee}")
    print(f"Итого, зарплата к выплате: {salary}")

def my_date():
    try:
        name, n1, n2, n3 = argv
    except ValueError or SyntaxError or NameError:
        print("Вы ввели некорректные данные, попробуйте еще раз!")
        exit(0)
    my_func(n1, n2, n3)

my_date()







