#GROUP: Silvia Hassan, Sama Mohamed, Mohamed Ashraf, Hazem Ashraf
import turtle
import math
import random
import subprocess
import winsound

#Set up the window screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.bgpic("galaxybackground.gif")

#register the shapes
turtle.register_shape("enemy1.gif")
turtle.register_shape("First_Spaceship.gif")
#turtle.register_shape("ban.gif")

#Draw border
border_pen = turtle.Turtle() #creating a pen
border_pen.speed(0) #0 is the fastest
border_pen.color("white")
border_pen.penup() 
border_pen.setposition(-300,-300)
border_pen.pendown() 
border_pen.pensize(3) 
for side in range(4):
	border_pen.fd(600) 
	border_pen.lt(90) 
border_pen.hideturtle() 	

#assigning variables
score = 0
level = 1
keeplooping= True
ispaused = False
enemies_num = 5

#Draw the score
scorepen = turtle.Turtle()
scorepen.speed(0)
scorepen.color("white")
scorepen.penup()
scorepen.setposition(-290, 280) 
scorestring = "Score: {}".format(score)
scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
scorepen.hideturtle()

#creating level pen
levelpen = turtle.Turtle()
levelpen.speed(0)
levelpen.color("white")
levelpen.penup()
levelpen.setposition(0, 300) 
levelstring = "Level: {}".format(level) 
levelpen.write(levelstring, False, align="center", font=("Arial", 14, "normal"))
levelpen.hideturtle()


#Create the shuttle turtle
shuttle = turtle.Turtle()
shuttle.color("blue")
shuttle.shape("First_Spaceship.gif")
shuttle.penup()
shuttle.speed(0) #calling the method
shuttle.setposition(0, -250)
shuttle.setheading(90) 
shuttle.speed = 0 



#creating an empty list of enemies
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


#Create the shuttle's weapon
weapon = turtle.Turtle()
weapon.color("yellow")
#weapon.shape("ban.gif")
weapon.penup()
weapon.speed(0)
weapon.setheading(90) #rotates 90 degrees 
weapon.shapesize(0.5, 0.5) #dimensions of the weapon
weapon.hideturtle()

weaponspeed = 20

#Define weapon state
#ready means ready to fire
#fire means weapon is already firing (started moving)
weaponstate = "ready"

#to play sound
def playsound(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)

#for pause option
def toggle_pause():
    global ispaused
    if ispaused== True:
        ispaused = False
    else:
        ispaused= True

#Move the shuttle left and right
def move_left(): #making a function to make the shuttle move left
	shuttle.speed = -15
	
def move_right(): #making a function to make the shuttle move right
	shuttle.speed = 15

def move_shuttle():
	x = shuttle.xcor()
	x += shuttle.speed 
	if x < -280:
		x = - 280 #to keep the shuttle inside the border
	if x > 280:
		x = 280
	shuttle.setx(x) 

#firing the bullets	
def fire_weapon():
    #Declare weaponstate as a global 
    global weaponstate
    if weaponstate == "ready": #to control behavior of the weapon
        weaponstate = "fire"
        #Move the weapon to the just above the shuttle
        x = shuttle.xcor()
        y = shuttle.ycor() + 10
        playsound('laser.wav')
        weapon.setposition(x, y)
        weapon.showturtle()

#calculates distance between things to see if they collided or not 
def isCollision(t1, t2): 
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2)) #pythagoras theory
	if distance < 23:
		return True #collision 
	else:
		return False  #no collision


#Create keyboard bindings
window.listen()
window.onkey(move_left, "Left") 
window.onkey(move_right, "Right") 
window.onkey(fire_weapon, "space") 
window.onkey(toggle_pause,'p') 


#Main loop
while keeplooping:
    if not ispaused:
        move_shuttle()
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
                
            #Check for a collision between the weapon and the enemy
            if isCollision(weapon, enemy):
                playsound('explosion.wav')
                #Reset the weapon
                weapon.hideturtle()
                weaponstate = "ready"
                weapon.setposition(0, -400)
                #Reset the enemy
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setposition(x, y)
                #Update the score
                score += 10
                scorestring = "Score: {}".format(score)
                scorepen.clear()
                scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            
            #check for collision between the shuttle and the enemy
            if isCollision(shuttle, enemy):
                playsound('explosion.wav')
                shuttle.hideturtle()
                enemy.hideturtle()
                print ("Game Over")
                #ends the main loop, player loses
                keeplooping = False
                break

            
        #Move the weapon
        if weaponstate == "fire":
            y = weapon.ycor()
            y += weaponspeed
            weapon.sety(y)
        
        #Check to see if the weapon has gone to the top
        if weapon.ycor() > 275:
            weapon.hideturtle()
            weaponstate = "ready"

        #checks score to move on to level 2
        if score == 30:
            subprocess.call(['python', 'level 2.py'])
            break


# Game over display screen
if keeplooping == False:
    border_pen.color("white")
    border_pen.penup()
    border_pen.goto(0,0)
    border_pen.pendown()
    border_pen.write("Game over", move=False, align= 'center', font=('Arial',80,'normal'))
    border_pen.penup()



leave= input("press enter to leave")

