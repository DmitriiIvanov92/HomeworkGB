""" 4. * (вместо 3) Решить задачу 3 для ситуации,
когда объём данных в файлах превышает объём ОЗУ (разумеется,
не нужно реально создавать такие большие файлы,
это просто задел на будущее проекта). Также реализовать парсинг данных из файлов —
получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби:
преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
В словаре должны храниться данные, полученные в результате парсинга."""

import json
from itertools import zip_longest

# with open('name_hobby.txt', 'a', encoding='utf-8') as file:
#     with open('users.cvs', encoding='utf-8') as users:
#         with open('hobby.csv', encoding='utf-8') as hobby:
#             num_lines_users = sum(1 for line in users)
#             num_lines_hobby = sum(1 for line in hobby)
#
#             if num_lines_users < num_lines_hobby:
#                 exit(1)
#
#             users.seek(0)
#             hobby.seek(0)
#
#             for line_users, line_hobby in zip_longest(users, hobby):
#                 file.write(f'{line_users.strip()}: '
#                            f'{line_hobby.strip() if line_hobby is not None else line_hobby}\n')

with open('name_hobby.json', encoding='utf-8') as file:  # Мое решение ))) файл my_name_hobby.txt - создал еще свой файл
    with open('my_name_hobby.txt', 'a', encoding='utf-8') as name_hobby:
        my_dict = json.load(file)
        for k, v in my_dict.items():
            name_hobby.write(f'{k}: {v}\n')
