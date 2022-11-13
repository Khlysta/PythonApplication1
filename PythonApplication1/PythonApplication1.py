# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

n = int(input("input day: "))

if n > 0 and n < 8:
    if n > 5 and n < 8:
        print("weekend")
    else:
        print(n, "not weekend")
else:
    print("error")


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

 for x in [True,False]:
     for y in [True,False]:
         for z in [True,False]:
             print(x,y,z)

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
#выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input("x:"))
y = int(input("y:"))

if x != 0 and y !=0:
    
    if x < 0 and y < 0:
        print("№3")
    elif x > 0 and y > 0:
        print ("№1")
    elif x > 0 and y < 0:
        print("№4")
    else:
        print("№2")
else:
    print("error")

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input ("enter number "))
if n == 1:
    print("x>0 and y>0")
elif n == 2:
    print("x<0 and y>0")
elif n == 3:
    print("x<0 and y<0")
elif n == 4:
    print("x>0 and y<0")
else:
     print ("enter number from 1 to 4")

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Ax = float(input("Ax: "))
Ay = float(input("Ay: "))
Bx = float(input("Bx: "))
By = float(input("By: "))

S = ((Bx - Ax) ** 2 + (By - Ay) ** 2) ** 0.5
print(round(S, 2))