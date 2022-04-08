"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os

path = []
for r, d, f in os.walk('..'):
    for file in f:
        path_file = os.path.join(r, file)  # прописали путь
        path.append(os.stat(path_file).st_size)  # высчитывает размер файлов
max_size = max(path)  # Отсортировали максимальный файл
i = 1
dict = {}
for _ in range(len(str(max_size))):  # Проходим по длине макс файла
    i *= 10  # Проходимся по длине и умножаем на 10
    dict[i] = 0  # Создаем ключ присвоив здесь значение все ключам 0
for file in path:  # Ходим по path пути
    dict[10 ** len(str(file))] += 1  # Дополняем словарь values по ключу

print(dict)
