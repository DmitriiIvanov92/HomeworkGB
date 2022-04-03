"""  5 задача (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
Проверить работу скрипта для случая, когда все файлы находятся в разных папках."""

import json
import sys

sys.path.append("C:\pythonProject\lesson_6")

all_names = []
all_surnames = []
all_middle_names = []
all_hobbies = []

path_1, path_2, path_3 = sys.argv[1:]

everything = ["all_names", "all_surnames", "all_middle_names", "all_hobbies"]

with open(path_1, 'r', encoding='utf-8') as f1:
    with open(path_2, 'r', encoding='utf-8') as f2:
        with open(path_3, 'w', encoding='utf-8') as f:
            for line in f1:
                all_surnames.append(line.split(',')[0])
                all_names.append(line.split(',')[1])
                all_middle_names.append(line.split(',')[2].strip())
            for line in f2:
                for el in line.split(','):
                    all_hobbies.append(el.strip())
                    all_lists = [all_names, all_surnames, all_middle_names, all_hobbies]
                    parsing_data = {k: v for k, v in zip(everything, all_lists)}
                    json.dump(parsing_data, f, ensure_ascii=False)
