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
# user_text = input('Введите по английски от 1 до 10: ')
# print(get_key(user_text.lower()))  # .lower() добавил что бы в любом случае функция срабатывала
# ------------------------------------------------------------
# Возвращаем значение по ключу (для себя прописал):
def get_value(value):
    for k, v in my_dict.items():
        if v == value:
            return k


user_text = input('Введите по русски от 1 до 10: ')
print(get_value(user_text.lower()))