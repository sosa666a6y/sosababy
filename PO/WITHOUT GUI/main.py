import math


f = open ('UserData.txt', 'w')
print ("Квадратное уравнение имеет вид - ax^2+bx+c")
print ("Введите значения a, b и c")
a = float(input("Введите a = "))
b = float(input("Введите b = "))
c = float (input("Введите c = "))
f. write('Пользователь ввёл: a = ')
f.write(str(a))
f. write (', b =  ')
f.write (str(b))
f. write (', c =  ')
f.write(str(c))
f. write ('\nУравнение пользователя -  ')
f.write (str(a))
f.write ('x^2+')
f.write (str(b))
f.write('x+')
f.write(str(c))
x = float()
x1 = float()
x2 = float()
print (f"Ваше уравнение = {a}x^2+{b}x+{c}")
d = (b*b)-(4*a*c)
print ("Дискриминант равен = ", d)
f.write("\nПолученный дискриминант = ")
f.write(str(d))
if d < 0:
    print ("Корней уравнения нет, так как дискриминант меньше 0")
    f.write('\nКорней уравнения нет, так как дискриминант меньше 0')
elif d == 0:
    x = -b/(2*a)
    print ("Корень уравнения только один:", x)
    f.write("\nКорень уравнения только один: ")
    f.write (str(x))


elif d > 0:
    x1 = (-b + math.sqrt(d))/(a*2)
    x2 = (-b - math.sqrt(d))/(a*2)
    print ("Корни уравнения равны: x1 =", x1, "x2 = ", x2)
    f.write("\nКорни уравнения равны: x1 = ")
    f.write (str(x1) )
    f.write('\tx2 = ')
    f.write(str(x2))
f.close()

