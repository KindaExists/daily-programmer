
"""
[intermediate] challenge #7

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pr265/2152012_challenge_7_intermediate/
"""

import turtle
from math import log2

t = turtle.Turtle()
length = 400
max_level = 2

def Sierpinski(s):
    if log2(200/s)+1 > max_level:   # I call this one the "what the function()"
        return
    t.forward(s)
    t.left(120)
    Sierpinski(s/2)
    t.forward(s)
    t.left(120)
    Sierpinski(s/2)
    t.forward(s)
    t.left(120)
    Sierpinski(s/2)

if __name__ == '__main__':
    Sierpinski(length)
    turtle.done()
