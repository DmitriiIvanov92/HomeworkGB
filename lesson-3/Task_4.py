'''Task 4:
 Написать функцию thesaurus_adv(),
 принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
  в котором ключи — первые буквы фамилий, а значения — словари,
  реализованные по схеме предыдущего задания и содержащие записи,
  в которых фамилия начинается с соответствующей буквы.'''

thesaurus_adv = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

def thesaurus(*args):
    my_dict = {}
    for name_surname in list(*args):
        name, surname = name_surname.split(' ')
        full_name = f'{name} {surname}'
        my_dict.setdefault(surname[0], {}).setdefault(name[0], []).append(full_name)
    return my_dict

    # sorted_dict = {x: my_dict[x] for x in sorted(my_dict)}  # Dict Comprehensions
    # return sorted_dict

print(thesaurus(thesaurus_adv))
