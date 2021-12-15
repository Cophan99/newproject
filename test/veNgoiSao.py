def veNgoiSao():
    import turtle
    t = turtle.Turtle()
    t.pensize(3)
    t.pencolor("pink")
    t.begin_fill()
    
    for i in range(5):
        t.forward(50)
        t.right(144)

    t.end_fill()

    turtle.exitonclick()
if __name__ == "__main__":
    veNgoiSao()