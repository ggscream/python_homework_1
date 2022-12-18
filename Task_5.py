# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input("Введите координату Х первой точки: "))
y1 = float(input("Введите координату Y первой точки: "))
x2 = float(input("Введите координату Х второй точки: "))
y2 = float(input("Введите координату Y второй точки: "))

from math import sqrt
distance = round(sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 3)
print(distance)

#или

from math import hypot
distance = round(hypot((x2 - x1),(y2 - y1)), 3)
print(distance)