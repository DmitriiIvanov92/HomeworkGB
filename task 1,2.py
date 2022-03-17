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


def get_value(value):
    for k, v in my_dict.items():
        if v == value:
            return k


# user_text = input('Введите словами по английски от 1 до 10: ')
# print(get_key(user_text.lower()))  # .lower() добавил что бы в любом случае функция срабатывала
# ------------------------------------------------------------
user_text = input('Введите словами по русски от 1 до 10: ')
print(get_value(user_text.lower()))
# ----------------------------------------------------------------------
# Возвращаем ключ с заглавной буквы или строчной:
# def get_key(text):
#     if my_dict.get(text.lower()):
#         return my_dict.get(text.lower()).capitalize() if text.istitle() else my_dict.get(text.lower())


# user_text = input('Введите словами от 1 до 10: ')
# print(get_key(user_text))