""" Task 3.
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
 и возвращающую словарь, в котором ключи — первые буквы имён,
  а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. """

names = ("Иван", "Мария", "Петр", "Илья")

def my_dict(*args):
    dict_names = {}
    for name in args:
        for str in name:
            dict_names.setdefault(str[0], []).append(str)
    return dict_names


print(my_dict(names))
# -------------------------------------------------------- ИЛИ ТАК:
def my_dict(*names):
    dict_names = {}
    for name in names:
        dict_names.setdefault(name[0], []).append(name)
    return dict_names


print(my_dict(*names))  # * - не забыть распаковать предварительно !
