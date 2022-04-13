my_list = []
for num in range(1, 1001, 2):
    my_list.append(num ** 3)

final_sum = 0  # итоговый подсчет
for num in my_list:
    sum = 0  # сумма цифр в числе
    for check_num in str(num):
        sum += int(check_num)
    if sum % 7 == 0:
        final_sum += num
print(final_sum)  # Ответ 17485588610

final_sum = 0  # Задание с + 17
for num in my_list:
    num += 17
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)

# final_sum = 0 # Без создания списка
# for num in range(1, 1001, 2):
#     expn = pow(num, 3)
#     amount = 0
#     while expn > 0:
#         remains = expn % 10
#         expn = expn // 10
#         amount += remains
#     if amount % 7 == 0:
#         final_sum += pow(num, 3)
# print(final_sum)
