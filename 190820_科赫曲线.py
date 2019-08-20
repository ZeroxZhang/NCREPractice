#科赫曲线的绘制.py
import turtle
def keco(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            keco(size/3,n-1)

def main():
    turtle.setup(800, 400)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    keco(600, 5)  # 0阶科赫曲线长度，阶数
    turtle.hideturtle()
main()