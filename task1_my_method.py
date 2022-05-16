"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:
    data = [number for number in range(1, 32)]  # Или можно использовать изначально как я делал  1 <= data <= 31
    month = [number for number in range(1, 13)]  # 1 <= month <= 12
    year = [year for year in range(4001)]  # 2022 <= year <= 4000

    @classmethod
    def __validation_day(cls, day):
        for date in cls.data:
            if day <= date:
                return day

        print('Не правильно выбрана дата в календарном месяце!')

    @classmethod
    def __validation_month(cls, month):
        for months in cls.month:
            if month <= months:
                return month

        print('Введите месяц от 1 до 12')

    @classmethod
    def __validation_year(cls, year):
        for years in cls.year:
            if year <= years:
                return year

        print('Выберите другой год!')

    def __init__(self, data):
        day, month, year = map(int, data.split('-'))
        if self.__validation_day(day) and self.__validation_month(month) and self.__validation_year(year):
            self.day = day
            self.month = month
            self.year = year

    @staticmethod
    def get_data_validation(data_string):
        day, month, year = map(int, data_string.split('-'))
        if 1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 4000:
            return data_string

        # 2 вариант ч/з @staticmethod:
        # data_list = []
        # for i in map(int, data_string.split('-')):
        #     data_list.append(i)
        # if 1 <= data_list[0] <= 31 and 1 <= data_list[1] <= 12 and 0 <= data_list[2] <= 4000:
        #     return data_string
        else:
            return 'Ошибка ввода данных!'


if __name__ == '__main__':
    my_data = Data('18-05-1970')  # Валидацию сделал в методе @classmethod через атрибуты cls
    print(my_data)
    my_data2 = Data('33-14-2022')
    print(my_data.get_data_validation('33-05-1970'))  # Другой метод валидации
    print(my_data.get_data_validation('18-05-1970'))
