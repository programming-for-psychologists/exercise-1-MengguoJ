import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square1 = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
deg = 0
square1.pos = (50,0)
square2 = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square2.pos = (-50,0)
square1.draw()
square2.draw()
win.flip()

while True:

    for i in range(60):

    #    win = visual.Window([400,400],color="black", units='pix')
        square1 = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
        deg = deg + 360/60
        square1.setOri(deg)
        square1.pos = (50,0)
        square1.draw()
        win.flip()
        core.wait(1/60)


        square2 = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
        deg = deg + 360/60
        square2.setOri(deg)
        square2.pos = (-50,0)
        square2.draw()
        win.flip()
        core.wait(1/60)

sys.exit()
