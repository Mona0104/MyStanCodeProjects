"""
File: bouncing_ball
Name:Mona Lai
-------------------------
This program is an animation, show throw the ball process.
One people only can throw three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
is_ball_moving = False



def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global is_ball_moving
    ball.filled = True
    window.add(ball)
    vy = 0
    count = 0
    onmouseclicked(start)

    while True:
        if is_ball_moving and count < 3:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y + ball.height > window.height:
                if vy > 0:
                    vy *= -REDUCE
            if ball.x > window.width:
                vy = 0
                ball.x = START_X
                ball.y = START_Y
                is_ball_moving = False
                count += 1
        pause(DELAY)


def start(event):
    global is_ball_moving
    is_ball_moving = True



if __name__ == "__main__":
    main()
