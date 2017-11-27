"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jiatong Zhang.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red',5)
red_turtle.speed = 15

size = 30

for k in range(10):
    red_turtle.draw_circle(size)

    red_turtle.pen_up()
    red_turtle.right(45)
    red_turtle.backward(15)
    red_turtle.left(45)
    red_turtle.pen_down()
    size = size - 1

green_turtle = rg.SimpleTurtle('turtle')
green_turtle.pen = rg.Pen('green',3)
green_turtle.speed = 10

for x in range(20):
    green_turtle.draw_regular_polygon(6,size)

    green_turtle.pen_up()
    green_turtle.right(45)
    green_turtle.forward(20)
    green_turtle.left(45)
    green_turtle.pen_down()
    size = size - 1

window.close_on_mouse_click()



