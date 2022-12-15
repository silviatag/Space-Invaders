import turtle
import math
import random
import winsound

#Set up the window screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.bgpic("galaxybackground.gif")

#register the shapes
turtle.register_shape("enemy1.gif")
turtle.register_shape("First_Spaceship.gif")
turtle.register_shape("Second_Spaceship.gif")

#Draw border
border_pen = turtle.Turtle() #creating a pen
border_pen.speed(0) #setting the speed of drawing, 0 is the fastest
border_pen.color("white")
border_pen.penup() #lifting the pen so that it doesnt  draw
border_pen.setposition(-300,-300) #because the center is (0,0) so it goes -300 left and then -300 down
border_pen.pendown() #puts the pen down so that it starts drawing
border_pen.pensize(3) #3 pixels wide
for side in range(4):
	border_pen.fd(600) #short for forward
	border_pen.lt(90) #90 degrees because we are drawing a square
border_pen.hideturtle() #to hide the pen when done	

#assigning variables
pcscore = 0
score = 0
ispaused = False
keeplooping= True


#Draw the score
pcscorepen = turtle.Turtle()
pcscorepen.speed(0)
pcscorepen.color("white")
pcscorepen.penup()
pcscorepen.setposition(-290, 280) #-290 to the left and 280 up
pcscorestring = "Score: %s" %score #the way it is going to be written
pcscorepen.write(pcscorestring, False, align="left", font=("Arial", 14, "normal"))
pcscorepen.hideturtle()



#Draw the score
scorepen = turtle.Turtle()
scorepen.speed(0)
scorepen.color("white")
scorepen.penup()
scorepen.setposition(290, 280) #-290 to the left and 280 up
scorestring = "Score: %s" %score #the way it is going to be written
scorepen.write(scorestring, False, align="right", font=("Arial", 14, "normal"))
scorepen.hideturtle()

#Create the shuttle turtle
shuttle = turtle.Turtle()
shuttle.color("blue")
shuttle.shape("First_Spaceship.gif")
shuttle.penup()
shuttle.speed(0)
shuttle.setposition(215, -250)
shuttle.setheading(90) #rotates 90 degrees

shuttlespeed = 15 #speed of the shuttle

#Create pc shuttle turtle
pcshuttle = turtle.Turtle()
pcshuttle.color("blue")
pcshuttle.shape("Second_Spaceship.gif")
pcshuttle.penup()
pcshuttle.speed(0)
pcshuttle.setposition(-215, -250)
pcshuttle.setheading(90) #rotates 90 degrees

pcshuttlespeed = 15 #speed of the shuttle


enemies_num = 5 #number of enemies
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
	y = random.randint(100, 250) #picks random number between 100 and 250
	enemy.setposition(x, y) #set the position of each enemy according to the numbers that were randomly picked

enemyspeed = 2


#Create the shuttle's weapon
weapon = turtle.Turtle()
weapon.color("yellow")
weapon.shape("triangle")
weapon.penup()
weapon.speed(0)
weapon.setheading(90) #rotates 90 degrees 
weapon.shapesize(0.5, 0.5) #dimensions of the weapon
weapon.hideturtle()

weaponspeed = 20

#Define weapon state
#ready - ready to fire
#fire - weapon is already firing (started moving)
weaponstate = "ready"


#Create pc shuttle's weapon
pcweapon = turtle.Turtle()
pcweapon.color("yellow")
pcweapon.shape("triangle")
pcweapon.penup()
pcweapon.speed(0)
pcweapon.setheading(90) #rotates 90 degrees 
pcweapon.shapesize(0.5, 0.5) #dimensions of the weapon
pcweapon.hideturtle()

pcweaponspeed = 20

#Define weapon state
#ready - ready to fire
#fire - weapon is already firing (started moving)
pcweaponstate = "ready"




def playsound(sound_file, time = 0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)

def toggle_pause():
    global ispaused
    if ispaused== True:
        ispaused = False
    else:
        ispaused= True
#Move the shuttle left and right

def move_down(): #making a function to make the shuttle move left
	y = shuttle.ycor() #to get the x coordinate
	y -= shuttlespeed #takes the current valu of x, subtracts the shuttle speed and assigns it to x
	if y < -250:
		y =  -250 #to keep the shuttle inside the border
	shuttle.sety(y) #changes the location to the new coordinates of x
	
	
def move_up(): #making a function to make the shuttle move right
	y = shuttle.ycor()
	y += shuttlespeed
	if y > -200:
		y = -200
	shuttle.sety(y)

def move_left(): #making a function to make the shuttle move left
	x = shuttle.xcor() #to get the x coordinate
	x -= shuttlespeed #takes the current valu of x, subtracts the shuttle speed and assigns it to x
	if x < -280:
		x = - 280 #to keep the shuttle inside the border
	shuttle.setx(x) #changes the location to the new coordinates of x
	
