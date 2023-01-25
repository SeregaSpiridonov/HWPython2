from abc import abstractmethod

"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        str_result = ''
        try:
            for list_el in self.matrix_list:
                for el in list_el:
                    str_result += str(el) + " "
                str_result += "\n"
            return f"Объект с матрицей:\n{str_result}"
        except TypeError:
            return 'Неверные входные данные.'

    def __add__(self, other):
        try:
            result_sum = [[self.matrix_list[row][col] + other.matrix_list[row][col]
                           for col in range(len(self.matrix_list[0]))] for row in range(len(self.matrix_list))]
            return result_sum
        except IndexError:
            print("Ошибка, матрицы не равны.")


mx_1 = [[31, 32], [37, 43], [51, 86]]
mx_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
mx_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]


def task_1():
    for el in [mx_1, mx_2, mx_3]:
        matrix_1 = Matrix(el)
        matrix_2 = Matrix(el)
        print(Matrix(matrix_1 + matrix_2))


task_1()

"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) 
этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся 
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def fabric_consumption(self):
        result = self.param / 6.5 + 0.5
        return round(result, 1)


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def fabric_consumption(self):
        result = self.param * 2 + 0.3
        return result


coat = Coat(48)
suit = Suit(10)


def task_2():
    for el in [coat, suit]:
        print(el.fabric_consumption)


task_2()

"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе 
должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), 
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и 
выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный 
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: 
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: 
*****\n*****\n*****.
"""


class Cell:
    def __init__(self, number_cells):
        self.number_cells = number_cells

    def __add__(self, other):
        return Cell(self.number_cells + other.number_cells)

    def __sub__(self, other):
        if self.number_cells <= other.number_cells:
            return 'Результат < или = 0'
        else:
            return Cell(self.number_cells - other.number_cells)

    def __mul__(self, other):
        return Cell(self.number_cells * other.number_cells)

    def __truediv__(self, other):
        return Cell(self.number_cells // other.number_cells)

    def make_order(self, amount):
        result = ''
        for el in range(self.number_cells // amount):
            result += '*' * amount + '\n'
        result += '*' * (self.number_cells % amount)
        return result

    def __str__(self):
        return f"Клетка с ячейками: {self.number_cells}"


one_cell = Cell(12)
two_cell = Cell(10)
print(one_cell.make_order(5))
print(one_cell + two_cell)
print(one_cell - two_cell)
print(one_cell * two_cell)
print(one_cell / two_cell)
