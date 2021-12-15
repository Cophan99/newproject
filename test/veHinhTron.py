def hinhTron():
    import turtle
    import math
    r = int(input("Nhap ban kinh: "))
    t= turtle.Turtle()
    t.pensize(3)
    t.color("red")
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    c = 2 * math.pi * r
    s = math.pi * r * r
    print("Chu vi cua hinh tron ban kinh = {r} la {c}".format(r=r, c=c))
    print("Dien tich cua hinh tron ban kinh = {r} la {s}".format(r=r, s=s))

    turtle.exitonclick()
if __name__ == "__main__":
    hinhTron()
