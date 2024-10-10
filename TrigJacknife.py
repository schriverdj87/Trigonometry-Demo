#Made by David Schriver - October 2024

import math

class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    #Measures the distance between this an another point
    def distanceTo(self,other):
        return math.sqrt(math.pow(self.x - other.x,2) + math.pow(self.y - other.y,2))
    
    #Adds the x and y of bythis to this point.
    def displace(self,bythis):
        self.x = self.x + bythis.x
        self.y = self.y + bythis.y

    #Gets angle between this and another point.
    def angleBetween (self,other):
        o = self.y - other.y
        a = self.x - other.x

        if a == 0: a = 0.00000000001 #This is needed because python will crap out if you try to divide by 0

        toSend = math.atan(o/a) #This gets the raw angle based on the difference in x and y of this point and the other point

        #Needs to be adjusted for proper use
        if (a > 0 or self.x == other.x):
            toSend = toSend + math.pi

        return toSend
    
    #Angle between, but returns in degrees instead of radians
    def degreesBetween (self,other):
        return self.angleBetween(other) * (180/math.pi)
    
    #Moves towards the other
    def chase (self,other,speed):
        toGo = shoot(self.angleBetween(other),speed)
        self.displace(toGo)
        return toGo
    
  


class Rectangle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    #Keep the point in the box
    def containPoint(self,point,radius):
        if (point.x < self.x + radius): point.x = self.x + radius
        if (point.y < self.y + radius): point.y = self.y + radius
        if (point.x > self.x + self.width - radius): point.x = self.x + self.width - radius
        if (point.y > self.y + self.height - radius): point.y = self.y + self.height - radius

#Converts an angle and speed to a point
def shoot (angle,speed):
    return Point(math.cos(angle) * speed, math.sin(angle) * speed)

#Returns the point of displacement to bring one point towards another
def chase (chaser, chasee, speed):
    toSend = shoot(chaser.angle(chasee),speed)
    return toSend
    
#Creates a "ring" of points as an array
#steps = How many points to go into the array
#startDistance and endDistance = Controls the radius of the ring. Make these different to make a spiral.
#angleoffset = Starting angle from the center to go off.
#locationOffset = Point that the ring is around.
def orbit (steps,startDistance,endDistance,angleoffset,locationoffset):
    angleStep = (math.pi*2)/steps #Difference in angle between points
    distStep = (startDistance - endDistance)/steps #Difference in distance from the center between each point
    toSend = []

    while len(toSend) < steps:
        toPut = shoot(angleoffset + (angleStep * len(toSend)),endDistance + (distStep * len(toSend)))
        toPut.displace(locationoffset)
        toSend.append(toPut)

    return toSend
    
