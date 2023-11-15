import turtle
import time
import random

retraso = 0.1

marcador = 0
marcador_alto = 0

Pantalla = turtle.Screen()
Pantalla.setup(960,540)
Pantalla.bgcolor("black")
Pantalla.title("Culebrita")

Serpiente=turtle.Turtle()
Serpiente.speed(1)
Serpiente.shape("square")
Serpiente.penup()
Serpiente.home()
Serpiente.color("green","green")
Serpiente.direction = "stop"

Comida=turtle.Turtle()
Comida.shape("circle")
Comida.color("red")
Comida.penup()
Comida.goto(0,100)
Comida.speed(0)

Cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(-480,270)
texto.write("Marcador: 0\tMarcador más alto: 0",align="center", font=("verdana",24,"normal"))

def arriba():
    Serpiente.direction="up"

def abajo():
    Serpiente.direction="down"

def derecha():
    Serpiente.direction="right"

def izquierda():
    Serpiente.direction="left"

def movimiento():
    if Serpiente.direction == "up":
        y = Serpiente.ycor()
        Serpiente.sety(y+20)
    if Serpiente.direction == "down":
        y = Serpiente.ycor()
        Serpiente.sety(y-20)
    if Serpiente.direction == "right":
        x = Serpiente.xcor()
        Serpiente.setx(x+20)
    if Serpiente.direction == "left":
        x = Serpiente.xcor()
        Serpiente.setx(x-20)

Pantalla.listen()
Pantalla.onkeypress(arriba, "Up")
Pantalla.onkeypress(abajo, "Down")
Pantalla.onkeypress(derecha, "Right")
Pantalla.onkeypress(izquierda, "Left")

while True:
    Pantalla.update()

    if Serpiente.xcor() > 480 or Serpiente.xcor() < -480 or Serpiente.ycor() > 270 or Serpiente.ycor() < -270:
        time.sleep(1)
        for i in Cuerpo:
            i.clear()
            i.hideturtle()
        Serpiente.home()
        Serpiente.direction = "stop"
        Cuerpo.clear()

        texto.clear()
        marcador = 0
        texto.write("marcador: {}\tMarcador más alto: {}".format(marcador,marcador_alto),align="center",font=("verdana",24,"normal"))

    if Serpiente.distance(Comida) < 20:
        x = random.randint(-480,480)
        y = random.randint(-260,260)
        Comida.goto(x,y)

        nuevo_cuerpo=turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        Cuerpo.append(nuevo_cuerpo)
        
        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
        texto.write("marcador: {}\tMarcador más alto: {}".format(marcador,marcador_alto),align="center",font=("verdana",24,"normal"))

    total = len(Cuerpo)
    for index in range(total -1,0,-1):
        x = Cuerpo[index-1].xcor()
        y = Cuerpo[index-1].ycor()
        Cuerpo[index].goto(x,y)

    if total > 0:
        x = Serpiente.xcor()
        y = Serpiente.ycor()
        Cuerpo[0].goto(x,y)

    movimiento()

    for i in Cuerpo:
        if i.distance(Serpiente) < 20:
            for i in Cuerpo:
                i.clear()
                i.hideturtle()
            Serpiente.home()
            Cuerpo.clear()
            Serpiente.direction = "stop"

            texto.clear()
            marcador = 0
            texto.write("marcador: {}\tMarcador más alto: {}".format(marcador,marcador_alto),align="center",font=("verdana",24,"normal"))
            
            

    time.sleep(retraso)

turtle.done()