import pygame,random
from pygame import mixer

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)

pygame.init()

player1x=150
player1y=400

player2x=620
player2y=400

status='ready'

p1score = 0
p2score = 0

comic = pygame.font.SysFont('Comic Sans MS', 30)

bullx1=player1x
bully1=player1y
bullx2=player2x
bully2=player2y

isjump=False
isjump1=False

v=10
m=1

v1=10
m1=1

ec1x=[]
ec1y=[]
ec2x=[]
ec2y=[]
ec1img=[]
ec2img=[]
e_count1=2
e_count2=2

for _ in range (e_count1):
    ec1img.append(pygame.image.load('en.png'))
    ec1x.append(random.randint(100,125))
    ec1y.append(random.randint(250,400))

for _ in range (e_count2):
    ec2img.append(pygame.image.load('en.png'))
    ec2x.append(random.randint(700,800))
    ec2y.append(random.randint(280,390))

def drawscore():
    score = comic.render(str(p1score) + " - " + str(p2score), False, black)
    screen.blit(score, (470,70))
   
def show_enemies():
    global e_cont1,e_count2,ec1img,e_count2,ec1x,ec1y,ec2x,ec2y
    for i in range(e_count1):
       screen.blit(ec1img[i],(ec1x[i],ec1y[i]))    
    for j in range(e_count2):
       screen.blit(ec2img[j],(ec2x[j],ec2y[j]))

def fire1():
    global bullx1,bully1,status,player1x,player1y
    if status=="fire":
        return
    screen.blit(bullet,(bullx1,bully1))
    bullx1=player1x+100
    bully1=player1y
    status='fire'
    bullet_sound=mixer.Sound('laser.wav')
    bullet_sound.play()

def fire2():
    global bullx2,bully2,status,player2x,player2y
    if status=="fire":
        return
    screen.blit(bullet,(bullx2,bully2))
    bullx2=player2x-100
    bully2=player2y
    status='fire'
    bullet_sound=mixer.Sound('laser.wav')
    bullet_sound.play()


def check_and_fire_1():
    global bullx1,bully1,status
    if status=='ready':
        return
    screen.blit(bullet,(bullx1,bully1))
    bullx1+=50
    if bullx1<=250:
        status='ready'
    
def check_and_fire_2():
    global bullx2,bully2,status
    if status=='ready':
        return
    screen.blit(bullet,(bullx1,bully1))
    bullx2-=50
    if bullx2>=620:
        status='ready'

def check_collision():
    global bullx1,bully1,ec1x,ec1y,ec2x,ec2y,e_count1,e_count2
    for i in range(e_count1):
        xhit=False
        yhit=False
        if bullx1>=ec1x[i] and bullx1<=ec1y[i]+45:
            xhit=True
        if bully1>=ec1y[i] and bully1<=ec2y[i]+30:
            yhit=True
        if xhit and yhit:
            ec1img.pop(i)
            ecx1.pop(i)
            ecy1.pop(i)
            e_count1-=1
            status='ready'
            exp_music=mixer.Sound('explosion.wav')
            exp_music.play()
            return
size=(1000,600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption('DOODLE ARMY ZONE')

mixer.music.load('bg.wav')
mixer.music.play(-1)

bg=pygame.image.load('bg.jpg')
player_1=pygame.image.load('girl.png')
player_2=pygame.image.load('boy.png')
bullet=pygame.image.load('bull.png')
en=pygame.image.load('en.png')
en1=pygame.image.load('en.png')

run=True
while run:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                player2x+=10
            elif event.key==pygame.K_d:
                player1x+=10
            elif event.key==pygame.K_a:
                player1x-=10
            elif event.key==pygame.K_LEFT:
                player2x-=10
            elif event.key==pygame.K_RSHIFT:
                fire1()
            elif event.key==pygame.K_LSHIFT:
                fire2()
    keys=pygame.key.get_pressed()  
    if isjump==False or isjump1==False:
       if keys[pygame.K_w]:
           isjump=True
       elif keys[pygame.K_UP]:
           isjump1=True
    if isjump:
        f=(1/2)*m*(v**2)
        player1y-=f
        v=v-1
        if v<0:
           m=-1
        if v==-11:
           isjump=False
           v=10
           m=1
    elif isjump1:
        F=(1/2)*m1*(v1**2)
        player2y-=F
        v1=v1-1
        if v1<0:
           m1=-1
        if v1==-11:
           isjump1=False
           v1=10
           m1=1
    print(pygame.mouse.get_pos())
    screen.blit(player_1,[player1x,player1y])
    screen.blit(player_2,[player2x,player2y])
    show_enemies()
    fire1()
    fire2()
    check_and_fire_1()
    check_and_fire_2()
    drawscore()
    check_collision()
    pygame.display.update()
    
    
    #Team work done by
    #M.Sakthi Vihaas(XI)
    #K.Dharun Ram(XI)
