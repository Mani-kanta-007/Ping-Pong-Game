import turtle 
wn=turtle.Screen()
wn.title("PING_PONG")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.goto(-350,0)
paddle_a.color("yellow")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5,stretch_len=1)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.goto(350,0)
paddle_b.color("yellow")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5,stretch_len=1)

#Pong
pong=turtle.Turtle()
pong.speed(0)
pong.shape("circle")
pong.goto(0,0)
pong.color("white")
pong.penup()
pong_dx=2
pong_dy=2
# pong.shapesize(stretch_wid=5,stretch_len=1)


#score
a,b=0,0

pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-10,260)
pen.hideturtle()
pen.color("red")
pen.write(" Player A: 0  Player B: 0",font=("center",26,"normal"))
 
 


# moment for paddle A
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

# moment for paddle B
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
    
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)



#keyboard Listener
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

while True:
    wn.update() #updating window each sec
    
    #pong Moment
    pong.setx(pong.xcor() + pong_dx)
    pong.sety(pong.ycor() + pong_dy)
    
    #pong moment with walls
    if pong.ycor()>290:
        pong.sety(290)
        pong_dy*=-1
    if pong.ycor()<-290:
        pong.sety(-290)
        pong_dy*=-1
        
    if pong.xcor()>390:
        a+=1
        pen.clear()
        pen.write(" Player A: {}  Player B: {}".format(a,b),font=("center",26,"bold"))
        pong.goto(0,0)
      
        #break;
        pong_dx*=-1
    if pong.xcor()<-390:
        pong.goto(0,0)
        b+=1
        pen.clear()
        pen.write(" Player A: {}  Player B: {}".format(a,b),font=("arial",26,"bold"))
        #break;
        pong_dx*=-1
        
    # ping and pong collision
    if pong.xcor()>340 and pong.xcor()<350 and (pong.ycor()<paddle_b.ycor()+50 and pong.ycor()>paddle_b.ycor()-50):
        pong.setx(340)
        pong_dx*=-1
    
    if pong.xcor()<-340 and pong.xcor()>-350 and (pong.ycor()<paddle_a.ycor()+50 and pong.ycor()>paddle_a.ycor()-50):
        pong.setx(-340)
        pong_dx*=-1
    
