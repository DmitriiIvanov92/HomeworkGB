''' Task 3.
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
 и возвращающую словарь, в котором ключи — первые буквы имён,
  а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.'''

# thesaurus = ("Иван", "Мария", "Петр", "Илья")

# def my_dict(*args):
#     dict_names = {}
#     for name in args:
#         print(name)
#         for str in name:
#             print(str)
#             dict_names.setdefault(str[0], []).append(str)
#     return print(dict_names)

# my_dict(thesaurus)
# -------------------------------------------------------- ИЛИ ТАК:
    # for name in list(*args):
    #     dict_names.setdefault(name[0], []).append(name)
    # return print(dict_names)


# my_dict(thesaurus)
# ------------------------------------------------------------
'''Task 4:
 Написать функцию thesaurus_adv(),
 принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
  в котором ключи — первые буквы фамилий, а значения — словари, 
  реализованные по схеме предыдущего задания и содержащие записи, 
  в которых фамилия начинается с соответствующей буквы.'''

thesaurus_adv = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

def thesaurus(*args):
    my_dict_ln = {}
    for i in args:
        split_i = i.split(' ')
        name = split_i[0]
        l_name = split_i[1]
        if l_name[0] not in my_dict_ln:
            my_dict_ln[l_name[0]] = {}
        if name[0] not in my_dict_ln[l_name[0]]:
            my_dict_ln[l_name[0]][name[0]] = []
        my_dict_ln[l_name[0]][name[0]].append(i)
    return my_dict_ln


print(thesaurus(thesaurus_adv))