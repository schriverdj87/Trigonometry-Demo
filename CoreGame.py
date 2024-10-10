#Made by David Schriver - October 2024
import TrigJacknife
import math


arenaWidth = 500
arenaHeight = 500
radius = 20 #Programmical size of everything (player, NPCs, circles)
containingBox = TrigJacknife.Rectangle(0,0,500,500)
player = TrigJacknife.Point(250,250)
playerSpeed = 10

#Just follows the player
follower1 = TrigJacknife.Point(30,30)
follower1Speed = 3
follower1Space = 60 #How far away the follower1 will stop from the player

#Lunges at the player
follower2 = TrigJacknife.Point(arenaWidth - 30,30)
follower2Speed = 15
follower2Tickdown = [0,30]#x Ticks up to 30 and then it calculates lunge
follower2JumpDuration  = [0,5]# x is set to y and moves as it ticks down 
follower2JumpDirection = TrigJacknife.Point(0,0)#follower 2 displaces by this to lunge

#Arrays of points to simulate a ring of spinning circles
circle1 = []
circle2 = []
circle3 = []
circle4 = []
circle5 = []

circleAmt = 10
circleRadius = 250 #Base size of the ring of circles
circleAngle = 0 #Angle offsets so they spin
circle2Angle = 0
circleAngleStep = (math.pi * 2)/100 #How fast to spin

#What player input is pressed
UP = False
DOWN = False
LEFT = False
RIGHT = False

def input_up():
    global UP
    UP = True
    
def input_down():
    global DOWN
    DOWN = True

def input_left():
    global LEFT
    LEFT = True

def input_right():
    global RIGHT
    RIGHT = True



#This method should be updated 33 times per second
def crank():
    global UP
    global DOWN
    global LEFT
    global RIGHT
    global circle1
    global circle2
    global circle3
    global circle4
    global circle5
    global circleAngle
    global circle2Angle
    global follower2
    global follower2Tickdown
    global follower2JumpDirection
    global follower2JumpDuration
    global follower2Speed

    
    
    #Move the player
    toGo = TrigJacknife.Point(0,0)

    if UP == True:
        toGo.y = toGo.y - playerSpeed
        
    elif DOWN:
        toGo.y = toGo.y + playerSpeed

    if LEFT:
        toGo.x = toGo.x - playerSpeed
    elif RIGHT:
        toGo.x = toGo.x + playerSpeed

    if (toGo.x != 0 and toGo.y != 0):
        toGo.x = toGo.x * 0.7
        toGo.y = toGo.y * 0.7

    player.displace(toGo)
    #Keep player and Follower 2 in the arena
    containingBox.containPoint(player,radius)
    containingBox.containPoint(follower2,radius)
    
    #Move follower1
    if (player.distanceTo(follower1) > follower1Space):
        follower1.chase(player,follower1Speed)

    #Move follower 2
    if (follower2Tickdown[0] < follower2Tickdown[1] and follower2JumpDuration[0] == 0): #Charging jump
        follower2Tickdown[0] = follower2Tickdown[0] + 1
        if (follower2Tickdown[0] == follower2Tickdown[1]): #Time to jump
            follower2JumpDirection = TrigJacknife.shoot(follower2.angleBetween(player),follower2Speed)
            follower2Tickdown[0] = 0
            follower2JumpDuration[0] = follower2JumpDuration[1]

    if (follower2JumpDuration[0] > 0): #Jumping
        follower2JumpDuration[0] = follower2JumpDuration[0] - 1
        follower2.displace(follower2JumpDirection)
        if (follower2.distanceTo(player) < radius * 2): #Bounce off the player
            follower2JumpDirection.x = follower2JumpDirection.x * -1
            follower2JumpDirection.y = follower2JumpDirection.y * -1
            follower2.displace(TrigJacknife.shoot(player.angleBetween(follower2),radius * 2))#Initial bounce


    #Set up the spinning circles
    circleAngle = circleAngle + circleAngleStep
    if (circleAngle > (math.pi * 2)): circleAngle = circleAngle - (math.pi * 2)
    circle1 = TrigJacknife.orbit(circleAmt,circleRadius,circleRadius,circleAngle,TrigJacknife.Point(arenaWidth/2,arenaHeight/2))
    circle3 = TrigJacknife.orbit(circleAmt,circleRadius * 0.6,circleRadius * 0.6,circleAngle,TrigJacknife.Point(arenaWidth/2,arenaHeight/2))
    circle5 = TrigJacknife.orbit(circleAmt,circleRadius * 0.2,circleRadius * 0.2,circleAngle,TrigJacknife.Point(arenaWidth/2,arenaHeight/2))

    circle2Angle = circle2Angle - circleAngleStep
    circle2 = TrigJacknife.orbit(circleAmt,circleRadius * 0.8, circleRadius * 0.8, circle2Angle, TrigJacknife.Point(arenaWidth/2,arenaHeight/2))
    circle4 = TrigJacknife.orbit(circleAmt,circleRadius * 0.4, circleRadius * 0.4, circle2Angle, TrigJacknife.Point(arenaWidth/2,arenaHeight/2))
    if (circle2Angle < (math.pi * -2)): circle2Angle = 0

    UP = DOWN = LEFT = RIGHT = False

