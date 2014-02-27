# sumloky
# (Edward) Sum Lok Yu
#--------------------

# Import a library of functions called 'pygame'
import pygame
import random
# Initialize the game engine
pygame.init()

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)

def drawTable():
    #base of rink
    pygame.draw.rect(screen, white,(25,25,450,650),0)
    
    #middle section
    pygame.draw.line(screen, red, [25,350],[475,350],5)
    pygame.draw.circle(screen, red, [250,350],50,5)
    pygame.draw.circle(screen, red, [250,350],10)
    
    #end of middle section
    pygame.draw.line(screen, blue, [25,250],[475,250],5)
    pygame.draw.line(screen, blue, [25,450],[475,450],5)
    
    #decorative circles
    for x in xrange(125,376,250):
        for y in xrange(175,526,350):
            pygame.draw.circle(screen, red, [x,y],50,5)
            pygame.draw.circle(screen, red, [x,y],10)
    #end lines        
    pygame.draw.line(screen, red, [25,50],[475,50],2)
    pygame.draw.line(screen, red, [25,650],[475,650],2)
    
    #rink frame   
    pygame.draw.rect(screen, black,(25,25,450,650),5)
    
    #thin frame
    #pygame.draw.rect(screen, black,(25,25,450,650),1)
    
puckStart_x = 250
puckStart_y = 350
    

