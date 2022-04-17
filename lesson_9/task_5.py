"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки в классе {}'.format(self.title).lower())


class Pen(Stationery):
    def draw(self):
        print('Переопределили метод в классе Pen.Запуск отрисовки в классе {}'.format(self.title))


class Pencil(Stationery):
    def draw(self):
        print('Пеереопределили метод в классе Pencil.Запуск отрисовки в классе {}'.format(self.title))


class Handle(Stationery):
    def draw(self):
        print('Переопределили метод в классе Handle.Запуск отрисовки в классе {}'.format(self.title))


s = Stationery('Канцелярия')
s.draw()

pen = Pen('Ручка')
pen.draw()

pencil = Pen('Ручка')
pencil.draw()

h = Handle('Маркер')
h.draw()

