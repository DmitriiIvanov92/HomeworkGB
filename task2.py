final_sum = 0    # Задание с + 17
for num in range(1, 1001, 2):
    new_num = num + 17
    expon = pow(new_num, 3)
    amount = 0
    while expon > 0:
        remains = expon % 10
        expon = expon // 10
        amount += remains
    if amount % 7 == 0:
        final_sum += pow(new_num, 3)
print(final_sum)

# final_sum = 0 # Без создания списка
# for num in range(1, 1001, 2):
#     expon = pow(num, 3)
#     amount = 0
#     while expon > 0:
#         remains = expon % 10
#         expon = expon // 10
#         amount += remains
#     if amount % 7 == 0:
#         final_sum += pow(num, 3)
# print(final_sum)


# my_list = []
# for num in range(1, 1001, 2):
#     my_list.append(pow(num, 3))
# final_sum = 0 # итоговый подсчет
# for num in my_list:
#    sum = 0 # сумма цифр в числе
#    for check_num in str(num):
#        sum += int(check_num)
#    if sum % 7 == 0:
#        final_sum += num
# print(final_sum)

