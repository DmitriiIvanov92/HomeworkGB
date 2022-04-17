"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного
кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    def __init__(self, lenght, width, weight, depth):
        self._lenght = lenght
        self._width = width
        self.weight = weight
        self.depth = depth

    @property
    def calc_mass(self):
        return f'{(self._lenght * self._width * self.weight * self.depth) / 1000} тонн'


r = Road(lenght=20, width=5000, weight=25, depth=5)
print(r.calc_mass)
