def veHinhChuNhat():
    import turtle
    t= turtle.Turtle()
    t.pensize(3)
    t.pencolor("pink")
    t.begin_fill()
    
    a = 100
    b = 50

    for i in range(2):
        t.forward(a)
        t.right(90)

        t.forward(b)
        t.right(90)
    t.end_fill()

    turtle.exitonclick()
if __name__ == "__main__":
    veHinhChuNhat()