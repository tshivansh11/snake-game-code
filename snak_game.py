 #importing libraries
import turtle
import random
import time


#creating turtle screen
screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width = 800, height = 700)
screen.tracer(0)
turtle.bgcolor('black')



##creating a border for our game

turtle.speed(0)
turtle.pensize()
turtle.penup()
turtle.goto(-300,300)
turtle.pendown()
turtle.color('white')
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.penup()
turtle.hideturtle()


turtle.penup()
turtle.hideturtle()

#score
score = 0
delay = 0.1
highest_score=0


#snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("azure",'turquoise')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'


#food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('azure','magenta')
fruit.penup()
fruit.goto(0,200)

old_fruit=[]

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.shape('square')
scoring.penup()
scoring.fillcolor('white')
scoring.hideturtle()
scoring.goto(-310,310)
scoring.write("                 Score: 0  |highest score: 0  ",align="center",font=("Courier",12,"bold"))

#######define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

#main loop

while True:
        screen.update()
            #snake and fruit coliisions
        if snake.distance(fruit)< 20:
                x = random.randint(-290,290)
                y = random.randint(-290,290)
                fruit.goto(x,y)
                scoring.clear()
                score+=10
                scoring.write("                 Score:{} | Highest Score".format(score,highest_score),align="center",font=("Courier",12,"bold"))
                delay-=0.001
                
                ## creating new_ball
                new_fruit = turtle.Turtle()
                new_fruit.speed(0)
                new_fruit.shape('circle')
                new_fruit.color("azure",'magenta')
                new_fruit.penup()
                old_fruit.append(new_fruit)
                
         
        #adding ball to snake
        
        for index in range(len(old_fruit)-1,0,-1):
                a = old_fruit[index-1].xcor()
                b = old_fruit[index-1].ycor()

                old_fruit[index].goto(a,b)
                                     
        if len(old_fruit)>0:
                a= snake.xcor()
                b = snake.ycor()
                old_fruit[0].goto(a,b)
        snake_move()

        ##snake and border collision    
        """
        if snake.xcor()>290 or snake.xcor()< -290 or snake.ycor()>290 or snake.ycor()<-290:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('turquoise')
                scoring.goto(0,0)
                scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
        """
        if snake.xcor()>290:
            snake.setx(-290)

        if snake.xcor()<-290:
            snake.setx(290)

        if snake.ycor()>290:
            snake.sety(-290)


        if snake.ycor()<-290:
            snake.sety(290)

        ## snake collision
        for food in old_fruit:
                if food.distance(snake) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('black')
                        scoring.goto(0,0)
                        scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",20,"bold"))
         

                
        time.sleep(delay)

turtle.Terminator()






