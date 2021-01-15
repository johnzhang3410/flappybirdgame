#John Zhang
#Flappy Bird Game
#June 4, 2020

import turtle, pygame, time, sys
from pygame.locals import * 

pygame.init()
pygame.mixer.init()
#playbgm = 1
pygame.mixer.pre_init(44100,-16,2,2048)
sndHit = pygame.mixer.Sound('hit.wav')
sndFly = pygame.mixer.Sound('fly.wav')
snddie = pygame.mixer.Sound('die.wav')
sndpoint = pygame.mixer.Sound('point.wav')

pygame.mixer.music.load("bgm.wav")
pygame.mixer.music.play(1000, 0.0)

#Set up game screen
win = turtle.Screen()
win.register_shape("bird.gif")
win.title("Flappy Bird Game")
win.bgcolor("blue")
win.setup(width=500, height=600)
win.tracer(0)
win.bgpic("bg.gif")

#Display score
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("White")
pen.goto(0,250)
pen.write("0", move = False, align = "Left", font = ("Arial", 38, "normal"))

#Attributes of Player
player = turtle.Turtle()
player.penup()
player.color("yellow")
player.shape("bird.gif")
player.goto(-200,0) #Coordinates of player
#player.shapesize(stretch_wid = 3, stretch_len = 3, outline = None) #Resizes player, 60 * 60

#Pipe1 Top
pipetop = turtle.Turtle()
pipetop.penup()
pipetop.color("green")
pipetop.shape("square")
pipetop.goto(0,190)
pipetop.shapesize(stretch_wid = 11, stretch_len = 4, outline = None) #80, 220
pipetop.dx = -2
pipetop.dy = 0
pipetop.value = 1

#Pipe1 Bottom
pipeBottom = turtle.Turtle()
pipeBottom.penup()
pipeBottom.color("green")
pipeBottom.shape("square")
pipeBottom.goto(0,-190)
pipeBottom.shapesize(stretch_wid = 11, stretch_len = 4, outline = None)
pipeBottom.dx = -2
pipeBottom.dy = 0

#Pipe2 Top
pipe2top = turtle.Turtle()
pipe2top.penup()
pipe2top.color("green")
pipe2top.shape("square")
pipe2top.goto(300,190)
pipe2top.shapesize(stretch_wid = 18, stretch_len = 4, outline = None) #360, 80
pipe2top.dx = -2
pipe2top.dy = 0
pipe2top.value = 1

#Pipe2 Bottom
pipe2Bottom = turtle.Turtle()
pipe2Bottom.penup()
pipe2Bottom.color("green")
pipe2Bottom.shape("square")
pipe2Bottom.goto(300,-200)
pipe2Bottom.shapesize(stretch_wid = 9, stretch_len = 4, outline = None) #180, 80
pipe2Bottom.dx = -2
pipe2Bottom.dy = 0

#Speed changes for players
player.dx = 0 #dx is always positive, player doesn't go in x axis
player.dy = 1

score = 0

#print "Score: {}".format(score)
 
gravity = -0.1

#Function to change dy up
def up():
	player.dy += 4
	
	if player.dy > 4: #So it doesn't exceed speed limit
		player.dy = 4
		
	sndFly.play()
		
# def EndGame():
	# #Resets game
	# score = 0
	# pipetop.setx(0)
	# pipeBottom.setx(0)
	# pipe2top.setx(300)
	# pipe2Bottom.setx(300)
	# player.goto(-200,0)
	# player.dy = 0

#Bind Keys
win.listen()
win.onkey(up, "space") #Binds key "space" to function "up" (Moves player up)


#Main infinite Loop
while True:
	win.update() #Updates the Screen
	
	player.dy += gravity #Each loop adds on to the gravity
	
	#Movement of player
	y = player.ycor() #Player's original/Current coordinate
	y += player.dy #The change or the speed up and down
	player.sety(y) #Update y
	
	#Borders
	if player.ycor() < -280:
		player.dy = 0
		player.sety(-280)
		
	if player.ycor() > 285:
		player.dy = 0
		player.sety(285)

#Same as above, this time the movement of pipe1
	x = pipetop.xcor() #x so this move in x axis
	x += pipetop.dx #I set dx to be negative so they move left
	pipetop.setx(x)
	
	x = pipeBottom.xcor() #Same thing here
	x += pipeBottom.dx
	pipeBottom.setx(x)
	
	if pipetop.xcor() < -300: #Reset pipes
		pipetop.setx(300)
		pipeBottom.setx(300)
		pipetop.value = 1
		pipe2top.value = 1
	
	#Pipe2
	x = pipe2top.xcor() 
	x += pipe2top.dx 
	pipe2top.setx(x)
	
	x = pipe2Bottom.xcor() 
	x += pipe2Bottom.dx
	pipe2Bottom.setx(x)
	
	if pipe2top.xcor() < -300: 
		pipe2top.setx(300)
		pipe2Bottom.setx(300)
	
	#Collisions
	#X Collision
	# if (player.xcor() + 40 > pipetop.xcor() - 40) and (player.xcor() - 40 < pipetop.xcor() + 40):
		# print "xcollision" #I tested collisions here and tried to make numbers more accurate
	# else:
		# print "Nope"
		
		#First section is collision from right and after "and" is collision from left
	if (player.xcor() + 10 > pipetop.xcor() - 40) and (player.xcor() - 10 < pipetop.xcor() + 40): #Player is 60 by 60, so I used 30 which takes me to the edge of the image, and 40 for the pipes because I stretched its length 4 times and only 3 times for player
		if (player.ycor() + 10 > pipetop.ycor() - 110) or (player.ycor() - 10 < pipeBottom.ycor() + 110): # 110 is an estimation from me, checks ytop then ybottom
			sndHit.play()
			pen.clear()
			pen.penup()
			pen.write("Game Over", move = False, align = "center", font = ("Arial", 15, "normal"))
			snddie.play()
			win.update()
			time.sleep(5)
			#Resets game
			score = 0
			pipe2top.setx(300)
			pipe2Bottom.setx(300)
			pipetop.setx(0)
			pipeBottom.setx(0)
			player.goto(-200,0)
			player.dy = 0
			pen.clear()
			
	#Score sys
	if pipetop.xcor() + 40 < player.xcor() - 10:
			sndpoint.play()
			score = score + pipetop.value
			pipetop.value = 0
			pen.clear() #So score doesn't display over one another
			pen.write(score, move = False, align = "Left", font = ("Arial", 38, "normal"))
				
		#Pipe2
	if (player.xcor() + 10 > pipe2top.xcor() - 40 ) and (player.xcor() - 10 < pipe2top.xcor() + 40): 
		if (player.ycor() + 10 > pipe2top.ycor() - 180) or (player.ycor() - 10 < pipe2Bottom.ycor() + 90): # Again estimations
			sndHit.play()
			pen.clear()
			pen.penup()
			pen.write("Game Over", move = False, align = "center", font = ("Arial", 15, "normal"))
			snddie.play()
			win.update()
			time.sleep(3)
			#Resets game
			score = 0
			pipe2top.setx(300)
			pipe2Bottom.setx(300)
			pipetop.setx(0)
			pipeBottom.setx(0)
			player.goto(-200,0)
			player.dy = 0
			pen.clear()
			
	# Score sys
	if pipe2top.xcor() + 40 < player.xcor() - 10:
		sndpoint.play()
		score = score + pipe2top.value
		pipe2top.value = 0
		pen.clear()
		pen.write(score, move = False, align = "Left", font = ("Arial", 38, "normal"))
	
	time.sleep(0.02) #Not update too fast
	
turtle.mainloop()
