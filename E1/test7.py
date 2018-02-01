import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
deg = 0
#square.setOri(deg)
#square.draw()
#win.flip()

while True:

    for i in range(60):

    #    win = visual.Window([400,400],color="black", units='pix')
        square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
        deg = deg + 360/60
        square.setOri(deg)
        square.draw()
        win.flip()
        core.wait(1/60)

    if event.getKeys(['q']):
        break

sys.exit()

"""
win =
sqaure =

increment = 6

while True:
    sqaure.draw()
    win.flip()
    sqaure.ori +=6 #rotate after draw and flip
    if even.getKeys(['g']):
        break

win.close()

sys.exit()
"""


#1. while True: those codes with this loop will be exectued/updated everytime of the looping. every looping means the time/process where all the codes within this loop has been ran through
