"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        return f'{self.name} машина поехала'

    def car_stop(self):
        return f'{self.name} машина остановилась'

    def car_turned(self, direction):
        return f'Машина повернула на {direction}'

    def show_speed(self):
        return f'Текущая скорость: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости!\nCкорость более {self.speed} км/ч'
        else:
            return f'{self.speed} км/ч'


class SportCar(Car):
    def car_go(self):
        print(f'ПОЕХАЛИ!')

    def car_stop(self):
        print(f'ОСТАНАЛИВАЕТСЯ!')

    def car_turned(self, direction):
        print(f'Куда повернем КЭП? Поварачивам на {direction}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости!\nCкорость более {self.speed} км/ч'
        else:
            return self.speed


class PoliceCar(Car):
    def show_speed(self):
        return f'Машина МЧИТСЯ очень быстро {self.speed} км/ч'

    def what_this_car(self):
        if self.name == 'Bentley':
            return f'Твой выбор {self.name} и это - {self.is_police}'


car = Car(speed=80, color='White', name='Toyota', is_police=False)
print(car.show_speed())
print(car.car_turned('лево!'))

town_car = TownCar(speed=160, color='Black', name='BMW', is_police=True)
print(town_car.show_speed())
print(town_car.car_turned('право!'))

work_car = WorkCar(speed=60, color='blue', name='Mersedes', is_police=True)
print(work_car.show_speed())
print(work_car.car_turned('разВорот'))

police_car = PoliceCar(speed=250, color='green', name='Bentley', is_police=True)
print(police_car.what_this_car())
print(police_car.show_speed())
