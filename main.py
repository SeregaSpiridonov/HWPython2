"""
1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки
и сохраните в переменные, затем выведите на экран.
2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции.
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее
сообщение.
6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите
численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат
спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно
натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
"""
def task_1():
    number_1 = 5
    number_3 = number_1 * 2
    line_one = "Привет "
    number_2 = int(input('Введите первое число: '))
    number_4 = int(input('Введите второе число: '))
    line_two = input('Введите имя: ')
    print(number_1)
    print(number_3)
    print(f'{line_one}{line_two}')
    print(f'Число 1 = {number_2}, Число 2 = {number_4}, Сумма = {number_2 + number_4}.')
#task_1()

def task_2(my_time):
    seс = my_time % 60
    min = my_time // 60
    hour = min // 60
    min = min - hour * 60
    print(f'{hour}:{min}:{seс}')
#task_2(int(input('Введите время в секундах: ')))

def task_3(number):
    number_3 = number + number + number
    number_2 = number + number
    sum_number = int(number) + int(number_2) + int(number_3)
    print(f'result = {sum_number}.')
#task_3(input('n = '))

def task_4(number):
    max_num = number % 10
    while number != 0:
        number = number // 10
        cur_num = number % 10
        if max_num < cur_num:
            max_num = cur_num
    print(f'Наибольшая цифра в числе => {max_num}.')
#task_4(int(input('Введите число: ')))

def task_5_and_6():
    revenue = int(input('Введите прибыль: '))
    costs = int(input('Введите издержки: '))
    if revenue > costs:
        print('Компания работает в прибыль — выручка больше издержек.')
        profitability = revenue - costs
        workers_num = int(input('Сколько работников в фирме?: '))
        print(f'Всего доходов: {profitability}, в пересчёте на одного работника: {profitability / workers_num}.')
    elif revenue == costs:
        print('Компания работает в ноль. Прибыль равна убыткам.')
    else:
        print('Компания работает в убыток — издержки больше выручки.')
task_5_and_6()

def task_7():
    next_day = int(input('Число километров в первый день: '))
    kilometer_result = int(input('Требуемое колличество километров за пробежку: '))
    num_day = 1
    while next_day < kilometer_result:
        percent_10 = next_day / 100 * 10
        next_day = next_day + percent_10
        num_day = num_day + 1
    print(f'Ответ: на {num_day} день спортсмен достиг результата — не менее {kilometer_result} км.')
#task_7()