from graphics import *
from time import sleep

def main() :
    win= GraphWin("TheGrid", 500, 500)
    win.setBackground('black')
    pt= Point(250,250)
    cir=Circle(pt,5)
    cir.setFill('green')
    cir.draw(win)
    for t in range(250) :
        sleep(0.1)
        cir.move(1,0)
    win.getMouse()
    win.close()



main()
