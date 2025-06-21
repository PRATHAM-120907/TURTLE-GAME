
from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
print(f"Your bet: {user_bet}")


all_turtles = []
for turtle_index in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[turtle_index])
    t.goto(-220, y_positions[turtle_index])
    all_turtles.append(t)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            
            if winning_color == user_bet:
                print(f"You won! The winning turtle is {winning_color}. 🏆")
            else:
                print(f"You lost. The winning turtle is {winning_color}. Better luck next time!")
       
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()





