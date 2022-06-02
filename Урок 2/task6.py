# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например, название. Тогда значение — список значений-характеристик, например, список названий товаров.

num_product = int(input("Введите количество товаров для каталога "))
catalog = []
product_name = []
product_price = []
product_amount = []
product_el = []

for i in range(num_product):
    n1 = input(f"Введите название товара № {i+1} ")
    n2 = float(input(f"Введите цену товара № {i+1} "))
    n3 = int(input(f"Введите количество товара № {i+1} "))
    n4 = input(f"Введите единицу измерения товара № {i+1} ")
    n = dict(название=n1, цена=n2, количество=n3, единица=n4)
    num = (i+1, n)
    catalog.append(num)
    print()
print('Ваш каталог товаров:')
print(catalog)
print()

print("Аналитика о товарах, включенных в каталог: ")
for i in range(num_product):
    product_name.append(catalog[i][1].get('название'))
    product_price.append(catalog[i][1].get('цена'))
    product_amount.append(catalog[i][1].get('количество'))
    product_el.append(catalog[i][1].get('единица'))

product_name = list(set(product_name))
product_price = list(set(product_price))
product_amount = list(set(product_amount))
product_el = list(set(product_el))

catalog_new = {'название': product_name, 'цена': product_price, 'количество': product_amount, 'единица': product_el}

print(catalog_new)




