# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

f = open("result_text_for_task4", "w", encoding='utf-8')
with open("text_for_task4", "r", encoding='utf-8') as my_file:
    while True:
        line = my_file.readline()
        line = line.replace('One', 'Один')
        line = line.replace('Two', 'Два')
        line = line.replace('Three', 'Три')
        line = line.replace('Four', 'Четыре')
        line = f.write(line)
        if not line:
            break
f.close()