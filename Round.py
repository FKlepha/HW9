from math import pi


class Round:
    def __init__(self, radius):
        self.radius = radius

    def round_lenth(self):
        lenth = 2 * pi * (self.radius)
        print(f'Длина круга:   {lenth}')

    def round_area(self):
        area = (pi * (self.radius) ** 2)
        print(f'Площадь круга:   {area}')

#   def info(self):
#       print(lenth)
#       print(area)


radius = Round(int(input('Введите радиус окружности')))
lenth = Round.round_lenth(radius)
area = Round.round_area(radius)




