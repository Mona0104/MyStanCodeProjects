"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Build the breakout game's prototype and make the game rule function.--Mona Lai
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window_h = window_height
        self.window_w = window_width


        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle_set = paddle_offset
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)
        self.ball.filled = True
        self.ball_r = ball_radius
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.start_a_ball)
        onmousemoved(self.move_paddle)

        self.is_game_start = False

        # Draw bricks
        for i in range(0, brick_rows):
            # change the brick color
            color = ''
            if i // 2 == 0:
                color = 'lavenderblush'
            elif i // 2 == 1:
                color = 'lawngreen'
            elif i // 2 == 2:
                color = 'lemonchiffon'
            elif i // 2 == 3:
                color = 'lightblue'
            elif i // 2 == 4:
                color = 'lightcoral'

            for j in range(0, brick_cols):
                brick = GRect(width=brick_width, height=brick_height)
                brick.filled = True
                brick.fill_color = color
                brick.x = j * (brick_width + brick_spacing)
                brick.y = i * (brick_height + brick_spacing) + brick_offset
                self.window.add(brick)

    def move_paddle(self, event):
        self.paddle.x = event.x
        self.paddle.y = self.window_h - self.paddle_set
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif self.paddle.x >= self.window_w or self.paddle.x > self.window_w - self.paddle.width:
            self.paddle.x = self.window_w - self.paddle.width

    def set_ball_velocity(self):
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dy = -self.__dy

    def start_a_ball(self, event):
        if not self.is_game_start:
            self.set_ball_velocity()
            self.is_game_start = True

    def reset_a_ball(self):
        self.__dx = 0
        self.__dy = 0
        self.ball.x = (self.window_w - self.ball.width) / 2
        self.ball.y = (self.window_h - self.ball.height) / 2
        self.is_game_start = False

    def get_the_dx(self):
        return self.__dx

    def get_the_dy(self):
        return self.__dy

    def bound_dx(self):
        self.__dx = -self.__dx

    def bound_dy(self):
        self.__dx = -self.__dy

    def game_over(self):
        self.window.remove(self.ball)
        label = GLabel('Game over!', x=self.window_w/2, y=self.window_h/2)
        self.window.add(label)

