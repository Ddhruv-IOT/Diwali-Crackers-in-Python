# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 00:07:34 2021

@author: ACER
"""
import turtle
from turtle import color
import random
from pydub import AudioSegment
from pydub.playback import play
import threading as th
import time


turtle.bgcolor("black")
turtle.speed(0)
colors = ["red", "yellow", "blue", "pink", "orange", "cyan", "magenta", "gold"]

s = turtle.Screen()
t = turtle.Turtle()

s.setup(width = 1.0, height = 1.0)

#remove close,minimaze,maximaze buttons:
canvas = s.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

def pla():
    song = AudioSegment.from_mp3(r'C:\Users\ACER\Desktop\1.mp3')
    play(song)

def pen(colo):
    turtle.color(colo)


def fireworks(size):
    for num in range(20):
        turtle.forward(size)
        turtle.rt(180-(360/20))

def move():
    turtle.penup()
    x = random.randint(-660, 430)
    y = random.randint(-300, 130)
    turtle.goto(x, y)
    turtle.pendown()

def move_to(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_rectangle(a,b):
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.end_fill()
    t.speed(100)

def happy():
    t.color("red")
    move_to(-500,200)
    draw_rectangle(10,100)
    move_to(-490,250)
    t.left(90)
    draw_rectangle(80,10)
    move_to(-410,200)
    t.left(90)
    draw_rectangle(10,100)
    move_to(-380,200)
    t.left(60)
    t.color("yellow")
    draw_rectangle(10,122)
    move_to(-275,198)
    t.left(145)
    draw_rectangle(10,110)
    move_to(-350,230)
    t.left(335)
    draw_rectangle(10,63)
    move_to(-240,198)
    t.left(270)
    t.color("green")
    draw_rectangle(100,10)
    move_to(-240,288)
    draw_rectangle(50,10)
    move_to(-190,288)
    draw_rectangle(40,10)
    move_to(-190,248)
    draw_rectangle(50,10)
    move_to(-160,198)
    t.color("violet")
    draw_rectangle(100,10)
    move_to(-160,288)
    draw_rectangle(50,10)
    move_to(-110,288)
    draw_rectangle(40,10)
    move_to(-110,248)
    draw_rectangle(50,10)
    move_to(-80,198)
    t.left(320)
    t.color("orange")
    draw_rectangle(120,10)
    move_to(-100,295)
    draw_rectangle(68,10)
    move_to(-500,80)
    t.left(40)
    t.color("red")
    draw_rectangle(100,10)
    t.left(180)
    move_to(-490,70)
    draw_rectangle(50,10)
    t.left(90)
    t.fd(50)
    t.right(90)
    draw_rectangle(80,10)
    t.left(90)
    t.fd(80)
    t.left(270)
    draw_rectangle(50,10)
    move_to(-400,80)
    t.left(180)
    t.color("pink")
    draw_rectangle(100,10)
    move_to(-220,70)
    t.left(60)
    t.color("brown")
    draw_rectangle(100,10)
    t.left(300)
    move_to(-370,70)
    t.right(152)
    draw_rectangle(100,10)
    t.left(152)
    move_to(-290,10)
    t.right(45)
    draw_rectangle(40,10)
    t.right(3)
    draw_rectangle(40,10)
    move_to(-200,-15)
    t.left(200)
    t.color("green")
    draw_rectangle(10,110)
    move_to(-95,-20)
    t.left(145)
    draw_rectangle(10,114)
    move_to(-175,25)
    t.left(333)
    draw_rectangle(10,63)
    move_to(-70,79)
    t.left(90)
    t.color("blue")
    draw_rectangle(101,10)
    move_to(-60,-22)
    t.left(180)
    draw_rectangle(80,10)
    move_to(50,-22)
    t.left(180)
    t.color("Green")
    draw_rectangle(100,10)
    move_to(300,150)
    t.color("red")

def crac():
    angle=0
    for i in range(20):
        t.fd(50)
        move_to(300,150)
        angle+=18
        t.left(angle)

    for _ in range(70):
        colo = random.choice(colors)
        pen(colo)
        fireworks(random.randint(50, 100))
        move()

    turtle.done()


th.Thread(target=pla).start()
time.sleep(2)
happy()
crac()
