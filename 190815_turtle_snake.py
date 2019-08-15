import turtle
turtle.setup(650,350,200,200)#设置启动窗体的宽，高，起始点坐标的x，起始点坐标的y。setup并不是必须的。后两个参数不写，表明窗体在屏幕正中
turtle.penup()#画笔控制，抬起画笔，因此不会再画布上留下轨迹。可简写为turtle.pu
turtle.fd(-250)
turtle.pendown()#画笔控制，落下画笔，因此后面会在画布上留下轨迹.可简写文turtle.pd
turtle.pensize(25)#画笔粗细。也可以直接使用turtle.width()
turtle.pencolor("purple")#可以使用字符串或者r,g,b定义画笔颜色
turtle.seth(-40)#全称turtle.setheading,
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)#整数是255模式，小数是小数模式
turtle.fd(40*2/3)
turtle.done()
#以下为实例及解释
turtle.goto(10,10)#绝对坐标，代表以海龟为中心的x，y坐标
turtle.fd()#海龟坐标，海龟前进
turtle.bk()#海龟坐标，海龟后退
turtle.circle(r,angle)#海龟坐标，半径，角度。
turtle.circle(100)#绘制半径为100像素的原型
turtle.circle(-100,180)#绘制半径为100，逆时针❀半圆
turtle.seth(angle)#改变当前海龟的行进方向，并不行进，angle表示绝对角度
turtle.left(angle)#向左旋转角度
turtle.right(angle)#向右旋转角度
turtle.color()