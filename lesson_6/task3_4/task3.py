""" 3. Есть два файла: в одном хранятся ФИО пользователей сайта,
а в другом — данные об их хобби. Известно, что при хранении данных используется принцип:
одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи"""

import csv
from itertools import zip_longest
import json

users = [
    ['Иванов', 'Иван', 'Иванович'],
    ['Петров', 'Петр', 'Петрович'],
    ['Петров', 'Петр', 'Иваныч'],
    ['Петров', 'Иван', 'Иваныч'],
    ['Сидоров', 'Алексей', 'Иваныч']
]

with open('users.cvs', 'w', encoding='utf-8') as f:
    user = csv.writer(f, lineterminator='\r')
    for line in users:
        user.writerow(line)

with open('hobby.csv', 'w', encoding='utf-8') as f:
    hobby = csv.writer(f, lineterminator='\r')
    hobby.writerow(['скалолазание', 'охота'])
    hobby.writerow(['сноуборд'])
    hobby.writerow(['горные лыжи'])
    hobby.writerow(['футбол'])

# with open('users.cvs', encoding='utf-8') as f:
#     user_reader = csv.reader(f)
#     for row in user_reader:
#         print(','.join(row))
#
# with open('hobby.csv', encoding='utf-8') as file:
#     hobby_reader = csv.reader(file)
#     for row in hobby_reader:
#         print(" ".join(row))

name_hobby_dict = {}
with open('users.cvs', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        num_lines_users = sum(1 for line in users)
        num_lines_hobby = sum(1 for line in hobby)

        if num_lines_users < num_lines_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)

        for line_users, line_hobby in zip_longest(users, hobby):
            name_hobby_dict[line_users.strip()] = line_hobby.strip() if line_hobby is not None else line_hobby
with open('name_hobby.json', 'w', encoding='utf-8') as file:
    json.dump(name_hobby_dict, file, ensure_ascii=False)

with open('name_hobby.json', encoding='utf-8') as f:
    print(json.load(f))