def move_right(): #making a function to make the shuttle move right
	x = shuttle.xcor()
	x += shuttlespeed
	if x > 280:
		x = 280
	shuttle.setx(x)
	
def fire_weapon():
	#Declare weaponstate as a global if it needs changed
	global weaponstate
	if weaponstate == "ready": #to control behavior of the weapon
		weaponstate = "fire"
		#Move the weapon to the just above the shuttle
		x = shuttle.xcor()
		y = shuttle.ycor() + 10
		playsound('laser.wav')
		weapon.setposition(x, y)
		weapon.showturtle()

def movepc_left(): #making a function to make the shuttle move left
	x = pcshuttle.xcor() #to get the x coordinate
	x -= pcshuttlespeed #takes the current valu of x, subtracts the shuttle speed and assigns it to x
	if x < -280:
		x = - 280 #to keep the shuttle inside the border
	pcshuttle.setx(x) #changes the location to the new coordinates of x
	
def movepc_right(): #making a function to make the shuttle move right
	x = pcshuttle.xcor()
	x += pcshuttlespeed
	if x > 280:
		x = 280
	pcshuttle.setx(x)
	
def fire_pcweapon():
	#Declare weaponstate as a global if it needs changed
	global pcweaponstate
	if pcweaponstate == "ready": #to control behavior of the weapon
		pcweaponstate = "fire"
		#Move the weapon to the just above the shuttle
		x = pcshuttle.xcor()
		y = pcshuttle.ycor() + 10
		playsound('laser.wav')
		pcweapon.setposition(x, y)
		pcweapon.showturtle()


def isCollision(t1, t2): #calculate a certain distance between shuttle and weapon where its considered collision
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2)) #pythagoras theory
	if distance < 23:
		return True #thats collision 
	else:
		return False  #no collision

def in_range(enemy):
		shooting_range = pcshuttle.xcor() - enemy.xcor()
		if shooting_range == -30:
			while shooting_range <= 0:
				movepc_right()
				shooting_range = pcshuttle.xcor() - enemy.xcor()
				if shooting_range == 0:
					fire_pcweapon()
					break
		if shooting_range == 30:
			while shooting_range >= 0:
				movepc_left()
				shooting_range = pcshuttle.xcor() - enemy.xcor()
				if shooting_range == 0:
					fire_pcweapon()
					break


window.listen()
window.onkey(move_left, "Left") #moving left is assigned to the left arrow key
window.onkey(move_right, "Right") #moving right is assigned to the right arrow key
window.onkey(fire_weapon, "space") #firing weapon is assigned to the space bar
window.onkey(move_down, "Down")
window.onkey(move_up, "Up")
window.onkey(toggle_pause,'p')


#Main game loop for the game to keep going
while keeplooping:
	if not ispaused:
		for enemy in enemies: #to loop over every enemy 
			in_range(enemy)
			#Move the enemy
			x = enemy.xcor() #current x coordinate of enemy
			x += enemyspeed 
			enemy.setx(x) #change enemy's posistion to new coordinates of x

			#Move the enemy back and forth
			if enemy.xcor() > 280:
				#Move all enemies down
				for e in enemies:
					y = e.ycor()
					y -= 40
					e.sety(y) #change enemy's postion to new coordinate of y
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

			# in_range(enemy)
				
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
				scorestring = "Score: %s" %(score)
				scorepen.clear()
				scorepen.write(scorestring, False, align="right", font=("Arial", 14, "normal"))

			if isCollision(pcweapon, enemy):
				playsound('explosion.wav')
				weapon.hideturtle()
				pcweaponstate = "ready"
				pcweapon.setposition(0, -400)
				x = random.randint(-200, 200)
				y = random.randint(100, 250)
				enemy.setposition(x,y)
				pcscore += 10
				pcscorestring = "Score %s" %(pcscore)
				pcscorepen.clear()
				pcscorepen.write(pcscorestring, False, align='left', font=('Arial', 14, "normal"))
			
			if isCollision(shuttle, enemy):
				playsound('explosion.wav')
				shuttle.hideturtle()
				enemy.hideturtle()
				print ("Game Over")
				keeplooping = False
				break

			if isCollision(shuttle, pcshuttle):
				playsound('explosion.wav')
				shuttle.hideturtle()
				pcshuttle.hideturtle()
				print("game over")
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

		if pcweaponstate == "fire":
			y = pcweapon.ycor()
			y += pcweaponspeed
			pcweapon.sety(y)

		if pcweapon.ycor() >275:
			pcweapon.hideturtle()
			pcweaponstate = "ready"

turtle. clearscreen()
border_pen.color("black")
border_pen.penup()
border_pen.goto(0,0)
border_pen.pendown()
border_pen.write("Game over", move=False, align= 'center', font=('Arial',80,'normal'))
leave= input("")