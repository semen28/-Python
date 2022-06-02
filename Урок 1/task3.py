# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
num1 = input('Введите число ')
num2 = num1 + num1
num3 = num1 + num1 + num1
summa = int(num1) + int(num2) + int(num3)
print(f"{num1} + {num2} + {num3} = {summa}")