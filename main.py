from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0) # turn off the tracer

#create a snake using Snake class
my_snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen() # start listening to keys actions

#change direction of the snake
screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")



#Move the snake
game_on = True
while game_on:
    screen.update() #update the screen
    time.sleep(0.1) # delay refresh
    my_snake.move()

    #detect collision with food, using distance method of Turtle class
    if my_snake.head.distance(food) < 15:
        #food go random
        food.new_food()
        my_snake.extend()
        scoreboard.inscrease_score()

    # DETECT COLLISION WITH WALL
    if my_snake.head.xcor() < -290 or my_snake.head.xcor() > 290 or my_snake.head.ycor() < -290 or my_snake.head.ycor() > 290:
        game_on = False
        scoreboard.game_over()


    #DETECT COLLISION WITH TAIL, need test
    # if the head collides with any part of the snake body -> GAME OVER
    for segment in my_snake.segments[1:]: # check the body only
        if my_snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()










screen.exitonclick()