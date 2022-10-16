"""
File: draw_line
Name:Mona Lai
-------------------------
This program use circle and mouse click times  could draw line.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 40
window = GWindow(width=800, height=1000)
circle = GOval(SIZE, SIZE)
circle.filled = True
circle.fill_color = 'white'
count = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    global count
    count += 1
    if count % 2 == 1:
        window.add(circle, x=event.x - SIZE // 2, y=event.y - SIZE //2)
    else:
        window.remove(circle)
        line = GLine(circle.x, circle.y, event.x, event.y)
        window.add(line)




if __name__ == "__main__":
    main()
