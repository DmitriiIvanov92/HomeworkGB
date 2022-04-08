"""
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

import os
import json

path = []
for r, d, f in os.walk('../.'):
    for file in f:
        file_path = os.path.join(r, file)
        path.append((file_path.split('.')[-1],os.stat(file_path).st_size))
        # (Разбили путь по '.' взяли последний элемент и размер файла)
max_size = max(path, key=lambda x: x[1])[1]  # lambda фильтр на макс размер, max_size[1] - получение битов
i = 1
my_dict = {}
for _ in range(len(str(max_size))):  # Проходим по длине макс файла
    i *= 10  # Проходимся по длине и умножаем на 10
    my_dict[i] = (0, [])  # Создаем ключ присвоив здесь значение все ключам 0

for file in path:
    num, ext_list = my_dict[10 ** len(str(file[1]))]  # Ходим по path пути
    ext_list.append(file[0])  # добавляем расширение .
    ext_list = list(set(ext_list))  # приводим к уникальным элекментам и списку
    print(ext_list)
    my_dict[10 ** len(str(file[1]))] = (num + 1, ext_list)  # Дополняем словарь кортежем
print(my_dict)

with open(os.path.basename(os.getcwd()) + 'summary.json', 'w', encoding='utf-8') as f_json:
    json.dump(my_dict, f_json)