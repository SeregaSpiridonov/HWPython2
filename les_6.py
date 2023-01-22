"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    __traffic_light_color = None

    def running(self):
        for count in range(3):
            self.__traffic_light_color = 'red'
            print('\033[31m{}'.format(self.__traffic_light_color), end='')
            time.sleep(7)
            print('\r', end='')
            self.__traffic_light_color = 'yellow'
            print('\033[33m{}'.format(self.__traffic_light_color), end='')
            time.sleep(2)
            print('\r', end='')
            self.__traffic_light_color = 'green'
            print('\033[32m{}'.format(self.__traffic_light_color), end='')
            time.sleep(10)
            print('\r', end='')
        print('\033[0m')


task_1 = TrafficLight()
task_1.running()

"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    _road_length = 5000
    _road_width = 20

    def mass_asphalt(self, road_thickness=1):
        result_mass = self._road_length * self._road_width * 25 * road_thickness
        print(f'{result_mass / 1000} т.')


task_2 = Road()
task_2.mass_asphalt(5)

"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода 
с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, worker_name, worker_surname, worker_position, wage, bonus):
        self.worker_name = worker_name
        self.worker_surname = worker_surname
        self.worker_position = worker_position
        self._worker_income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.worker_name} - {self.worker_surname}')

    def get_total_income(self):
        print(self._worker_income['wage'] + self._worker_income['bonus'])


task_3 = Position('Иван', 'Иванов', 'Рабочий', 25000, 5000)
task_3.get_full_name()
task_3.get_total_income()

"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, car_speed, car_color, car_name, car_is_police):
        self.car_speed = car_speed
        self.car_color = car_color
        self.car_name = car_name
        self.car_is_police = car_is_police

    def go(self):
        if self.car_speed > 0:
            print('Машина поехала.')

    def stop(self):
        if self.car_speed == 0:
            print('Машина остановилась.')

    def turn(self, direction=0):
        if direction == 1:
            print('Повернула налево.')
        elif direction == 2:
            print('Повернула направо.')
        elif direction == 0:
            print('Едет прямо.')

    def show_speed(self):
        print(f'Текущая скорость {self.car_speed} км/ч.')


class TownCar(Car):
    def __init__(self, car_speed, car_color, car_name, car_is_police):
        super().__init__(car_speed, car_color, car_name, car_is_police)

    def show_speed(self):
        if self.car_speed > 60:
            print('Внимание, превышение скорости!')
        print(f'Текущая скорость {self.car_speed} км/ч.')


class SportCar(Car):
    def __init__(self, car_speed, car_color, car_name, car_is_police):
        super().__init__(car_speed, car_color, car_name, car_is_police)


class WorkCar(Car):
    def __init__(self, car_speed, car_color, car_name, car_is_police):
        super().__init__(car_speed, car_color, car_name, car_is_police)

    def show_speed(self):
        if self.car_speed > 40:
            print('Внимание, превышение скорости!')
        print(f'Текущая скорость {self.car_speed} км/ч.')


class PoliceCar(Car):
    def __init__(self, car_speed, car_color, car_name, car_is_police):
        super().__init__(car_speed, car_color, car_name, car_is_police)


task_4_1 = TownCar(60, 'red', 'Town Car', False)
task_4_2 = SportCar(0, 'yellow', 'Sport Car', False)
task_4_3 = WorkCar(41, 'black', 'Work Car', False)
task_4_4 = PoliceCar(60, 'blue', 'Police Car', True)


def test_task_4():
    for el in [task_4_1, task_4_2, task_4_3, task_4_4]:
        print(el.car_name, el.car_color, el.car_speed, el.car_is_police)
        el.go(), el.stop(), el.turn(2), el.show_speed()
        print()


test_task_4()

"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, stationery_title):
        self.stationery_title = stationery_title

    def draw(self):
        print('«Запуск отрисовки»')


class Pen(Stationery):
    def __init__(self, stationery_title):
        super().__init__(stationery_title)

    def draw(self):
        print('«Запуск отрисовки ручкой»')


class Pencil(Stationery):
    def __init__(self, stationery_title):
        super().__init__(stationery_title)

    def draw(self):
        print('«Запуск отрисовки карандашом»')


class Handle(Stationery):
    def __init__(self, stationery_title):
        super().__init__(stationery_title)

    def draw(self):
        print('«Запуск отрисовки маркером»')


task_5_1 = Pen('Pen')
task_5_2 = Pencil('Pencil')
task_5_3 = Handle('Handle')


def test_task_5():
    for el in [task_5_1, task_5_2, task_5_3]:
        el.draw()


test_task_5()
