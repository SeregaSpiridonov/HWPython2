import json

"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""


def user_in():
    my_list = []
    flag = True
    while flag:
        us_line = input('Введите строку(для выхода оставте пустой): ')
        if us_line == '':
            flag = False
        else:
            my_list.append(us_line + '\n')
    return my_list


def task_1():
    with open("text_task_1.txt", "w") as wr_obj:
        wr_obj.writelines(user_in())


task_1()

"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк 
и слов в каждой строке.
"""


def task_2():
    with open("text_task_2.txt") as r_obj:
        count_line = 0
        for r_line in r_obj:
            count_line += 1
            count_word = len(r_line.split())
            print(f'Строка №{count_line} - слов: {count_word}.')
        print(f'Всего строк: {count_line}.')


task_2()

"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их 
окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести 
фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""


def task_3(name_file):
    low_sal_list = []
    job_dict = dict()
    gen_salary = 0
    with open(name_file, encoding="UTF8") as r_obj:
        for r_line in r_obj:
            value, key = r_line.split()
            job_dict[key] = value
    for el in job_dict:
        gen_salary += float(el)
        if float(el) < 20000:
            low_sal_list.append(job_dict.get(el))
    print(f'{low_sal_list} < 20000')
    print(f'{gen_salary / len(job_dict)} - средняя по всем сотрудникам')


task_3("text_task_3.txt")

"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские 
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""


def task_4(name_file, res_name_file):
    num_dict = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
    result_list = []
    with open(name_file, encoding="UTF8") as r_obj:
        for r_line in r_obj:
            value, key = r_line.split(" — ")
            result_list.append(''.join([num_dict.get(int(key)), ' — ', key]))
    with open(res_name_file, "w", encoding="UTF8") as wr_obj:
        wr_obj.writelines(result_list)


task_4('text_task_4.txt', "text_task_4_result.txt")

"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""


def task_5(name_file):
    res_sum = 0
    with open(name_file, "w") as wr_obj:
        wr_obj.write('10 5 5 3 101')
    with open(name_file) as r_obj:
        num_string = r_obj.read()
        some_list = num_string.split()
    for num in some_list:
        res_sum += int(num)
    print(res_sum)


task_5('number_task_5.txt')

"""
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и 
наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. 
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def select_sum_num(some_list):
    num_list = []
    sum_num_list = 0
    num = ''
    for some_str in some_list:
        for el in some_str:
            if el.isdigit():
                num = num + el
            else:
                if num != '':
                    num_list.append(int(num))
                    num = ''
    for num in num_list:
        sum_num_list += num
    return sum_num_list


def task_6(name_file):
    res_dict = {}
    with open(name_file, encoding="UTF8") as r_obj:
        for r_line in r_obj:
            key, *value = r_line.split()
            res_dict[key[:-1]] = select_sum_num(value)
    print(res_dict)


task_6('text_task_6.txt')

"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о 
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила 
убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""


def task_7(name_file_in, out_json_name):
    firms_dict = {}
    gen_prof = 0
    count = 0
    with open(name_file_in, encoding="UTF8") as r_obj:
        for r_line in r_obj:
            key, *value = r_line.split()
            profit = int(value[1]) - int(value[2])
            firms_dict[key] = profit
            if profit > 0:
                gen_prof += profit
                count += 1
    aver_profit_dict = {"average_profit": gen_prof // count}
    result_list = [firms_dict, aver_profit_dict]
    with open(out_json_name, "w") as w_obj:
        json.dump(result_list, w_obj)


task_7('text_task_7.txt', 'file_task_7.json')
