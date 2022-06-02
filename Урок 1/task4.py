#  Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#  Для решения используйте цикл while и арифметические операции.

num_base = int(input("Введите число "))
result = 0
if num_base <= 9:
    result = num_base
else:
    while num_base != 0:
        remaind = num_base % 10
        if remaind > result:
            result = remaind
        num_base = num_base//10

print(f"Самая большая цифра во введенном числе: {result}")
