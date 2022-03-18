'''Task 4:
 Написать функцию thesaurus_adv(),
 принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
  в котором ключи — первые буквы фамилий, а значения — словари,
  реализованные по схеме предыдущего задания и содержащие записи,
  в которых фамилия начинается с соответствующей буквы.'''

thesaurus_adv = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

def thesaurus(*args):
    my_dict = {}
    for i in list(*args):
        i = i.split(' ')
        name = i[0]
        sername = i[1]
        full_name = f'{name} {sername}'
        my_dict.setdefault(sername[0], {}).setdefault(name[0], []).append(full_name)
    return my_dict

print(thesaurus(thesaurus_adv))