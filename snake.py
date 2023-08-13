from turtle import Turtle, Screen

# 3 segments with different cordinates
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# create classes
class Snake:
    def __init__(self):
        self.segments = [] # variable of the class
        self.create_snake() # function of the class
        self.head = self.segments[0]
    def create_snake(self):
        # Create a snakes
        for position in STARTING_POSITION:
            self.add_segment(position)


    def move(self):
        # move last segment(tail) to the body position, body to head
        for seg_num in range(len(self.segments) - 1, 0, -1):  # reverse order
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # move the head
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    #EXTEND THE LENGTH OF THE SNAKE
    def add_segment(self, position):
        new_segment = Turtle(shape="square")  # 20x 20 each square
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment) #use variable of the class


    def extend(self):
        #add a new segment
        # get hold of the position of the last segment
        #  position is the method of turtle
        self.add_segment(self.segments[-1].position())







