# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


import random
with open("text_for_task5", "w+", encoding='utf-8') as my_file:
    my_file.write(" ".join([str(random.randrange(10)) for i in range(10)]))
    my_file.seek(0)
    print(sum(map(int, my_file.readline().split())))

