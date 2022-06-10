# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()

from functools import reduce
my_list = [i for i in range(100, 1001) if i %2 == 0]
print(reduce(lambda x,y: x*y, my_list))

#result = 1
#for i in my_list:
#    result = result * i
#print(my_list)
#print(result)
