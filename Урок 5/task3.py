# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:#
# Иванов 23543.12
# Петров 13749.32

with open("text_for_task3", "r", encoding='utf-8') as my_file:
    list_employ = my_file.read().split()
number_list = len(list_employ)
i = 0
sum = 0
print('Фамилии сотрудников, чья зарплата менее 20 000:')
while i < number_list-2:
    if float(list_employ[i+1]) < 20000:
        print(list_employ[i])
    sum = sum + float(list_employ[i+1])
    i += 2
print(f'Средняя величина дохода сотрудников: {round(sum/number_list/2,2)}')

