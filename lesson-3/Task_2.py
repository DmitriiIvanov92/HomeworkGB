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
# Возвращаем ключ с заглавной буквы или строчной:
def get_key(text):
    if my_dict.get(text.lower()):
        return my_dict.get(text.lower()).capitalize() if text.istitle() else my_dict.get(text.lower())


user_text = input('Введите по английски от 1 до 10: ')
print(get_key(user_text))