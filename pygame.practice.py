import pygame
import sys
import random
import time
pygame.init()
dw=700
dh=550
screen=pygame.display.set_mode((dw,dh))
pygame.display.set_caption("new game")
clock=pygame.time.Clock()
black=(0,0,0)#rgb values for black
white=(255,255,255)#rgb values for white
rswidth=50 #rangership height
rsheight=75#rangership width
eswidth=50 #enemyship width
esheight=75 #enemyship width
r_ship=pygame.image.load('r_ship.png').convert()
r_ship=pygame.transform.scale(r_ship,(50,75))
r_ship.set_colorkey(black)
r_bullet=pygame.image.load('r_bullet1.png').convert()
r_bullet=pygame.transform.scale(r_bullet,(10,15))
e_ship=pygame.image.load('enemy_army.png').convert()
e_ship=pygame.transform.scale(e_ship,(50,75))
e_ship.set_colorkey(black)
e_bullet=pygame.image.load('e_bullet.png').convert()
e_bullet=pygame.transform.scale(e_bullet,(8,10))
blast=pygame.image.load('residue.png').convert()
blast=pygame.transform.scale(blast,(40,50))
blast.set_colorkey(black)
''' blit() fn is used for adding images to the screen'''
x=480 #initial pos for ranger ship x-axis
y=200 #initial pos of ranger ship y-axis
x_change=0 #initial value for changing positions of ranger ship.
y_change=0 #the same as above
b_x=0 #variable for moving the ranger ship's bullet along x-axis

'''ey,ey2,ey3,ey4 are y co-ordinates of the enemy ships'''
ey=random.randrange(0,100)
ey2=random.randrange(110,210)
ey3=random.randrange(230,360)
ey4=random.randrange(380,500)
'''ex,ex2,ex3,ex4 are x-cordinates of the enemy ships'''
ex=-10
ex2=0-random.randrange(0,100)# we took the values of ex,ex2,ex3,ex4 in a random,
#-ve number so that there would be time gap between appearance of each ship
ex3=0-random.randrange(0,120)
ex4=0-random.randrange(0,120)
es=1 #speed of enemyships
rbs=8 #bullet speed
rbx=0 #init position for rangership bullet
rby=0 #init pos for ranger bullet
count=0 #counting how many ships have been dodged
crashcount=0 #counting how many crashes have occured
xc=0
yc=0
evar=random.randrange(1,5) #making the enemy ships appear randomly from any of given five locations
def text_objects(text, font):
    textSurface = font.render(text,True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((dw/2),(dh/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
                    
    
def crash(xc,yc): #crash code
    message_display("you crashed")
    screen.blit(blast,(xc,yc)) #blitting blast image at the crash location
    pygame.display.update()
    time.sleep(1)
    
def rship(x,y): #making the rangership appear
    screen.blit(r_ship,(x,y))
def rbullet(x,y):
    while(x>0):
        screen.blit(r_bullet1,(x,y+40))
        x=x-2
def eship(ex,ey,es): #making the enemyship appear
    screen.blit(e_ship,(ex,ey))
    pygame.display.update()

def rbullet():
    screen.blit(r_bullet,(rbx,rby))
    rbx=x-n

def e_var(evar): #making the enemyships appear from any of the five parts of y-axis
    if(evar==1):
        eship(ex,random.randrange(0,100),es) #first part
    elif(evar==2):
        eship(ex,random.randrange(101,210),es)#second part
    elif(evar==3):
        eship(ex,random.randrange(211,320),es)#third part
    elif(evar==4):
        eship(ex,random.randrange(321,430),es)#fourth part
    elif(evar==5):
        eship(ex,random.randrange(431,525),es)#fifth part
    

def ships_dodged(count,crashcount): #record for the ships that have been dodged.
    font = pygame.font.SysFont(None, 40)
    text = font.render("Dodged: "+str(count), True,white)
    #counting total score
    text3= font.render("total score "+str((count-crashcount)*5), True,white)#at bottom
    text2= font.render("you crashed: "+str(crashcount), True,white)
    screen.blit(text,(450,0))
    screen.blit(text2,(430,20))
    screen.blit(text3,(430,520))

close=False
while not close: #main gameloop
    for event in pygame.event.get(): #listening events from the keyboard
        print(event)
        if event.type==pygame.QUIT: #matching the events when a key is pressed
            close= True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change=-1
            elif event.key == pygame.K_RIGHT:
                x_change=1
            elif event.key == pygame.K_UP:
                y_change = -1
            elif event.key == pygame.K_DOWN:
                y_change = 1
            elif event.key==pygame.K_SPACE:
                b_x=x
                b_y=y
                
        if event.type == pygame.KEYUP: #matching the events when the presed key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change =0 #we decided that the key up should do nothing
            
            
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
    x+=x_change #changing ranger ship pos
    y+=y_change
    screen.fill(black)#initial screen
    rship(x,y) #creating rangership
    eship(ex,ey,es)#creating enemyships
    eship(ex2,ey2,es)
    eship(ex3,ey3,es)
    eship(ex4,ey4,es)
    ships_dodged(count,crashcount)#checking the dodged ships
    ex+=1 #moving theenemy ships along the x-axis,but not along y
    ex2+=1
    ex3+=1
    ex4+=1
    if x >650: #creating the boundary for ranger ship, so that it may not go out of sight
        x=645
    elif x<0:
        x=0
    if y>470:
        y=465
    elif y<0:
        y=1
    '''if ex>dw: #if enemyship 1 crosses the entire screen, then let it appear again from the start of screen
        ex=0-5 #at -5 of x-axis
        ey=random.randrange(0,dh) '''

    if ex+eswidth > dw:#if enemyship 1 crosses the entire screen, then let it appear again from the start of screen
            ex= 0 - 10
            ey = random.randrange(0,100)
            count += 1
            es+=1
    if ex2+eswidth > dw:#reappearance of enemyship2
            ex2=0-random.randrange(0,150)
            ey2 = random.randrange(110,210)
            count += 1
            es+=1

    if ex3+eswidth > dw:#reappearance of enemyship3
            ex3=0-random.randrange(0,120)
            ey3= random.randrange(230,360)
            count+= 1
            es+=1

    if ex4+eswidth > dw:#reappearance of enemyship4
            ex4=0-random.randrange(0,150)
            ey4= random.randrange(380,500)
            count+= 1
            es+=1
            
    if x==ex+eswidth: #matching locations of enemyship and rangership
        print(x,"  ",ex," ",y)#so as to check for a crash and dodge
        if ey+esheight>y and ey+esheight<y+rsheight or ey>y and ey<y+rsheight:
            crash(x,y)
            crashcount+=1

    if x==ex2+eswidth:
        print(x,"  ",ex," ",y)
        if ey2+esheight>y and ey2+esheight<y+rsheight or ey2>y and ey2<y+rsheight:
            crash(x,y)
            crashcount+=1
    if x==ex3+eswidth:
        print(x,"  ",ex," ",y)
        if ey3+esheight>y and ey3+esheight<y+rsheight or ey3>y and ey3<y+rsheight:
            crash(x,y)
            crashcount+=1    
    if x==ex4+eswidth:
        print(x,"  ",ex," ",y)
        if ey4+esheight>y and ey4+esheight<y+rsheight or ey4>y and ey4<y+rsheight:
            crash(x,y)
            crashcount+=1
        '''i haven't updated the code for game over, but you can do it by modifying the crash() fn'''
    pygame.display.update()
    clock.tick(80)
pygame.quit()
sys.exit()
