# Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
f = open("text_for_task2", 'r', encoding='utf-8')

my_f = f.readlines()

number_str = len(my_f)
print(f'Число строк в файле: {number_str}')

for i in range(number_str):
    print (f'Число слов в {i+1}-й строке: {len(my_f[i].split())}')

f.close()