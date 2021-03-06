import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')

for i in range(3):
    square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
    square.draw()
    win.flip()
    core.wait(1) #pause for 500 ms (half a second)

    win.flip()
    core.wait(0.5)

    square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
    square.draw()
    win.flip()
    core.wait(1)

    win.flip()
    core.wait(0.5)

sys.exit()
