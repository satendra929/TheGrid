import pygame

pygame.init()
dis=pygame.display.set_mode((500,500))
pygame.display.set_caption('TheGrid')
clock=pygame.time.Clock()

crashed=False

carImg=pygame.image.load('taxi.png')
carImg=pygame.transform.scale(carImg,(20,20))
rect=carImg.get_rect()
rect.center=(0,0)

def car(x,y) :
    dis.blit(carImg,(x,y))

def env() :
    dis.fill((0,0,0))
    pygame.draw.line(dis, (0, 0, 255), (50, 0), (50, 500),2)
    pygame.draw.line(dis, (0, 0, 255), (100, 0), (100, 500),2)
    pygame.draw.line(dis, (0, 0, 255), (150, 0), (150, 500),2)
    pygame.draw.line(dis, (0, 0, 255), (200, 0), (200, 500),2)
    pygame.draw.line(dis, (0, 0, 255), (250, 0), (250, 500),2)
    pygame.draw.line(dis, (0, 0, 255), (300, 0), (300, 500),2)
    pygame.draw.line(dis, (0, 0, 255), (350, 0), (350, 500),2)
    pygame.draw.line(dis, (0, 0, 255), (400, 0), (400, 500),2)
    pygame.draw.line(dis, (0, 0, 255), (450, 0), (450, 500),2)
    pygame.draw.line(dis, (0, 0, 255), (0,50), (500,50),2)
    pygame.draw.line(dis, (0, 0, 255), (0,100), (500,100),2)
    pygame.draw.line(dis, (0, 0, 255), (0,150), (500,150),2)
    pygame.draw.line(dis, (0, 0, 255), (0,200), (500,200),2)
    pygame.draw.line(dis, (0, 0, 255), (0,250), (500,250),2)
    pygame.draw.line(dis, (0, 0, 255), (0,300), (500,300),2)
    pygame.draw.line(dis, (0, 0, 255), (0,350), (500,350),2)
    pygame.draw.line(dis, (0, 0, 255), (0,400), (500,400),2)
    pygame.draw.line(dis, (0, 0, 255), (0,450), (500,450),2)
    pygame.draw.circle(dis,(255,0,0),(250,250),5)
    pygame.draw.circle(dis,(0,255,0),(250,50),5)
    pygame.display.update()

x=246
y=246
obs=False
count=0
while crashed==False :
    for event in pygame.event.get() :
        if event.type==pygame.QUIT :
            crashed=True
    count+=1
    if count==100 :
        carImg=pygame.transform.rotate(carImg,90)
    if obs==False :
        env()
        car(x,y)
        if count < 100 :
            y-=1
        else :
            x+=1
    if dis.get_at((x,y-1))== (0,255,0) :
        obs=True
    pygame.display.update()
    clock.tick(30)
pygame.quit()
