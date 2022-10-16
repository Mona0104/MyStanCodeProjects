"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is breakout game! You need to use paddle catch the ball and break all brick!
Everyone have three times live.--Mona Lai
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    live = NUM_LIVES
    graphics.is_game_start = False

    # Add the animation loop here!
    while True:
        # pause
        pause(FRAME_RATE)

        # update
        graphics.ball.move(graphics.get_the_dx(), graphics.get_the_dy())
        probe1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        probe2 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_r, graphics.ball.y)
        probe3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * graphics.ball_r)
        probe4 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_r,
                                               graphics.ball.y + 2 * graphics.ball_r)
        # check wall condition
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window_w:
            graphics.bound_dx()
        if graphics.ball.y <= 0:
            graphics.bound_dy()

        # check is None or brick or paddle
        if probe1 is not None:
            if probe1 is graphics.paddle:
                graphics.bound_dy()
            else:
                graphics.window.remove(probe1)
                graphics.set_ball_velocity()
        elif probe2 is not None:
            if probe2 is graphics.paddle:
                graphics.bound_dy()
            else:
                graphics.window.remove(probe2)
                graphics.set_ball_velocity()
        elif probe3 is not None:
            if probe3 is graphics.paddle:
                graphics.bound_dy()
            else:
                graphics.window.remove(probe3)
                graphics.set_ball_velocity()
        elif probe4 is not None:
            if probe4 is graphics.paddle:
                graphics.bound_dy()
            else:
                graphics.window.remove(probe4)
                graphics.set_ball_velocity()

        # check not get the ball
        if graphics.ball.y > graphics.window_h - graphics.paddle_set + graphics.ball_r:
            live -= 1
            if live > 0:
                graphics.reset_a_ball()
            else:
                graphics.game_over()
                break


if __name__ == '__main__':
    main()
