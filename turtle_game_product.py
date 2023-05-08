import turtle
from random import randint
import time

game_screen = turtle.Screen()
game_screen.bgcolor("#808080")
game_screen.title("TURTLE CLİCK GAME WİTH PYTHON")

t = turtle.Turtle()
t.penup()
t.shape("turtle")
t.shapesize(3, 3, 3)
t.speed(2)
t.fillcolor("red")

game_screen.listen()

score_list = []

score_turtle = turtle.Turtle()
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(-300, 120)
score = 0


def click_where(x=0, y=0):
    global score_list
    tx, ty = t.position()
    distance = ((x - tx) ** 2 + (y - ty) ** 2) ** 0.5
    if distance <= 55:
        score_list.append(1)
        score_turtle.clear()
        score_turtle.write(f"Score: {len(score_list)}", font=("Arial", 18, "bold"))

game_time = turtle.Turtle()
game_time.penup()
game_time.hideturtle()
game_time.goto(-300, 220)


for i in range(11):
    game_time.clear()
    game_time.write(f"time: {i}", font=("Arial", 20, "bold"))
    t.hideturtle()
    tx = randint(-305, 305)
    ty = randint(-305, 305)
    t.goto(tx, ty)
    t.showturtle()
    time.sleep(0.5)
    t.onclick(click_where)

t.hideturtle()

game_over = turtle.Turtle()
game_over.penup()
game_over.hideturtle()
game_over.goto(-250, 450)
score_turtle.write("GAME OVER", font=("Arial", 80, "bold"))

turtle.mainloop()

