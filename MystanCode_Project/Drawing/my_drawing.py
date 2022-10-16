"""
File: my_drawing
Name:Mona
----------------------
Draw pokemon
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
        Please guess which pokemon I draw.
        """
    window = GWindow(width=800, height=600, title='my pokemon')
    circle1 = GOval(200, 200, x=100, y=100)
    circle1.filled = True
    circle1.fill_color = 'red'
    circle1.color = 'white'
    circle2 = GOval(200, 200, x=100, y=120)
    circle2.filled = True
    circle2.fill_color = 'white'
    window.add(circle1)
    window.add(circle2)
    mid = GRect(200, 25, x=100, y=200)
    mid.filled = True
    circle3 = GOval(175, 90, x=110, y=115)
    circle3.filled = True
    circle3.fill_color = 'red'
    circle3.color = 'red'
    circle4 = GOval(60, 60)
    circle4.filled = True
    circle4.fill_color = 'red'
    circle4.color = 'red'
    circle5 = GOval(60, 60)
    circle5.filled = True
    circle5.fill_color = 'red'
    circle5.color = 'red'
    window.add(circle3)
    window.add(circle5, x=238, y=160)
    window.add(circle4, x=102, y=160)
    window.add(mid)
    big_circle = GOval(90, 90, x=150, y=170)
    big_circle.filled = True
    sm_circle = GOval(70, 70, x=160, y=180)
    sm_circle.filled = True
    sm_circle.fill_color = 'gray'
    window.add(big_circle)
    window.add(sm_circle)
    r_foot = GOval(120, 60)
    r_foot.filled = True
    r_foot.fill_color = 'pink'
    l_foot = GOval(120, 60)
    l_foot.filled = True
    l_foot.fill_color = 'pink'
    window.add(l_foot, x=450, y=420)
    window.add(r_foot, x=600, y=420)
    face = GOval(250, 250, x=450, y=200)
    face.filled = True
    face.fill_color = 'pink'
    window.add(face)
    r_eye1 = GOval(100, 100)
    r_eye1.filled = 'True'
    r_eye1.fill_color = 'white'
    r_eye2 = GOval(90, 90)
    r_eye2.filled = 'True'
    r_eye2.fill_color = 'seagreen'
    r_eye3 = GOval(30, 30)
    r_eye3.filled = True
    r_eye3.fill_color = 'white'
    l_eye1 = GOval(100, 100)
    l_eye1.filled = 'True'
    l_eye1.fill_color = 'white'
    l_eye2 = GOval(90, 90)
    l_eye2.filled = 'True'
    l_eye2.fill_color = 'seagreen'
    l_eye3 = GOval(30, 30)
    l_eye3.filled = True
    l_eye3.fill_color = 'white'
    window.add(l_eye1, x=460, y=260)
    window.add(l_eye2, x=460, y=260)
    window.add(l_eye3, x=500, y=280)
    window.add(r_eye1, x=550, y=260)
    window.add(r_eye2, x=550, y=260)
    window.add(r_eye3, x=600, y=280)
    ph_head = GOval(60, 60)
    ph_head.filled = True
    ph_head.fill_color = 'gray'
    ph_body = GRect(60, 120)
    ph_body.filled = True
    ph_body.fill_color = 'gray'
    line = GArc(380, 360, 180, 70)
    window.add(ph_head, x=350, y=260)
    window.add(line, x=380, y=320)
    window.add(ph_body, x=350, y=300)
    card = GRect(350, 100)
    card.filled = True
    card.fill_color = 'darkblue'
    window.add(card, x=400, y=30)
    word = GLabel('??? Who am I??')
    word.font = '-40'
    word.color = 'yellow'
    window.add(word, x=410, y=100)


if __name__ == '__main__':
    main()
