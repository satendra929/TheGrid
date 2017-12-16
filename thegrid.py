from graphics import *
from time import sleep

def main() :
    win= GraphWin("TheGrid", 500, 500)
    win.setBackground('black')
    startX=250
    startY=250
    grid=[50,100,150,200,250,300,350,400,450]
    pt= Point(startX,startY)
    cir=Circle(pt,5)
    cir.setFill('green')
    cir.draw(win)
    draw_grid(win)
    for t in range(250) :
        sleep(0.1)
        cir.move(1,0)
    win.getMouse()
    win.close()

def draw_grid(win) :
    l=Line(Point(50,500),Point(50,0))
    l.setFill('green')
    l.draw(win)
    l1=Line(Point(100,500),Point(100,0))
    l1.setFill('green')
    l1.draw(win)
    l2=Line(Point(150,500),Point(150,0))
    l2.setFill('green')
    l2.draw(win)
    l3=Line(Point(200,500),Point(200,0))
    l3.setFill('green')
    l3.draw(win)
    l4=Line(Point(250,500),Point(250,0))
    l4.setFill('green')
    l4.draw(win)
    l5=Line(Point(300,500),Point(300,0))
    l5.setFill('green')
    l5.draw(win)
    l6=Line(Point(350,500),Point(350,0))
    l6.setFill('green')
    l6.draw(win)
    l7=Line(Point(400,500),Point(400,0))
    l7.setFill('green')
    l7.draw(win)
    l8=Line(Point(450,500),Point(450,0))
    l8.setFill('green')
    l8.draw(win)
    lh=Line(Point(0,50),Point(500,50))
    lh.setFill('green')
    lh.draw(win)
    lh1=Line(Point(0,100),Point(500,100))
    lh1.setFill('green')
    lh1.draw(win)
    lh2=Line(Point(0,150),Point(500,150))
    lh2.setFill('green')
    lh2.draw(win)
    lh3=Line(Point(0,200),Point(500,200))
    lh3.setFill('green')
    lh3.draw(win)
    lh4=Line(Point(0,250),Point(500,250))
    lh4.setFill('green')
    lh4.draw(win)
    lh5=Line(Point(0,300),Point(500,300))
    lh5.setFill('green')
    lh5.draw(win)
    lh6=Line(Point(0,350),Point(500,350))
    lh6.setFill('green')
    lh6.draw(win)
    lh7=Line(Point(0,400),Point(500,400))
    lh7.setFill('green')
    lh7.draw(win)
    lh8=Line(Point(0,450),Point(500,450))
    lh8.setFill('green')
    lh8.draw(win)

def is_path(x,y,grid) :
    for c in grid :
        dxc = currPoint.x - point1.x
        dyc = currPoint.y - point1.y
        dxl = point2.x - point1.x
        dyl = point2.y - point1.y
        cross = dxc * dyl - dyc * dxl

        dxc = currPoint.x - point1.x
        dyc = currPoint.y - point1.y
        dxl = point2.x - point1.x
        dyl = point2.y - point1.y
        cross = dxc * dyl - dyc * dxl

main()
