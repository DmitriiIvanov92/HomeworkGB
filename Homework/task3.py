while True:
    try:
        percent = int(input('Введите количество процентов (%) : '))
        if 4 < percent <= 20:
            print(f'{percent} процентов')
            break
        elif percent % 10 == 1:
            print(f'{percent} процент')
            break
        elif 1 < percent % 10 < 5:
            print(f'{percent} процента')
            break
        else:
            print(f'{percent} процентов')
            break
    except ValueError as error:
        print('Введите число еще раз : ')

# for percent in range(1, 101):
#     if 4 < percent <= 20:
#         print(f'{percent} процентов')
#     elif percent % 10 == 1:
#         print(f'{percent} процент')
#     elif 1 < percent % 10 < 5:
#         print(f'{percent} процента')
#     else:
#         print(f'{percent} процентов')
#
