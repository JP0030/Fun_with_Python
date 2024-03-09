# JP0030

import turtle

wn=turtle.Screen()          
wn.setup(640,640)           
wn.title("Laptop")
wn.bgcolor("blue")

b=turtle.Turtle()
b.shapesize(1.5)
b.speed(0)

b.begin_fill()
b.color("#848283","#848283")
b.seth(90)
b.fd(320)
b.seth(180)
b.fd(320)
b.seth(-90)
b.fd(640)
b.seth(0)
b.fd(320)
b.seth(90)
b.fd(320)
b.end_fill()

b.bk(10)
b.begin_fill()
b.color("white","white")
b.seth(135)
b.circle(35,36)
b.circle(300,20)
b.seth(-60)
b.circle(-50,115)
b.fd(30)
b.seth(-100)
b.circle(30,55)
b.seth(100)
b.circle(-10,55)
b.circle(-1.5,150)
b.circle(20,70)
b.circle(494,22)
b.end_fill()

b.up()
b.seth(90)
b.fd(125)
b.down()
b.begin_fill()
b.color("black","black")
b.circle(30,64)
b.circle(-55,34)
b.circle(-7,101)
b.circle(-75,27)
b.end_fill()

b.color("white")
b.begin_fill()
b.color("white","white")
b.up()
b.seth(-90)
b.fd(3)
b.down()
b.seth(-175)
b.fd(20)
b.circle(4,160)
b.fd(23)
b.end_fill()

b.up()
b.seth(-90)
b.fd(70)
b.down()
b.begin_fill()
b.color("black","black")
b.seth(-163)
b.circle(-160,54)
b.seth(-41)
b.circle(160,30)
b.seth(-4)
b.circle(160,25)
b.end_fill()

b.up()
b.seth(-90)
b.fd(50)
b.down()
b.begin_fill()
b.color("black","black")
b.seth(180)
b.circle(-160,25)
b.seth(-29)
b.circle(160,26)
b.end_fill()

b.up()
b.seth(180)
b.fd(2)
b.seth(90)
b.fd(156)
b.seth(180)
b.fd(105)
b.down()

b.begin_fill()
b.color("#fae383","#fae383")
b.seth(65)
b.circle(200,50)
b.circle(10,90)
b.circle(80,30)
b.seth(-117)
b.circle(200,35)
b.seth(-20)
b.circle(-100,33)
b.seth(16)
b.fd(20)
b.end_fill()

b.color("black")
b.up()
b.seth(65)
b.circle(200,35)
b.down()
b.begin_fill()
b.color("black","black")
b.pensize(1)
b.circle(200,5)
b.pensize(2)
b.circle(200,10)
b.circle(10,90)
b.circle(80,20)
b.pensize(1)
b.circle(80,10)
b.seth(48)
b.circle(-80,30)
b.seth(-10)
b.fd(7)
b.seth(-68)
b.fd(50)
b.end_fill()

b.up()
b.seth(-97)
b.fd(125)
b.down()
b.begin_fill()
b.color("#1a9a1a","#46e026")
b.seth(65)
b.circle(150,35)
b.circle(17,147)
b.circle(150,34)
b.seth(-46)
b.fd(15)
b.seth(18)
b.fd(20)
b.end_fill()

b.color("black")
b.up()
b.bk(7)
b.down()
b.begin_fill()
b.color("black","black")
b.seth(55)
b.circle(70,55)
b.circle(5,127)
b.circle(70,58)
b.end_fill()

b.up()
b.seth(-60)
b.fd(23)
b.down()
b.begin_fill()
b.color("black","black")
b.seth(150)
b.circle(250,50)
b.seth(22)
b.circle(-250,30)
b.seth(-12)
b.circle(-250,20)
b.end_fill()

b.up()
b.seth(-60)
b.fd(12)
b.down()
b.begin_fill()
b.color("black","black")
b.seth(-155)
b.circle(-250,50)
b.seth(-27)
b.circle(250,25)
b.seth(1)
b.circle(250,25)
b.end_fill()

b.up()
b.seth(92)
b.fd(35)
b.down()
b.begin_fill()
b.color("#a6a6a6","#a6a6a6")
b.seth(65)
b.circle(200,30)
b.seth(60)
b.fd(30)
b.circle(-15,125)
b.fd(25)
b.circle(3,158)
b.fd(45)
b.circle(-35,84)
b.seth(-90)
b.fd(198)
b.seth(135)

b.circle(35,36)
b.circle(300,16)
b.end_fill()

b.color("black")
b.up()
b.seth(90)
b.fd(200)
b.seth(0)
b.fd(30)
b.down()
b.begin_fill()
b.color("black","black")
b.seth(158)
b.circle(80,90)
b.seth(100)
b.circle(-80,35)
b.seth(43)
b.circle(-80,44)
b.seth(-2)
b.ht()
b.circle(-50,60)
b.end_fill()

a=turtle.Turtle()
a.shapesize(1.5)
a.speed(0)
a.begin_fill()
a.color("#e48508","#e48508")
a.seth(90)
a.fd(320)
a.seth(0)
a.fd(320)
a.seth(-90)
a.fd(640)
a.seth(180)
a.fd(320)
a.seth(90)
a.fd(320)
a.end_fill()

a.bk(10)
a.begin_fill()
a.color("#f8bc74","#f8bc74")
a.seth(45)
a.circle(-35,36)
a.circle(-300,20)
a.seth(-120)
a.circle(50,115)
a.fd(30)
a.seth(-80)
a.circle(-30,63)
a.circle(-530,22)
a.end_fill()

a.up()
a.seth(90)
a.fd(125)
a.down()
a.begin_fill()
a.color("black","black")
a.circle(-30,64)
a.circle(55,34)
a.circle(7,99)
a.circle(75,29)
a.end_fill()

a.color("white")
a.begin_fill()
a.color("white","white")
a.up()
a.seth(-90)
a.fd(3)
a.down()
a.seth(-5)
a.fd(20)
a.circle(-4,160)
a.fd(23)
a.end_fill()

a.up()
a.seth(-90)
a.fd(70)
a.down()
a.begin_fill()
a.color("black","black")
a.seth(-17)
a.circle(160,54)
a.seth(-139)
a.circle(-160,30)
a.seth(-176)
a.circle(-160,25)
a.end_fill()