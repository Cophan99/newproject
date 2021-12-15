from veNgoiSao import veNgoiSao


def veNgoiNha():
    import turtle
    t = turtle.Turtle()   
    t.pencolor("White")
    t.goto(80,90)

# Vẽ mặt trời 
    t.pensize(5)
    t.pencolor("yellow")
    t.begin_fill()
    t.fillcolor("yellow")

    t.circle(50)
    t.pencolor("White")
    t.home()
    t.pencolor("White")
    t.end_fill

# Vẽ cái cây
    
    t.pensize(3)
    t.pencolor("maroon")
    t.begin_fill()
    t.goto(90,-80)
    
    for i in range(5):
        t.forward(50)
        t.right(144)

    t.end_fill()
    turtle.exitonclick()
if __name__ == "__main__":
    veNgoiNha()

    


    