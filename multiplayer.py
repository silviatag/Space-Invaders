#GROUP: Silvia Hassan, Sama Mohamed, Mohamed Ashraf, Hazem Ashraf

import turtle
import math
import random
import winsound

#Set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.bgpic("galaxybackground.gif")

#register the shapes
turtle.register_shape("enemy1.gif")
turtle.register_shape("First_Spaceship.gif")
turtle.register_shape("Second_Spaceship.gif")


#Draw border
border_pen = turtle.Turtle() 
border_pen.speed(0) # 0 is the fastest
border_pen.color("white")
border_pen.penup()  
border_pen.setposition(-300,-300)  
border_pen.pendown() 
border_pen.pensize(3) #3 pixels wide
for side in range(4):
	border_pen.fd(600) 
	border_pen.lt(90) 
border_pen.hideturtle()  

#assigning variables
score1 = 0
score2 = 0
enemies_num = 5
ispaused = False
keeplooping= True

#Draw the score of 1st player
scorepen1 = turtle.Turtle()
scorepen1.speed(0)
scorepen1.color("white")
scorepen1.penup()
scorepen1.setposition(208, 280) 
scorestring1 = "Score: {}".format(score1)
scorepen1.write(scorestring1, False, align="left", font=("Arial", 14, "normal"))
scorepen1.hideturtle()

#Draw the score of 2nd player
scorepen2 = turtle.Turtle()
scorepen2.speed(0)
scorepen2.color("white")
scorepen2.penup()
scorepen2.setposition(-290, 280)
scorestring2 = "Score: {}".format(score2) 
scorepen2.write(scorestring1, False, align="left", font=("Arial", 14, "normal"))
scorepen2.hideturtle()

#Create the player1 turtle
player1 = turtle.Turtle()
player1.color("blue")
player1.shape("First_Spaceship.gif")
player1.penup()
player1.speed(0) #calling the method
player1.setposition(215, -250)
player1.setheading(90) #rotates 90 degrees
player1.speed = 0 

#Create the player2 turtle
player2 = turtle.Turtle()
player2.color("blue")
player2.shape("Second_Spaceship.gif")
player2.penup()
player2.speed(0) #calling the method
player2.setposition(-215, -250)
player2.setheading(90) #rotates 90 degrees
player2.speed = 0 


#Create an empty list of enemies
enemies = []

#Add enemies to the list. To create multiple enemies
for i in range(enemies_num):
	#Create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("red")
	enemy.shape("enemy1.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200) #picks random number between -200 and 200
	y = random.randint(100, 250)
	enemy.setposition(x, y) 

enemyspeed = 2


#Create the player1's weapon
weapon1 = turtle.Turtle()
weapon1.color("yellow")
weapon1.shape("triangle")
weapon1.penup()
weapon1.speed(0)
weapon1.setheading(90) #rotates 90 degrees 
weapon1.shapesize(0.5, 0.5) #dimensions of weapon1
weapon1.hideturtle()
weapon1speed = 20

#Define weapon1 state
#ready - ready to fire
#fire - weapon1 is already firing (started moving)
weapon1state = "ready"


#Create the player2's weapon
weapon2 = turtle.Turtle()
weapon2.color("yellow")
weapon2.shape("triangle")
weapon2.penup()
weapon2.speed(0)
weapon2.setheading(90) #rotates 90 degrees 
weapon2.shapesize(0.5, 0.5) #dimensions of weapon2
weapon2.hideturtle()
weapon2speed = 20

#Define weapon2 state
#ready - ready to fire
#fire - weapon2 is already firing (started moving)
weapon2state = "ready"



#to play sounds
def playsound(sound_file, time = 0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)

#for pause option
def toggle_pause():
    global ispaused
    if ispaused== True:
        ispaused = False
    else:
        ispaused= True

#Move the player1 left and right
def move1_left(): #making a function to make the player1 move left
	player1.speed = -15
	
def move1_right(): #making a function to make the player1 move right
	player1.speed = 15

def move_player1():
	x = player1.xcor() 
	x += player1.speed 
	if x < -280:
		x = - 280 #to keep player1 inside the border
	if x > 280:
		x = 280
	player1.setx(x) 

#Move the player2 left and right
def move2_left(): #making a function to make the player2 move left
	player2.speed = -15
	
def move2_right(): #making a function to make the player2 move right
	player2.speed = 15

def move_player2():
	x = player2.xcor() 
	x += player2.speed 
	if x < -280:
		x = - 280 #to keep player2 inside the border
	if x > 280:
		x = 280
	player2.setx(x)

#firing weapon - 1st player
def fire_weapon1():
    #Declare weapon1state as a global 
    global weapon1state
    if weapon1state == "ready": #to control behavior of the weapon1
        weapon1state = "fire"
        #Move the weapon1 to the just above the player
        x = player1.xcor()
        y = player1.ycor() + 10
        playsound('laser.wav')
        weapon1.setposition(x, y)
        weapon1.showturtle()

#firing weapon - 2nd player
def fire_weapon2():
    #Declare weapon2state as a global 
    global weapon2state
    if weapon2state == "ready": #to control behavior of the weapon1
        weapon2state = "fire"
        #Move the weapon2 to the just above the player
        x = player2.xcor()
        y = player2.ycor() + 10
        playsound('laser.wav')
        weapon2.setposition(x, y)
        weapon2.showturtle()

#calculate a certain distance between 2 things where its considered collision
def isCollision(t1, t2): 
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2)) #pythagoras theory
	if distance < 23:
		return True #collision 
	else:
		return False  #no collision