class Puck(object):
    def __init__(self,x,y,dx=0,dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.puckStart_x = self.x
        self.puckStart_y = self.y
    def updatePuck(self):
        if self.x<=40:
            self.x = 42
            self.dx *= -1
        elif self.x>=460:
            self.x = 458
            self.dx *= -1
        if self.y<=30:
            self.y = 32
            self.dy *= -1 
        elif self.y>=670:
            self.y = 668
            self.dy *= -1
        self.x += self.dx
        self.y += self.dy
    def frictionOnPuck(self):
        if self.dx > 1:
            self.dx -= 1
        elif self.dx < -1:
            self.dx += 1
        if self.dy > 1:
            self.dy -= 1
        elif self.dy < -1:
            self.dy += 1
    def drawPuck(self):
        pygame.draw.circle(screen, black, [self.x,self.y],15,0)
        
    def limitPuckSpeed(self):
        if self.dx > 10:
            self.dx = 10
        if self.dx < -10:
            self.dx = -10
        if self.dy > 10:
            self.dy = 10
        if self.dy < -10:
            self.dy = 10
            
    def reset(self):
        self.x = self.puckStart_x
        self.y = self.puckStart_y
        self.dx = 0
        self.dy = 0
        

puck1 = Puck(puckStart_x,puckStart_y)


class Mallet(object):
    def __init__(self,malletType,x,y,uLim=50,bLim=650,lLim=50,rLim=450,dx=0,dy=0):
        self.x = x
        self.y = y
        self.last_x = self.x
        self.last_y = self.y
        
        self.malletType = malletType
        
        self.uLim = uLim
        self.bLim = bLim
        self.lLim = lLim
        self.rLim = rLim
                
        self.dx = dx
        self.dy = dy
        
        self.malletStart_x = self.x
        self.malletStart_y = self.y
        
    def updateMallet(self):
        if self.malletType != "MP":
            self.x += self.dx
            self.y += self.dy
            
        if self.x<self.lLim:
            #self.dx = 0
            self.x = self.lLim
        elif self.x>self.rLim:
            #self.dx = 0
            self.x = self.rLim
        
        if self.y<self.uLim:
            #self.dy = 0
            self.y = self.uLim
        elif self.y>self.bLim:
            #self.dy = 0
            self.y = self.bLim
        
    def drawMallet(self):
        pygame.draw.circle(screen, white, [self.x,self.y],20,0)
        pygame.draw.circle(screen, black, [self.x,self.y],20,1)
        pygame.draw.circle(screen, black, [self.x,self.y],5,0)
        
    def resetMallet(self):
        self.x = self.malletStart_x
        self.y = self.malletStart_y
    
upperMallet=Mallet("AI",250,100,50,330)
lowerMallet=Mallet("MP",250,600,370,650)


def malletAI(upperMallet):
    if puck1.x < upperMallet.x:
        if puck1.x < upperMallet.lLim:
            upperMallet.dx = 1
        else:
            upperMallet.dx = -2
    if puck1.x > upperMallet.x:
        if  puck1.x > upperMallet.rLim:
            upperMallet.dx = -1
        else:
            upperMallet.dx = 2
    if puck1.y < upperMallet.y:
        if puck1.y < upperMallet.uLim:
            upperMallet.dy = 1
        else:
            upperMallet.dy = -6
    if puck1.y > upperMallet.y:
        if puck1.y<=360: #was 250
            upperMallet.dy = 6
        #elif puck1.y<=350:
        #    upperMallet.dy = 2
        else:
            if upperMallet.y>200:
                upperMallet.dy = -2
            else:
                upperMallet.dy = 0
        if abs(puck1.y-upperMallet.y)< 20 and abs(puck1.x-upperMallet.x)< 20:
            puck1.dy +=2

class Goal(object):
    def __init__(self,x,y,w=100,h=20):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.centre_x = self.x + self.w/2
        self.centre_y = self.y + self.w/2
                
    def drawGoal(self):
        pygame.draw.rect(screen, green,(self.x,self.y,self.w,self.h),0)
       
upperGoal = Goal(200,10)
lowerGoal = Goal(200,670)


class UpperZone(object):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    
    def drawZone(self):
        pygame.draw.rect(screen,self.colour,(self.x,self.y,self.w,self.h),0)


ticksToFriction = 60
ticksToAI = 10

cpuScore = 0
playerScore = 0


# Set the width and height of the screen
size=[500,700]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("Air Hockey by Edward Yu")


done=False

clock=pygame.time.Clock()

print """

#################################################################
#                   A       IIIII    RRRRRRR                    #
#                  A A        I      R     R                    #
#                 A   A       I      RRRRRR                     #
#                AAAAAAA      I      R    R                     #
#               A       A   IIIII    R     R                    #
#                                                               #
#     H    H     OOO        CCC   K    KK   EEEEEE  YY     YY   #
#     H    H   OO   OO    CC      K KK      E         YY  YY    #
#     HHHHHH  O       O  C        K         EEEEEE      YY      #
#     H    H   OO   OO    CC      K KKK     E           YY      #
#     H    H     OOO        CCC   K    KK   EEEEEE      YY      #
#                                                               #
#                                  By: (Edward) Sum Lok Yu      #
#                                                               #
#################################################################

Games go up to 10.
Move your mouse to control your mallet (the lower one).
Click "R" to reset the game.

"""

  
# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        # User pressed down on a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and upperMallet.malletType == "KB":
                upperMallet.dx=-7
            if event.key == pygame.K_d and upperMallet.malletType == "KB":
                upperMallet.dx=7
            if event.key == pygame.K_w and upperMallet.malletType == "KB":
                upperMallet.dy=-7
            if event.key == pygame.K_s and upperMallet.malletType == "KB":
                upperMallet.dy=7

            if event.key == pygame.K_r:
                print "Game reset by user.."
                cpuScore = 0
                playerScore = 0
                puck1.reset()
                upperMallet.resetMallet()
                 
        # User let up on a key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and upperMallet.malletType == "KB":
                upperMallet.dx=0
            if event.key == pygame.K_d and upperMallet.malletType == "KB":
                upperMallet.dx=0
            if event.key == pygame.K_w and upperMallet.malletType == "KB":
                upperMallet.dy=0
            if event.key == pygame.K_s and upperMallet.malletType == "KB":
                upperMallet.dy=0
                
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  
  
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
    pos = pygame.mouse.get_pos()
    lowerMallet.x = pos[0]
    lowerMallet.y = pos[1]
    lowerMallet.updateMallet()
    
    lowerMallet.dx = lowerMallet.x-lowerMallet.last_x
    lowerMallet.dy = lowerMallet.y-lowerMallet.last_y
    while ticksToAI == 0:
        malletAI(upperMallet)
        ticksToAI = 10
    
            
    if (abs(upperMallet.x-puck1.x)<=35 and abs(upperMallet.y-puck1.y)<=35):
        puck1.dx = -1*puck1.dx + upperMallet.dx
        puck1.dy = -1*puck1.dy + upperMallet.dy
    
    if (abs(lowerMallet.x-puck1.x)<=35 and abs(lowerMallet.y-puck1.y)<=35):
        puck1.dx = -1*puck1.dx + lowerMallet.dx
        puck1.dy = -1*puck1.dy + lowerMallet.dy
    
    puck1.limitPuckSpeed()        
               
    if (abs(lowerGoal.centre_y-puck1.y)<=50 and abs(lowerGoal.centre_x-puck1.x)<=50):
        print "Computer Scores!"
        cpuScore += 1
        print "Player:", playerScore,"Computer:", cpuScore
        
        if cpuScore >= 10:
            print "\nComputer Wins! New Game about to begin..."
            playerScore = 0
            cpuScore = 0

        puck1.reset()
        upperMallet.resetMallet()
    
    #NEEED TO FIX NEW GAME SCORE
    if (abs(upperGoal.centre_y-puck1.y)<=5 and abs(upperGoal.centre_x-puck1.x)<=40):
        print "Player Scores!"
        playerScore += 1
        print "Player:", playerScore,"Computer:", cpuScore
        
        
        if playerScore >= 10:
            print "\nPlayer Wins! New Game about to begin..."
            playerScore = 0
            cpuScore = 0

        puck1.reset()
        upperMallet.resetMallet()

    
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
     
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(blue)
    drawTable()
    upperGoal.drawGoal()
    lowerGoal.drawGoal()
    
    puck1.drawPuck()
    
    upperMallet.drawMallet()
    lowerMallet.drawMallet()

    
    pygame.display.flip()
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    puck1.updatePuck()
    while ticksToFriction==0:
        puck1.frictionOnPuck()
        ticksToFriction = 60
    upperMallet.updateMallet()
    
    lowerMallet.last_x = lowerMallet.x
    lowerMallet.last_y = lowerMallet.y
    
    ticksToFriction -=1
    ticksToAI -= 1
    # frames per second
    clock.tick(60)  

pygame.quit ()
