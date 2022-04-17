"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


# class Worker:
#     def __init__(self, name, surname, position, income):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income_wage = income['wage']
#         self._income_bonus = income['bonus']
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return f'{self.name} {self.surname} {self.position}'
#
#     def get_total_income(self):
#         return round(self._income_wage + self._income_bonus, 2)
#
#
# p = Position('Dmitrii', 'Ivanov', 'CEO', {'wage': 50000.00, 'bonus': 22999.951})
# print(p.get_full_name())
# print(p.get_total_income())
# ----------------------------------------- ДЛЯ СЕБЯ ВАРИАНТ -------------------------
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = wage
        self._bonus = bonus
        self.full_name_pos = f'{self.name} {self.surname} - position {self.position}'


class Position(Worker):
    def get_full_name_pos(self):
        return self.full_name_pos

    def get_income_salary(self):
        return round(float(self._wage) + float(self._bonus), 2)


p = Position(name=input('What is you name? '), surname=input('What is you surname? '), position=input('What is you position on work? '),
             wage=input('Enter the salary: '), bonus=input('Enter the bonus: '))
print(p.get_full_name_pos())
print(p.get_income_salary())
