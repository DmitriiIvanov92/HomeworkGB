''' Task 3.
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
 и возвращающую словарь, в котором ключи — первые буквы имён,
  а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.'''

thesaurus = ("Иван", "Мария", "Петр", "Илья")

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

'''Task 4:
 Написать функцию thesaurus_adv(),
 принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
  в котором ключи — первые буквы фамилий, а значения — словари, 
  реализованные по схеме предыдущего задания и содержащие записи, 
  в которых фамилия начинается с соответствующей буквы.'''

thesaurus_adv = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

def dict_in_dict(*args):
    dict_external = {}
    dict_internal = {}
    my_map = list(map(str, *args))
    print(my_map)
    split = str(my_map).split(' ')
    print(split[1])
    for name in my_map:
        dict_internal.setdefault(name[0], [])
        dict_external.setdefault(name[5], dict_internal)
    return print(dict_external)

dict_in_dict(thesaurus_adv)
