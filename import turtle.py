import turtle
import random
import math
#encoding:utf-8

ekran = turtle.Screen()
ekran.setup(width = 1.0, height = 1.0)
turtle.title("Karelerin Yerleşimi")
turtle.hideturtle( )
ok = turtle.Turtle()
ok.speed(10)
ok.hideturtle()

F=("Times new roman", 12, "normal")

renkler = ['#ADC855', '#55C85F', '#55C89F', '#55A7C8', '#AD55C8', '#C8559A',
           'orange', 'magenta', 'cyan', 'DeepPink','SkyBlue1', 'gold1',
           'OliveDrab1', 'plum','yellow', 'chartreuse', 'firebrick1']

def kare(a):
    for i in range(4):
        ok.forward(a)
        ok.left(90)
    ok.penup()
    ok.forward(a)
    ok.pendown()

kenar1 = float(turtle.textinput("1. Kenar",'Dikdörtgenin bir kenarını giriniz:'))
if kenar1 == int(kenar1):
    kenar1 = int(kenar1)
kenar2 = float(turtle.textinput("2. Kenar",'Dikdörtgenin diğer kenarını giriniz:'))
if kenar2 == int(kenar2):
    kenar2 = int(kenar2)

if kenar1 >= kenar2:
    buyuk = kenar1
    kucuk = kenar2
else:
    buyuk = kenar2
    kucuk = kenar1

b = buyuk*20
k = kucuk*20

sb = 40
sk = 40 * (k/b)

ok.penup()
ok.goto(-int(b)/2,-50)
ok.pendown()

for i in range(2):
    ok.forward(b)
    ok.left(90)
    ok.forward(k)
    ok.left(90)

turtle.penup()
turtle.right(90)
turtle.goto(-int(b)/2,-100)
turtle.pendown()

if (k/20) == int(k/20):
    turtle.write("Kısa kenarı " + str(int(k/20)) + " birim ve", font=F)
else:
    turtle.write("Kısa kenarı " + str(k/20) + " birim ve", font=F)

turtle.penup()
turtle.forward(20)
turtle.pendown()

if (b/20) == int(b/20):
    turtle.write("uzun kenarı " + str(int(b/20)) + " birim olan dikdörtgenin içine", font=F)
else:
    turtle.write("uzun kenarı " + str(b/20) + " birim olan dikdörtgenin içine", font=F)

turtle.penup()
turtle.forward(40)
s = 0

while True:
    bolum = int(b/k)    
    turtle.pendown()

    if (k/20) == int(k/20):
        turtle.write(str(bolum) + " adet " + str(int(k/20)) + " x " + str(int(k/20)) + " birim karelik kare", font=F)
    else:
        turtle.write(str(bolum) + " adet " + str((k/20)) + " x " + str((k/20)) + " birim karelik kare", font=F)
    
    turtle.penup()
    turtle.forward(20)

    s = s + bolum
    r = random.choice(renkler)
 
    for i in range(bolum):
        ok.fillcolor(r)
        ok.begin_fill()
        kare(k)
        ok.hideturtle()
        ok.left(135)
        ok.penup()
        ok.forward((float(k/2))*math.sqrt(2))
        ok.left(135)
        ok.forward(k/10)

        if (k/20)==int(k/20):
            ok.write(int((k)/20), font=("Times new roman", int((k)/5), "normal"))
        else:
            ok.write(float((k)/20), font=("Times new roman", int((k)/5), "normal"))

        ok.left(180)
        ok.forward(k/10)
        ok.right(135)
        ok.forward((float(k/2))*math.sqrt(2))
        ok.left(45)
        ok.pendown()
        ok.showturtle()
        ok.end_fill()

    renkler.remove(r)  
    kalan = b % k
    
    if float(kalan) == 0:
        break
    else:
        ok.forward(float(kalan))
        ok.left(90)
        temp = b
        b = k
        k = kalan

turtle.forward(20)
turtle.pendown()
turtle.write("olmak üzere toplam olarak en az " + str(s) + " adet kare yerleştirilebilir.", font=("Times new roman", 12, "normal"))

ok.hideturtle()
ekran.mainloop()