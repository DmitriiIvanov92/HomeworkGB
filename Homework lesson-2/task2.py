""" Дан список:
1) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём
до двух целочисленных разрядов:
2) Сформировать из обработанного списка строку:
3) Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
Как модифицировать это условие для чисел со знаком?"""
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# new_my_list = []
# for i in my_list:
#     if i.isdigit():
#         new_my_list.append(f'"{int(i):02}"')  # или new_my_list.extend(['', f'{int(i):02}', ''])
#     elif i.startswith('+') or i.startswith('-') and i[1:].isdigit():
#         new_my_list.append(f'"{i[0]}{int(i[1:]):02}"')
#         # new_my_list.extend(['', f'{i[0]}{int(i[1:]):02}', ''])
#     else:
#         new_my_list.append(i)
# print(new_my_list)
# message = ' '.join(new_my_list)
# print(message)

idx = 0
while idx < len(my_list):
    if my_list[idx].isdigit():
        my_list.insert(idx, '')
        my_list[idx + 1] = f'{int(my_list[idx + 1]):02}'
        my_list.insert(idx + 2, '')
        idx += 2
    elif my_list[idx].startswith('+') or my_list[idx].startswith('-') and my_list[idx][1:].isdigit():
        my_list.insert(idx, '')
        my_list[idx + 1] = f'{my_list[idx + 1]}{int(my_list[idx + 1]):02}'
        my_list.insert(idx + 2, '')
        idx += 2
    idx += 1
print(my_list)
