from cProfile import label
from tkinter import *
from tracemalloc import start
import math
#Настроим окно будущего граф. интерфейса
root = Tk()
root.title('Решение квадратных уравнений')
root.geometry('500x700')
root.resizable(width=False, height=False)

#Настроим расположение полей ввода
text1 = Label (text = 'Квадратное уравнение имеет вид: ax^2+bx+c')
text1.place(x = 100, y = 30)
text2 = Label(text='Введите a, b, c:')
text2.place(x=200, y=100)
a = Entry()
a.place (x=225, y=150, width=50, height=40)
text3 = Label(text='a =')
text3.place (x = 200, y = 160)
b = Entry()
b.place (x=225, y=200, width=50, height=40)
text4 = Label(text='b =')
text4.place (x = 200, y = 210)
c = Entry()
c.place (x=225, y=250, width=50 ,height=40)
text5 = Label(text='c =')
text5.place (x = 200, y = 260)
#Логика нажатия на кнопку "Решить"
def solve():
    x=float()
    x1=float()
    x2=float()
    a_val=float(a.get())
    b_val=float(b.get())
    c_val=float(c.get())
    D = b_val*b_val-4*a_val*c_val
    if D < 0:
        output1.delete (0, END)
        output1.insert(0,'D < 0, Уравнение не имеет корней')
    elif D == 0:
        x = -b_val/(2*a_val)
        output1.delete (0, END)
        output1.insert(0, x)
    elif D > 0:
        x1 = (-b_val + math.sqrt(D))/(a_val*2)
        x2 = (-b_val - math.sqrt(D))/(a_val*2)
        output1.delete (0, END)
        output2.delete (0, END)
        output1.insert(0, x1)
        output2.insert(0, x2)
#Кнопка "Решить"
button=Button(text = "Решить", command = solve)
button.place(x=225, y=300)
#Поле вывода для D<0, x при D = 0, x1 при D>0
output1 = Entry()
output1.place (x=0, y = 400, width=500, height=100)
#Поле вывода для x2 при D>0
output2 = Entry()
output2.place (x=0, y = 500, width=500, height=100)


root.mainloop()


