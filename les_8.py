"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def date_parsing(cls, str_date):
        day, month, year = map(int, str_date.split('-'))
        return day, month, year

    @staticmethod
    def verif_date(date):
        day, month, year = date
        if 0 < day < 32 and 0 < month < 13 and 999 < year < 10000:
            return 'Ok'
        else:
            return 'Err date.'


print(Date.verif_date(Date.date_parsing('31-01-2022')))
print(Date.date_parsing('10-11-2022'))

"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на 
данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать 
эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


def task_2():
    num_1 = input('Введите 1 число: ')
    num_2 = input('Введите 2 число: ')
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        if num_2 == 0:
            raise ZeroDiv('Нельзя делить на ноль')
    except ValueError:
        print('Вы ввели не число!')
    except ZeroDiv as err:
        print(err)
    else:
        print(f'Все ок, результат : {num_1 / num_2}')


task_2()

"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо 
только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит 
работу скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами 
выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода 
пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только 
если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить 
соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class NumControl(Exception):
    def __init__(self, txt):
        self.txt = txt


def task_3():
    some_list = []
    while True:
        num = input('Enter number(for exit "stop"): ')
        if num == 'stop':
            break
        try:
            if num.isdigit() is False:
                raise NumControl('Entered string is not number!')
        except NumControl as err:
            print(err)
        else:
            some_list.append(int(num))
    print(some_list)


task_3()

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, 
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и 
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, 
а также других данных, можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, 
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Stock:
    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.place = {}

    def __str__(self):
        return f'{self.place}'

    def receipt(self, product, quantity):
        try:
            if type(quantity) is not int:
                raise NumControl('Введённое количество не число!')
        except NumControl as err:
            print(err)
        else:
            if self.place.get(product.name) is None:
                self.place[product.name] = quantity
            else:
                self.place[product.name] += quantity

    def consumption(self, product, quantity):
        try:
            if type(quantity) is not int:
                raise NumControl('Введённое количество не число!')
        except NumControl as err:
            print(err)
        else:
            if self.place.get(product.name) is None:
                print("Такого нет на складе!")
            elif self.place[product.name] < quantity:
                print("Нельзя забрать больше чем есть!")
            else:
                self.place[product.name] -= quantity


class OfficeEquipment:
    total_quantity = 0

    def __init__(self, name, size, weight):
        self.name = name
        self.size = size
        self.weight = weight
        OfficeEquipment.total_quantity += 1

    def __str__(self):
        return self.name


class Printer(OfficeEquipment):
    def __init__(self, name, size, weight, color=False):
        super().__init__(name, size, weight)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, name, size, weight, auto_feeder=False):
        super().__init__(name, size, weight)
        self.auto_feeder = auto_feeder


class Copier(OfficeEquipment):
    def __init__(self, name, size, weight, size_paper):
        super().__init__(name, size, weight)
        self.size_paper = size_paper


obj_1 = Printer('HP-3120', (25, 10, 15), 5,)
obj_2 = Printer('Canon-ip7240', (20, 10, 15), 4, True)
obj_3 = Scanner('Canon-sc6570', (20, 5, 15), 2, True)
obj_4 = Copier('Brother-501v', (30, 50, 20), 10, 'A3-A5')

stock = Stock('Первый')
stock.receipt(obj_1, 1)
stock.receipt(obj_2, 2)
stock.receipt(obj_3, 5)
stock.receipt(obj_4, 1)
print(stock)
stock.consumption(obj_3, 1)
print(stock)

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте 
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры 
класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного 
результата.
"""


class ComplexNum:
    def __init__(self, num_a, num_b):
        self.num_a = num_a
        self.num_b = num_b

    def __str__(self):
        if self.num_b < 0:
            sign = '-'
            self.num_b *= -1
        else:
            sign = '+'
        return f'z = {self.num_a} {sign} {self.num_b}i'

    def __add__(self, other):
        num_2 = self.num_b + other.num_b
        if num_2 < 0:
            sign = '-'
            num_2 *= -1
        else:
            sign = '+'
        return f'z = {self.num_a + other.num_a} {sign} {num_2}i'

    def __mul__(self, other):
        num_2 = self.num_b * other.num_a + self.num_a * other.num_b
        if num_2 < 0:
            sign = '-'
            num_2 *= -1
        else:
            sign = '+'
        return f'z = {self.num_a * other.num_a - self.num_b * other.num_b} {sign} {num_2}i'


z_1 = ComplexNum(3, 7)
z_2 = ComplexNum(-5, 9)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
