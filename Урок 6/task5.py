# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title="канцелярскую принадлежность."):
        self.title = title

    def draw(self):
        print(f"Начинаем отрисовку. Выбираем {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Подписываем контракт ручкой фирмы '{self.title}'.")

class Pencil(Stationery):
    def draw(self):
        print(f"Начинаем рисовать карандашем фирмы '{self.title}'.")

class Handle(Stationery):
    def draw(self):
        print(f"Для работы на флипчарте используем маркер фирмы '{self.title}'.")

my_stat = Stationery()
my_pencil = Pencil('KOH-I-NOOR')
my_pen = Pen('Parker')
my_handle = Handle('TOUCH')

my_stat.draw()
my_pencil.draw()
my_pen.draw()
my_handle.draw()




