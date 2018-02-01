import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
deg = 0
square.setOri(deg)
square.draw()
win.flip()

x = 100
while True :

    for i in range(1):

        square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
        deg = deg + 0
        square.setOri(deg)
        square.size = [x,x]
        square.draw()
        win.flip()
        core.wait(1)


        if event.getKeys(['left']):

            while True:

                for i in range(1):

                    square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
                    x = 1.1*x
                    square.size = [x,x]
                    deg = deg + 0
                    square.setOri(deg)
                    square.draw()
                    win.flip()
                    core.wait(1)

                if not event.getKeys(['left']):
                    break

        if event.getKeys(['right']):

            while True:

                for i in range(1):

                    square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
                    x = x*0.9
                    square.size = [x,x]
                    deg = deg + 0
                    square.setOri(deg)
                    square.draw()
                    win.flip()
                    core.wait(1)

                if not event.getKeys(['right']):
                    break

sys.exit()
