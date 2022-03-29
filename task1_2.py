# def odd_nums(max_value):
#     for i in range(1, max_value + 1):
#         if i % 2 != 0:
#             yield i


# def odd_nums(max_value):
#     n = 1
#     while n < max_value:
#         yield n
#         n += 2


# odd_to_15 = odd_nums(15)
# print(odd_to_15)
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(list(odd_to_15))
# print(next(odd_to_15))

odd_to_15 = 15
my_gen = (i for i in range(1, odd_to_15 + 1, 2))
print(type(my_gen))
print(next(my_gen))
print(next(my_gen))
print(tuple(my_gen))
print(next(my_gen))

