"""
des: 使用turtle绘制tree
author: Mr_52Hz
date: 2020-06-11 2:04 PM
"""
import turtle

t = turtle.Turtle()


def draw_square():
    for i in range(4):
        t.forward(100)
        t.right(90)


def draw_tree(high):
    # high 树干的长度
    if high > 5:
        t.forward(high)
        t.right(20)
        draw_tree(high - 15)
        t.left(40)
        draw_tree(high - 15)
        t.right(20)
        t.backward(high)


if __name__ == '__main__':

    # 抬起画笔 将画笔移动到窗口合适位置
    t.penup()
    t.backward(50)
    t.right(90)
    t.forward(150)
    t.left(90)
    t.pendown()
    # 落笔 绘制正方形
    draw_square()

    # 移动画笔
    t.penup()
    t.forward(50)
    t.left(90)
    t.pendown()

    # 落笔绘制tree
    draw_tree(100)

    t.penup()
    t.backward(50)

    turtle.done()

