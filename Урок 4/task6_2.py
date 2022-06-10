# Реализовать  скрипт:
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие, при котором
# повторение элементов списка прекратится.

from itertools import cycle
from random import randrange

my_list = [randrange(100) for i in range (1,4)]
print(f'Сформированный список: {my_list}')
n = 1
for i in cycle(my_list):
    if n > 10:
        break
    else:
        print(i)
    n += 1