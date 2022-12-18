# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input("Введите координату Х: "))
y = float(input("Введите координату Y: "))

if x == 0 and y == 0:
    print("Точка не должна являться началом координат")
elif x == 0:
    print("Точка лежит на оси Y")
elif y == 0:
    print("Точка лежит на оси X")
elif x > 0 and y > 0:
    print("Точка лежит в 1 плоскости")
elif x < 0 and y > 0:
    print("Точка лежит в 2 плоскости")
elif x < 0 and y < 0:
    print("Точка лежит в 3 плоскости")
else:
    print("Точка лежит в 4 плоскости")