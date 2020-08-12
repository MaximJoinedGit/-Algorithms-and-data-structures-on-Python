# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import OrderedDict


def enter_number(text):
    """
    Проверка числа на валидность.
    """
    number = None
    while not number:
        try:
            number = int(input(text))
        except ValueError:
            print('Введено неверное значение, повторите ввод.')
    return number


n = enter_number('Введите количество компаний: ')
companies = dict()

# Для каждой компании необходимо ввести название и прибыль за 4 квартала.
for _ in range(n):
    name = input('Введите название компании: ')
    profit = enter_number('Введите прибыль компании за 4 квартала (целое число): ')
    companies[name] = profit

# Вычисляем среднее значение и сортируем словарь по выручке.
average = sum(companies.values()) / len(companies)
ordered_companies = OrderedDict(sorted(companies.items(), key=lambda money: money[1], reverse=True))

print(f'Компании, у которых прибыль больше или равна средней: '
      f'{", ".join(company for company, profit in ordered_companies.items() if profit >= average)}.\n'
      f'Компании, у которых прибыль меньше средней: '
      f'{", ".join(company for company, profit in ordered_companies.items() if profit < average)}.')
