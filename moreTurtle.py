import turtle
t=turtle.Pen()
t.begin_fill()
t.circle(100)
t.end_fill()


f=turtle.pen()
f.color(1,0,0)
f.right(90)
t.begin_fill()
t.circle(200)
t.end_fill()

    
def rightEye():
    pensize(3)
    home()
    pd()
    pensize(3)
    color("black", "white")
    begin_fill()
    circle(80)
    end_fill()
    left(90)
    pu()
    fd(74)
    pd()
    pensize(4)
    circle(2)


rightEye()