#Create keyboard bindings

window.listen()
window.onkey(move1_left, "Left") 
window.onkey(move1_right, "Right") 
window.onkey(fire_weapon1, "space") 
window.onkey(move2_left, 'a') 
window.onkey(move2_right, 'd')
window.onkey(fire_weapon2, 's')
window.onkey(toggle_pause,'p')

#Main loop
while keeplooping:
    if not ispaused:
        move_player1()
        for enemy in enemies: #to loop over every enemy 
            #Move the enemy
            x = enemy.xcor() 
            x += enemyspeed 
            enemy.setx(x)

            #Move the enemy back and forth
            if enemy.xcor() > 280:
                #Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                #Change enemy direction
                enemyspeed *= -1
            
            if enemy.xcor() < -280:
                #Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                #Change enemy direction
                enemyspeed *= -1
                
            #Check for a collision between the weapon1 and the enemy
            if isCollision(weapon1, enemy):
                playsound('explosion.wav')
                #Reset the weapon1
                weapon1.hideturtle()
                weapon1state = "ready"
                weapon1.setposition(0, -400)
                #Reset the enemy
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setposition(x, y)
                #Update the score
                score1 += 10
                scorestring1 = "Score: {}".format(score1)
                scorepen1.clear()
                scorepen1.write(scorestring1, False, align="left", font=("Arial", 14, "normal"))
            
            #checks for collision between player1 and enemy
            if isCollision(player1, enemy):
                playsound('explosion.wav')
                player1.hideturtle()
                enemy.hideturtle()
                print ("Game Over")
                #ends main loop
                keeplooping = False
                break

            
        #Move weapon1
        if weapon1state == "fire":
            y = weapon1.ycor()
            y += weapon1speed
            weapon1.sety(y)
        
        #Check to see if weapon1 has gone to the top
        if weapon1.ycor() > 275:
            weapon1.hideturtle()
            weapon1state = "ready"



        move_player2()
        for enemy in enemies: #to loop over every enemy 
            #Move the enemy
            x = enemy.xcor() 
            x += enemyspeed 
            enemy.setx(x) 

            #Move the enemy back and forth
            if enemy.xcor() > 280:
                #Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y) 
                #Change enemy direction
                enemyspeed *= -1
            
            if enemy.xcor() < -280:
                #Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                #Change enemy direction
                enemyspeed *= -1
                
            #Check for a collision between the weapon2 and the enemy
            if isCollision(weapon2, enemy):
                playsound('explosion.wav')
                #Reset the weapon1
                weapon2.hideturtle()
                weapon2state = "ready"
                weapon2.setposition(0, -400)
                #Reset the enemy
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setposition(x, y)
                #Update the score
                score2 += 10
                scorestring2 = "Score: {}".format(score2)
                scorepen2.clear()
                scorepen2.write(scorestring2, False, align="left", font=("Arial", 14, "normal"))
            
            #checks for collision between player2 and enemy
            if isCollision(player2, enemy):
                playsound('explosion.wav')
                player2.hideturtle()
                enemy.hideturtle()
                print ("Game Over")
                #ends main loop
                keeplooping = False
                break

            
        #Move weapon2
        if weapon2state == "fire":
            y = weapon2.ycor()
            y += weapon2speed
            weapon2.sety(y)
        
        #Check to see if weapon2 has gone to the top
        if weapon2.ycor() > 275:
            weapon2.hideturtle()
            weapon2state = "ready"
        
        #checks for collision between the two players
        if isCollision(player1,player2):
            player1.hideturtle()
            player2.hideturtle()
            print("game over")
            #end main loop
            break

#setting the game over window
turtle. clearscreen()
border_pen.color("black")
border_pen.penup()
border_pen.goto(0,0)
border_pen.pendown()
border_pen.write("Game over", move=False, align= 'center', font=('Arial',80,'normal'))
leave= input("")