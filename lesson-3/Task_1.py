my_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

# def get_key(key):
#     return my_dict.get(key)
#
#
# user_text = input('Введите по английски от 1 до 10: ').lower()  # .lower() - что бы всегда срабатывал (от себя добавил)
# print(get_key(user_text))
# ------------------------------------------------------------
# Возвращаем значение по ключу (для себя прописал):
# Вариант 1:
# def get_value(value):
#     for k, v in my_dict.items():
#         if v.title() == value:
#             return k.capitalize()
#         else:
#             return k
# --------------------------------- или так вариант 2:
# def get_value(value):
#     if value.istitle():
#         for k, v in my_dict.items():
#             if v.title() == value:
#                 return k.capitalize()
#     elif value.islower():
#         for k, v in my_dict.items():
#             if v == value:
#                 return k


# user_text = input('Введите по русски от 1 до 10: ')
# print(get_value(user_text))