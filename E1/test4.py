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
    core.wait(1)

    square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
    square.draw()
    win.flip()
    core.wait(1)

sys.exit()


"""
win =
square =

for i in ['blue', 'red']*3:
    square.setFillColor(i)
    square.draw()
    win.flip
    core.wait(1)
"""
