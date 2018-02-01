import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
deg = 0
square.setOri(deg)
square.draw()
win.flip()

while True :

    for i in range(60):

        square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
        deg = deg + 360/60
        square.setOri(deg)
        square.draw()
        win.flip()

    if event.getKeys(['s']):
        break

sys.exit()
