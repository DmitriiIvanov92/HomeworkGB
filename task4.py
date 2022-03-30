""" ### 4. Представлен список чисел.
Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
```

Подсказка: использовать возможности python, изученные на уроке.
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации."""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_1 = [num for i, num in enumerate(src, 0) if num > src[i - 1] and i != 0]
print(result_1)
result_2 = (num for i, num in enumerate(src, 0) if num > src[i - 1] and i != 0)
print(tuple(result_2))
result_3 = [y for x, y in zip(src, src[1:]) if y > x]
print(result_3)
new_src = []
for i in range(len(src) - 1):
     if src[i] < src[i + 1]:
        new_src.append(src[i + 1])
print(new_src)


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [i for i in src if src.count(i) == 1]
print(result)

