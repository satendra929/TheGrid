#from graphics import *
import pygame
from time import sleep
import math
import random
import copy
import threading
import time
time.clock()
from threading import Thread
from heapq import heappush, heappop

status=True

#pygame integration



crashed=False
clock=pygame.time.Clock()


def main() :
    global status
    global crashed
    pygame.init()
    dis=pygame.display.set_mode((500,500))
    pygame.display.set_caption('TheGrid')
    startX=450
    startY=100
    endX=50
    endY=400
    startX2=450
    startY2=450
    endX2=50
    endY2=50
    draw_grid(dis,True)
    path=find_path(startX,startY,endX,endY,dis)
    path2=find_path(startX2,startY2,endX2,endY2,dis)
    carImg=pygame.image.load('taxi.png')
    carImg=pygame.transform.scale(carImg,(20,20))
    carImg2=pygame.image.load('taxi.png')
    carImg2=pygame.transform.scale(carImg,(20,20))
    startp=pedestrians(dis)
    Thread(target=drive,args=(startX,startY,path,carImg,dis)).start()
    #Thread(target=drive,args=(startX2,startY2,path2,carImg2,dis)).start()
    Thread(target=move_pedestrians,args=(startp,dis)).start()
    crashed=False
    while crashed==False :
        for event in pygame.event.get() :
            if event.type==pygame.QUIT :
                crashed=True
                status=False
    pygame.quit()


def drive (startX,startY,path,carImg,dis) :
    cX=startX
    cY=startY
    ori=0
    for ind in range (len(path[0])) :
        px=path[0][ind]
        py=path[1][ind]
        draw_grid(dis,False)
        if cX-px != 0 :
            if cX-px==1 :
                carImg=pygame.image.load('taxiRight.png')
                carImg=pygame.transform.scale(carImg,(20,20))
            else :
                carImg=pygame.image.load('taxiLeft.png')
                carImg=pygame.transform.scale(carImg,(20,20))
        if cY-py != 0 :
            if cY-py==1 :
                carImg=pygame.image.load('taxiDown.png')
                carImg=pygame.transform.scale(carImg,(20,20))
            else :
                carImg=pygame.image.load('taxi.png')
                carImg=pygame.transform.scale(carImg,(20,20))
        cX=px
        cY=py
        ret=check_vic(px,py,px,py,dis,[])
        print ret[0]
        if ret[0]==True :
            sleep(2)
        dis.blit(carImg,(px-10,py-10))
        pygame.display.update()
        clock.tick(60)
        sleep(0.001)
    return

def move_pedestrians(startp,dis) :
    global status
    print startp
    while status==True :
        draw_grid(dis,False)
        for co in range(len(startp)) :
            positionsx=[startp[co][0]+1,startp[co][0]-1,startp[co][0]]
            positionsy=[startp[co][1]+1,startp[co][1]-1,startp[co][1]]
            ppx=positionsx[random.randint(0,2)]
            ppy=positionsy[random.randint(0,2)]
            pygame.draw.circle(dis,(255,255,255),(ppx,ppy),2)
            startp[co][0]=ppx
            startp[co][1]=ppy
        pygame.display.update()
        clock.tick(60)
        sleep(0.001)
    return True

def draw_grid(dis,ini) :
##    l=Line(Point(50,500),Point(50,0))
##    l.setFill('green')
##    l.draw(win)
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
    pygame.draw.circle(dis,(255,0,0),(450,100),5)
    pygame.draw.circle(dis,(0,255,0),(50,400),5)
    pygame.draw.circle(dis,(255,0,0),(450,450),5)
    pygame.draw.circle(dis,(0,255,0),(50,50),5)
    if ini==True :
        pygame.display.update()
        clock.tick(60)
        return
    else :
        return
    
    

def pedestrians(dis) :
    spoints=[]
    #epoints=[]
    cir_obj=[]
    for i in range(50) :
        spoints.append([random.randint(0,500),random.randint(0,500)])
        #epoints.append([random.randint(0,500),random.randint(0,500)])
    for j in spoints :
        pX=j[0]
        pY=j[1]
        pygame.draw.circle(dis,(255,255,255),(pX,pY),2)
    pygame.display.update()
##        ppt= Point(pX,pY)
##        pcir=Circle(ppt,2)
##        pcir.setFill('white')
##        pcir.draw(win)
##        cir_obj.append(pcir)
    return spoints
    

##def is_path(x,y,grid) :
##    for c in grid :
##        if x==c :
##            return True
##        elif y==c :
##            return True
##    return False

def check_vic(x,y,tx,ty,dis,checked) :
    surr=[(x+1,y),(x-1,y),(x+1,y+1),(x-1,y-1),(x,y+1),(x,y-1)]
    found=False
    while len(surr)!= 0 :
        tempx=surr[0][0]
        tempy=surr[0][1]
        if (tempx,tempy) not in checked :
            checked.append((tempx,tempy))
            if heuristic(tx,ty,tempx,tempy) <= 3 :
                val=dis.get_at((tempx,tempy))
                val=tuple(val[:3])
                print val
                if val!=(0,0,255) and val!=(0,0,0) and val!=(255,0,0) :
                    return (True,checked)
                else :
                    ret=check_vic(tempx,tempy,tx,ty,dis,checked)
                    found=ret[0]
                    checked=ret[1]
        del surr[0]
    return (found,checked)
            
def heuristic(x,y,endX,endY) :
    #print endX,endY
    a=math.fabs(x-endX)
    b=math.fabs(y-endY)
    return math.sqrt((a**2+b**2))

def successors(x,y,dis) :
    succ=[]
    if dis.get_at((x+1,y))!=(0,0,0) :
        succ.append((x+1,y))
    if dis.get_at((x,y+1))!=(0,0,0) :
        succ.append((x,y+1))
    if dis.get_at((x-1,y))!=(0,0,0) :
        succ.append((x-1,y))
    if dis.get_at((x,y-1))!=(0,0,0) :
        succ.append((x,y-1))
    return succ

def find_path(startX,startY,endX,endY,dis) :
    fringe=[]
    visited=[]
    cX=startX
    cY=startY
    pathx=[cX]
    pathy=[cY]
    visited.append((cX,cY))
    heu=heuristic(startX,startY,endX,endY)
    heappush(fringe,(heu,(startX,startY,pathx,pathy)))
    while fringe[0]!= IndexError :
        state=heappop(fringe)
        startX=state[1][0]
        startY=state[1][1]
        pX=state[1][2]
        pY=state[1][3]
        if startX==endX and startY==endY :
            return (pX,pY)
        for s in successors(startX,startY,dis) :
            tempX=s[0]
            tempY=s[1]
            temppX=copy.deepcopy(pX)
            temppY=copy.deepcopy(pY)
            if (tempX,tempY) not in visited :
                temppX.append(tempX)
                temppY.append(tempY)
                tempheu=heuristic(tempX,tempY,endX,endY)
                heappush(fringe,(tempheu,(tempX,tempY,temppX,temppY)))
                visited.append((tempX,tempY))

main()
