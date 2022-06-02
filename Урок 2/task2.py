# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input()

number_elements = int(input("Введите число элементов списка "))

my_list = []

for i in range(number_elements):
    my_list.append(input(f"Введите {i+1}-й элемент "))

print(' ')
print(f"Исходный список: {my_list}")

if number_elements % 2 > 0:
    number_elements = number_elements -1
step = 0
while step < number_elements:
    my_list[step], my_list[step+1] = my_list[step+1], my_list[step]
    step = step + 2

print(f"Список, который получился в результате: {my_list}")




