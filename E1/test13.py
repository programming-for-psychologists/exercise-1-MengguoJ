import time
import sys
from psychopy import visual,event,core
import math

win = visual.Window([400,400],color="black", units='pix')
Line1 = visual.Line(win,start=(-math.cos(54),-math.sin(54)), end=(0,1))
Line2 = visual.Line(win,start=(0, 1), end=(math.cos(54),-math.sin(54))

#Line3 = visual.Line(win,start=(math.cos(54),-math.sin(54)), end=(-math.cos(18), math.sin(18))

#Line4 = visual.Line(win,start=(-math.cos(18),math.sin(18)), end=(math.cos(18),math.sin(18))

#Line5 = visual.Line(win,start=(math.cos(18),math.sin(18)), end=(-math.cos(54),-math.sin(54))


Line1.draw()
Line2.draw()
#Line3.draw()
#Line4.draw()
#Line5.draw()

win.flip()
core.wait(.5) #pause for 500 ms (half a second)
sys.exit()
