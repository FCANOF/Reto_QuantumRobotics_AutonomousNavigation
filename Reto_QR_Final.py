# Reto Quantum Robotics
# Frida Cano Falcón
from random import randrange
from turtle import *
from freegames import vector, square
# or
import turtle
import random
import numpy as np
import math
import time


# Generacion de Coordenadas aleatorias
x = round(random.uniform(-249, 249),2)
y = round(random.uniform(-249, 249),2)

while(x==0 and y== 0): # Revisar si las coordenadas no son en las que ya se encuentra el rover
    x = round(random.uniform(-249, 249),2)
    y = round(random.uniform(-249, 249),2)

xRound = math.ceil(x)
cor = [x,y]
print("Coordenadas finales: ",cor)

# Variables principales
rX = 0
rY = 0
fX = 0

# Angulo del rover en funcion de la ubicacion en cuadrantes del punto final
if((x>0 and y>0) or (x>0 and y<0)): # I y IV cuadrante 
    ang = (math.atan(y/x))
    fX = 1
if((x<0 and y>0) or (x<0 and y<0)): # II y III cuadrante
    ang = (math.pi)+(math.atan(y/x))
    fX = -1
if(x==0 and y>0):
    ang = 90
if(x==0 and y<0):
    ang = -90
if(y==0 and x>0):
    ang = 0
if(y==0 and x<0):
    ang = 180

# Configuración de rover
rover = turtle.Turtle(shape='turtle')
rover.shapesize(1,1)
rover.setposition(rX,rY) # Posición inicial
rover.settiltangle(math.degrees(0)) # Dirección inicial

# Mapa
def world():
    """ Crear el plano
    """
    bgcolor('white')    # Color del fondo
    up()
    goto(cor)
    dot(5, 'red')       # Punto final

# Movimiento del rover
def move(begin):
    """Movimiento del rover
    """
    global rX, rY, x, y, xRound
    if(begin==1):
        #Actualizar angulo en dirección al punto final
        rover.settiltangle(math.degrees(ang))
        update()
        if(x>rX):
            mX = rX-x
            mY = rY-y
        else:
            mX = x-rX
            mY = y-rY
        while(rover.position()!=cor): #Trayectoria
            rX = (rX + fX)
            rY = ((mY/mX)*(rX)) # Trayectoria basada en la ecuación de línea recta
            rover.setposition(rX,rY)
            if(rX==xRound):
                rX = x
                rY = ((mY/mX)*(rX))
                rover.setposition(rX,rY)
                begin = 0
                print("Posicion del rover",rover.position(),math.degrees(ang), "grados")
                print("RECORRIDO TERMINADO")
                break
            time.sleep(0.25)
            print("Posicion del rover",rover.position(),math.degrees(ang), "grados")
            update()
    update()

# Configuración de la pantalla
setup(600,600)
hideturtle()
tracer(False)
title("Rover Autonomous Navigation")
world()
# Tecla que indica cuándo empezar el movimiento
listen()
onkey(lambda: move(1),'Left')
mainloop()