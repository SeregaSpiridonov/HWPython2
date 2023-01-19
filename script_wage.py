"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для
конкретных значений необходимо запускать скрипт с параметрами.
"""


from sys import argv
script_name, production_hours, rate_per_hour, premium = argv
wage = float(production_hours) * float(rate_per_hour) + float(premium)
print(wage)