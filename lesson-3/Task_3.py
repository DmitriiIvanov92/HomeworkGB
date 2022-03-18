''' Task 3.
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
 и возвращающую словарь, в котором ключи — первые буквы имён,
  а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.'''

thesaurus = ("Иван", "Мария", "Петр", "Илья")

# def my_dict(*args):
#     dict_names = {}
#     for name in args:
#         for str in name:
#             dict_names.setdefault(str[0], []).append(str)
#     return print(dict_names)


# my_dict(thesaurus)
# -------------------------------------------------------- ИЛИ ТАК:
# def my_dict(*args):
#     dict_names = {}
#     for name in list(*args):
#         dict_names.setdefault(name[0], []).append(name)
#     return print(dict_names)
#
#
# my_dict(thesaurus)
