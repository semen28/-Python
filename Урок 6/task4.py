# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

from random import choice

class Car:
    direction = ['влево', 'вправо', 'вперед', 'назад']

    def __init__(self, n, c, s, p=False):
        self.speed = s
        self.color = c
        self.name = n
        self.police = p
        print(f"Автомобиль: '{self.name}', цвет автомобиля: {self.color}.")
        if p == True:
            print("Это - полицейский автомобиль.")
            print()
        else:
            print("Это - не полицейский автомобиль.")
            print()

    def go(self):
        print(f"{self.name} поехал.")

    def stop(self):
        print(f"{self.name} остановился.")

    def turn(self):
        print(f"{self.name} поехал {choice(self.direction)}")

    def show_speed(self):
        return f'Скорость {self.name}: {self.speed}'

class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Скорость превышена!!!' if self.speed > 60 else super().show_speed()

class SportCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Скорость превышена!!!' if self.speed > 120 else super().show_speed()

class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Скорость превышена!!!' if self.speed > 40 else super().show_speed()

class PoliceCar(Car):
    def __init__(self, n, c, s):
        super().__init__(n, c, s, p=True)

police_car = PoliceCar('Ford Focus', 'белый', 100)
town_car = TownCar('Mini cooper', 'розовый', 70)
work_car = WorkCar('Сitroen','синий',30)
sport_car = SportCar('Lamborghini', 'оранжевый', 150)

list_of_car = [town_car, police_car, work_car, sport_car]

for i in list_of_car:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
