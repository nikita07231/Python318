import math


class Area:
    @staticmethod
    def triangle_area_1(a, b, c):
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def triangle_area_2(a, h):
        return 0.5 * a * h

    @staticmethod
    def square_area(a):
        return a ** 2

    @staticmethod
    def rect_area(a, b):
        return a * b


print(f"Площадь треугольника по формуле Герона: {Area.triangle_area_1(3, 4, 5)}")
print(f"Площадь треугольника через основание и высоту: {Area.triangle_area_2(6, 7)}")
print(f"Площадь квадрата: {Area.square_area(7)}")
print(f"Площадь прямоугольника: {Area.rect_area(2, 6)}")