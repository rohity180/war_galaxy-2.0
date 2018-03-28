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
black=(0,0,0)
white=(255,255,255)
rswidth=50
rsheight=75
eswidth=50
esheight=75
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
gameover=pygame.image.load('enough.png').convert()
gameover=pygame.transform.scale(gameover,(700,550))
lifes=pygame.image.load('heart.png').convert()
lifes=pygame.transform.scale(lifes,(20,24))
emptylife=pygame.image.load('emptyheart.png').convert()
emptylife=pygame.transform.scale(emptylife,(20,24))
emptylife.set_colorkey(black)
x=600
y=200
x_change=0
y_change=0
b_x=0
ey=random.randrange(0,100)
ey2=random.randrange(110,210)
ey3=random.randrange(230,360)
ey4=random.randrange(380,500)
ex=-10
ex2=0-random.randrange(0,100)
ex3=0-random.randrange(0,120)
ex4=0-random.randrange(0,120)
es=1
rbs=8
rbx=0
rby=0
count=0
crashcount=0
xc=0
yc=0
evar=random.randrange(1,5)
def text_objects(text, font):
    textSurface = font.render(text,True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((dw/2),(dh/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def life(crashcount):
    if(crashcount==0):
        screen.blit(lifes,(600,300))
    
    
def crash(xc,yc):
    message_display("you crashed")
    screen.blit(blast,(xc,yc))
    pygame.display.update()
    time.sleep(1)
def rship(x,y):
    screen.blit(r_ship,(x,y))
def rbullet(x,y):
    while(x>0):
        screen.blit(r_bullet1,(x,y+40))
        x=x-2
def eship(ex,ey,es):
    screen.blit(e_ship,(ex,ey))
    pygame.display.update()

def rbullet():
    screen.blit(r_bullet,(rbx,rby))
    rbx=x-n

def e_var(evar):
    if(evar==1):
        eship(ex,random.randrange(0,100),es)
    elif(evar==2):
        eship(ex,random.randrange(101,210),es)
    elif(evar==3):
        eship(ex,random.randrange(211,320),es)
    elif(evar==4):
        eship(ex,random.randrange(321,430),es)
    elif(evar==5):
        eship(ex,random.randrange(431,525),es)
    

def ships_dodged(count,crashcount):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Dodged: "+str(count), True,white)
    text3= font.render("total score "+str((count-crashcount)*5), True,white)
    text2= font.render("you crashed: "+str(crashcount), True,white)
    screen.blit(text,(450,0))
    screen.blit(text2,(430,20))
    screen.blit(text3,(430,520))

def gameoverfn():
    font = pygame.font.SysFont(None, 100)
    gameovertxt=font.render("enough crashes!!!!",True,white)
    screen.blit(gameover,(0,0))
    pygame.display.flip()
    pygame.display.update()
    

close=False
while not close:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
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
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change =0
            
            
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0   
    x+=x_change
    y+=y_change
    screen.fill(black)
    rship(x,y)
    eship(ex,ey,es)
    eship(ex2,ey2,es)
    eship(ex3,ey3,es)
    eship(ex4,ey4,es)
    ships_dodged(count,crashcount)
    ex+=1
    ex2+=1
    ex3+=1
    ex4+=1
    if x >650:
        x=645
    elif x<0:
        x=0
    if y>470:
        y=465
    elif y<0:
        y=1
    if ex>dw:
        ex=0-5
        ey=random.randrange(0,dh)

    if ex+eswidth > dw:
            ex= 0 - 10
            ey = random.randrange(0,100)
            count += 1
            es+=1
    if ex2+eswidth > dw:
            ex2=0-random.randrange(0,150)
            ey2 = random.randrange(110,210)
            count += 1
            es+=1

    if ex3+eswidth > dw:
            ex3=0-random.randrange(0,120)
            ey3= random.randrange(230,360)
            count+= 1
            es+=1

    if ex4+eswidth > dw:
            ex4=0-random.randrange(0,150)
            ey4= random.randrange(380,500)
            count+= 1
            es+=1
            
    if x==ex+eswidth:
        print(x,"  ",ex," ",y)
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

    if crashcount==0:
        screen.blit(lifes,(410,20))
        screen.blit(lifes,(380,20))
        screen.blit(lifes,(350,20))
        pygame.display.update()
    if crashcount==1:
        screen.blit(emptylife,(410,20))
        screen.blit(lifes,(380,20))
        screen.blit(lifes,(350,20))
        pygame.display.update()
    if crashcount==2:
        screen.blit(emptylife,(410,20))
        screen.blit(emptylife,(380,20))
        screen.blit(lifes,(350,20))
        pygame.display.update()
    if crashcount==3:
        screen.blit(emptylife,(410,20))
        screen.blit(emptylife,(380,20))
        screen.blit(emptylife,(350,20))
        pygame.display.update()

    pygame.display.update()
    clock.tick(80)
    if(crashcount>=3):
        time.sleep(2)
        gameoverfn()
        time.sleep(2)
        pygame.quit()
pygame.quit()        
sys.exit()
quit()
