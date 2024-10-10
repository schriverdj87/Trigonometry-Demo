#Made by David Schriver - October 2024
import pygame
import CoreGame

pygame.init()

window = pygame.display.set_mode((CoreGame.arenaWidth,CoreGame.arenaHeight))
pygame.display.set_caption("Trigonometry Demo")

#Import images
pirateSize = (45,75)
pirate = pygame.transform.scale(pygame.image.load('assets/PirateA.png'),pirateSize)

ronaldSize = (88,100)
ronald = pygame.transform.scale(pygame.image.load('assets/RonaldMask.png'),ronaldSize)

donkeySize = (75,75)
donkey = pygame.transform.scale(pygame.image.load('assets/Straw Donkey.png'),donkeySize)

#This method catches whether or not the player has tried to exit the game
def isClosed():
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT: return True
    
    return False


while isClosed() == False:
    
    #Ensures the game runs at 30 fps. Comment this out to make the game go super fast.
    pygame.time.delay(33)
    
    #Clear window with every frame for re-drawing
    pygame.draw.rect(window,(30,30,30),(0,0,500,500))

    #Get the player input and feed it to the core game.
    input = pygame.key.get_pressed()

    if input[pygame.K_UP] == True: CoreGame.input_up()
    if input[pygame.K_DOWN] == True: CoreGame.input_down()
    if input[pygame.K_LEFT] == True: CoreGame.input_left()
    if input[pygame.K_RIGHT] == True: CoreGame.input_right()

    #This method updates the "CoreGame" at about 30 fps.
    CoreGame.crank()

    #Draw spinning circles
    for pt in CoreGame.circle1:
        pygame.draw.circle(window,(0,230,230),(pt.x,pt.y),CoreGame.radius/2)

    for pt in CoreGame.circle2:
        pygame.draw.circle(window,(0,230,170),(pt.x,pt.y),CoreGame.radius/2)

    for pt in CoreGame.circle3:
        pygame.draw.circle(window,(0,230,110),(pt.x,pt.y),CoreGame.radius/2)

    for pt in CoreGame.circle4:
        pygame.draw.circle(window,(0,230,50),(pt.x,pt.y),CoreGame.radius/2)

    for pt in CoreGame.circle5:
        pygame.draw.circle(window,(0,230,0),(pt.x,pt.y),CoreGame.radius/2)

    

    #Render Followers
    window.blit(ronald,(CoreGame.follower1.x - ronaldSize[0]/2,CoreGame.follower1.y - ronaldSize[1]/2))
    window.blit(donkey,(CoreGame.follower2.x - donkeySize[0]/2,CoreGame.follower2.y - donkeySize[1]/2))

    #Render Player
    window.blit(pirate,(CoreGame.player.x - pirateSize[0]/2,CoreGame.player.y - pirateSize[1]/2))    

    pygame.display.update()