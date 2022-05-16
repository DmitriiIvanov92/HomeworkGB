"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException:

    @staticmethod
    def division_on_zero(a, b):
        try:
            result = round(a / b, 2)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

        else:
            return print(result)


my_exception = MyException()
my_exception.division_on_zero(1, 0)
my_exception.division_on_zero(1, 1)
