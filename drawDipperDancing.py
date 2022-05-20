from turtle import *
from math import *

speed(0)


def go(tup):
    goto(tup[0], tup[1])


def mark():
    dot(4, "black")


def changePenColor():
    pencolor('red')


def calculateAngle(tup1, tup2):
    dy = tup2[1] - tup1[1]
    dx = tup2[0] - tup1[0]
    angle = atan(abs(dy / dx))
    return angle / pi * 180


def drawDipperDancing(x):
    SKIN_COLOR = '#e8d6ba'
    HAIR_COLOR = '#645032'
    COSTUME_COLOR = '#f1fffa'
    COSTUME_SHADE_COLOR = '#98ccbb'
    EYE_COLOR = '#fefffe'
    IRIS_COLOR = '#040404'
    NOSE_COLOR = '#dcc2a1'
    MOUTH_COLOR = '#633852'
    TEETH_COLOR = '#efeaf1'
    TONGUE_COLOR = '#c4767d'
    CHEEK_COLOR = '#e5a4b1'
    EYEBROW_COLOR = 'black'
    BOW_COLOR = '#e17a98'
    GLOVE_COLOR = '#51746d'

    # draw the head
    fillcolor(SKIN_COLOR)
    begin_fill()
    startFace = pos()
    seth(351)
    circle(1.2 * x, 55)
    rt(5)
    circle(-1.45 * x, 43)
    endHair = pos()
    rt(16)
    circle(-2 * x, 68)
    lt(4)
    circle(-3 * x, 60)
    startBow1 = pos()
    rt(45)
    circle(1.9 * x, 48)
    rt(100)
    startBow2 = pos()
    circle(0.4 * x, 98)
    rt(105)
    circle(1.2 * x, 43)
    seth(138)
    circle(-1.6 * x, 94)
    rt(8)
    circle(1.15 * x, 69)
    end_fill()

    # draw eyes
    # right eye
    pu()
    go(startFace)
    seth(296)
    fd(1.7 * x)
    seth(0)
    pd()
    fillcolor(EYE_COLOR)
    begin_fill()
    pu()
    circle(0.75 * x, 43)
    pd()
    circle(0.75 * x, 255)
    pu()
    circle(0.75 * x, 62)
    end_fill()

    pu()
    circle(0.75 * x, 43)
    lt(82)
    fillcolor(SKIN_COLOR)
    begin_fill()
    pd()
    circle(0.85 * x, 90)
    lt(82)
    circle(0.75 * x, 105)
    end_fill()

    pu()
    go(startFace)
    seth(322)
    fd(1 * x)
    seth(0)
    pd()
    fillcolor(IRIS_COLOR)
    begin_fill()
    circle(0.1 * x)
    end_fill()

    # left eye
    pu()
    go(startFace)
    seth(318)
    fd(2.8 * x)
    seth(0)
    pd()
    fillcolor(EYE_COLOR)
    begin_fill()
    circle(0.75 * x)
    end_fill()

    pu()
    circle(0.75 * x, 43)
    lt(82)
    fillcolor(SKIN_COLOR)
    begin_fill()
    pd()
    circle(0.85 * x, 90)
    lt(82)
    circle(0.75 * x, 110)
    end_fill()

    pu()
    go(startFace)
    seth(335)
    fd(2.3 * x)
    seth(0)
    pd()
    fillcolor(IRIS_COLOR)
    begin_fill()
    circle(0.1 * x)
    end_fill()

    # draw nose
    pu()
    go(startFace)
    seth(296)
    fd(1.8 * x)
    seth(315)
    fillcolor(NOSE_COLOR)
    begin_fill()
    for i in range(2):
        pd()
        circle(0.35 * x, 90)
        if i == 0:
            pu()
        circle(0.35 * x / 2, 90)
    end_fill()

    # draw mouth
    pu()
    go(startFace)
    seth(277)
    fd(2.1 * x)
    seth(337)
    startMouth = pos()
    fillcolor(MOUTH_COLOR)
    begin_fill()
    pd()
    circle(2.6 * x, 45)
    rt(50)
    circle(-0.7 * x, 111)
    lt(4)
    circle(-1.55 * x, 86)
    circle(-0.95 * x, 60)
    circle(-0.45 * x, 60)
    end_fill()

    # draw teeth
    pu()
    go(startMouth)
    seth(337)
    fillcolor(TEETH_COLOR)
    begin_fill()
    pd()
    circle(2.6 * x, 45)
    seth(270)
    fd(0.25 * x)
    rt(62)
    circle(-2.2 * x, 54)
    go(startMouth)
    end_fill()

    # draw tongue
    pu()
    go(startMouth)
    seth(337)
    circle(2.6 * x, 45)
    rt(50)
    circle(-0.7 * x, 111)
    lt(4)
    circle(-1.55 * x, 13)
    fillcolor(TONGUE_COLOR)
    begin_fill()
    pd()
    circle(-1.55 * x, 40)
    rt(90)
    circle(-0.58 * x, 142)
    end_fill()

    # draw cheeks
    pu()
    go(startFace)
    seth(265)
    fd(2 * x)
    seth(0)
    fillcolor(CHEEK_COLOR)
    begin_fill()
    circle(0.3 * x)
    end_fill()

    pu()
    go(startBow1)
    seth(58)
    fd(1.8 * x)
    begin_fill()
    circle(0.3 * x)
    end_fill()

    # draw eyebrow
    pu()
    go(startFace)
    seth(4)
    fd(2.1 * x)
    seth(62)
    fillcolor(EYEBROW_COLOR)
    begin_fill()
    pd()
    circle(-0.35 * x, 160)
    seth(95)
    circle(0.36 * x, 133)
    end_fill()

    # draw hair
    pu()
    go(startFace)
    seth(145)
    fillcolor(HAIR_COLOR)
    begin_fill()
    pd()
    circle(-0.55 * x, 135)
    lt(122)
    circle(0.25 * x, 73)
    rt(8)
    circle(-0.18 * x, 180)
    lt(26)
    circle(-1 * x, 78)
    lt(180)
    circle(-0.75 * x, 35)
    rt(40)
    circle(-0.2 * x, 115)
    lt(5)
    circle(-0.8 * x, 34)
    lt(5)
    circle(1.66 * x, 37)
    go(endHair)
    seth(178)
    circle(1.45 * x, 43)
    lt(5)
    circle(-1.2 * x, 55)
    end_fill()

    # draw the head of the costume
    fillcolor(COSTUME_COLOR)
    begin_fill()
    seth(145)
    circle(-0.55 * x, 55)
    lt(108)
    circle(0.35 * x, 42)
    lt(4)
    circle(-2.5 * x, 48)
    lt(154)
    startShadeCostume = pos()
    circle(-0.75 * x, 58)
    circle(0.54 * x, 78)
    lt(58)
    circle(-1.6 * x, 25)
    rt(8)
    circle(1.15 * x, 69)
    go(startFace)
    end_fill()

    pu()
    go(startFace)
    pd()
    seth(145)
    circle(-0.55 * x, 42)
    lt(137)
    circle(1.7 * x, 51)

    pu()
    go(startShadeCostume)
    seth(350)
    fillcolor(COSTUME_SHADE_COLOR)
    begin_fill()
    pd()
    circle(-0.75 * x, 58)
    circle(0.54 * x, 78)
    lt(58)
    circle(-1.6 * x, -12)
    lt(112)
    circle(-1.1 * x, 76)
    lt(12)
    circle(-0.34 * x, 107)
    go(startShadeCostume)
    end_fill()

    pu()
    go(endHair)
    seth(342)
    pd()
    fillcolor(COSTUME_COLOR)
    begin_fill()
    circle(-2 * x, 68)
    lt(4)
    circle(-3 * x, 60)
    seth(346)
    circle(-0.75 * x, 49)
    lt(80)
    circle(2.6 * x, 49)
    lt(54)
    circle(-2.4 * x, 40)
    circle(-2.4 * x, -67)
    lt(160)
    circle(0.5 * x, 157)
    rt(15)
    circle(1.1 * x, 17)
    lt(23)
    fd(0.25 * x)
    bk(0.45 * x)
    lt(180)
    circle(0.17 * x, 180)
    lt(8)
    circle(-2.2 * x, 43)
    circle(1.4 * x, 32)
    rt(6)
    circle(0.65 * x, 115)
    circle(0.65 * x, -60)
    seth(137)
    circle(0.45 * x, 57)
    circle(0.45 * x, -57)
    seth(175)
    circle(0.65 * x, -15)
    rt(50)
    circle(3.5 * x, 81.5)
    lt(130)
    circle(-0.8 * x, 34)
    lt(5)
    circle(1.66 * x, 37)
    go(endHair)
    end_fill()

    # draw bow
    # center circle
    pu()
    go(startBow2)
    seth(121)
    pd()
    fillcolor(BOW_COLOR)
    begin_fill()
    circle(0.4 * x)
    end_fill()

    # right part
    begin_fill()
    lt(100)
    circle(1.9 * x, -48)
    seth(346)
    circle(-0.75 * x, 49)
    startLeftHand = pos()
    seth(292)
    circle(-0.8 * x, 34)
    lt(15)
    circle(-1.35 * x, 39)
    lt(25)
    endHand = pos()
    circle(-0.5 * x, 132)
    lt(22)
    circle(-2.6 * x, 31)
    rt(77)
    circle(0.4 * x, 74)
    go(startBow2)
    end_fill()

    pu()
    seth(121)
    circle(0.4 * x, -50)
    seth(23)
    pd()
    circle(-0.6 * x, 85)

    # left part
    pu()
    go(startBow2)
    seth(121)
    circle(0.4 * x, 98)
    rt(105)
    startBow3 = pos()
    begin_fill()
    pd()
    circle(1.2 * x, 43)
    seth(145)
    circle(0.75 * x, 90)
    startRightHand = pos()
    circle(1.1 * x, 94)
    lt(28)
    circle(1.6 * x, 53)
    startBody = pos()
    lt(85)
    circle(-0.4 * x, 92)
    go(startBow3)
    end_fill()

    pu()
    circle(-0.4 * x, -50)
    seth(140)
    pd()
    circle(0.5 * x, 77)

    # draw the ribbon
    pu()
    go(startBow3)
    circle(0.4 * x, 95)
    startRibbon1 = pos()
    pd()
    begin_fill()
    seth(258)
    circle(-1.8 * x, 43)
    rt(11)
    circle(1.5 * x, 29)
    lt(49)
    startBody2 = pos()
    circle(0.6 * x, 60)
    lt(74)
    circle(-1.5 * x, 39)
    lt(32)
    circle(1.8 * x, 44.3)
    lt(88)
    circle(-0.4 * x, 53)
    go(startRibbon1)
    end_fill()

    pu()
    circle(-0.4 * x, -53)
    seth(275)
    begin_fill()
    pd()
    circle(1.6 * x, 40)
    rt(10)
    circle(-2.45 * x, 37)
    lt(74)
    circle(0.6 * x, 52)
    lt(42)
    circle(1.6 * x, 55)
    lt(12)
    circle(-2.6 * x, 31.5)
    lt(121)
    circle(-0.4 * x, 41)
    end_fill()

    # draw right hand
    pu()
    go(startRightHand)
    fillcolor(GLOVE_COLOR)
    begin_fill()
    pd()
    seth(168)
    circle(-2.2 * x, 56)
    lt(20)
    circle(0.3 * x, 100)
    lt(25)
    circle(0.67 * x, 47)
    rt(168)
    circle(0.85 * x, 75)
    circle(0.75 * x, 118)
    rt(1)
    circle(5 * x, 34.5)
    rt(66)
    circle(1.1 * x, -63)
    go(startRightHand)
    end_fill()

    fillcolor(COSTUME_COLOR)
    begin_fill()
    seth(168)
    circle(-2.2 * x, 39)
    lt(154)
    circle(-1.55 * x, 71)
    lt(130)
    circle(5 * x, 21.5)
    rt(66)
    circle(1.1 * x, -63)
    go(startRightHand)
    end_fill()

    # draw left hand
    pu()
    go(startLeftHand)
    fillcolor(COSTUME_COLOR)
    begin_fill()
    pd()
    seth(292)
    circle(-0.8 * x, 34)
    lt(15)
    circle(-1.35 * x, 39)
    seth(12)
    fd(2.7 * x)
    startGlove = pos()
    lt(134)
    circle(-1.1 * x, 85)
    go(startLeftHand)
    end_fill()

    pu()
    go(startGlove)
    seth(146)
    fillcolor(GLOVE_COLOR)
    begin_fill()
    pd()
    circle(-1.1 * x, 93)
    lt(82)
    circle(-2.4 * x, -6)
    lt(162)
    circle(0.5 * x, 157)
    seth(25)
    circle(-0.8 * x, 102)
    lt(10)
    circle(-0.6 * x, 102)
    lt(15)
    circle(-3.8 * x, 24)
    end_fill()

    pu()
    go(startBody)
    fillcolor(COSTUME_COLOR)
    begin_fill()
    pd()
    seth(50)
    circle(1.6 * x, -33)
    seth(225)
    circle(1.8 * x, 36)
    rt(30)
    circle(1.5 * x, -26)
    lt(11)
    circle(-1.8 * x, -43)
    end_fill()

    pu()
    go(startBody)
    seth(50)
    circle(1.6 * x, -26)
    pd()
    seth(220)
    circle(1 * x, 52)

    pu()
    go(startBody2)
    seth(282)
    circle(0.6 * x, 8)
    fillcolor(COSTUME_COLOR)
    begin_fill()
    pd()
    seth(242)
    circle(0.75 * x, 51)
    rt(128)
    circle(1.9 * x, 58)
    lt(15)
    circle(1.2 * x, 96)
    lt(6)
    startRightShoe = pos()
    circle(1.4 * x, 67)
    lt(75)
    circle(1.3 * x, 7)
    seth(0)
    bk(0.4 * x)
    fd(1.1 * x)
    seth(331)
    circle(2 * x, 58)
    rt(68)
    circle(2.6 * x, 49)
    rt(6)
    startLeftShoe = pos()
    circle(0.9 * x, 140)
    lt(40)
    circle(-2.1 * x, 35)
    rt(75)
    circle(0.9 * x, 62)
    rt(10)
    circle(-0.9 * x, 60)
    go(endHand)
    seth(260)
    circle(-0.5 * x, 132)
    lt(22)
    circle(-2.6 * x, 31)
    rt(7)
    circle(-2.6 * x, -31.5)
    rt(12)
    circle(1.6 * x, -55)
    rt(42)
    circle(0.6 * x, -52)
    rt(74)
    circle(-2.45 * x, -37)
    lt(10)
    circle(1.6 * x, -40)
    lt(177)
    circle(1.8 * x, -44.3)
    rt(32)
    circle(-1.5 * x, -38)
    rt(74)
    circle(0.6 * x, -52)
    end_fill()

    pu()
    go(startBody2)
    seth(282)
    circle(0.6 * x, 50)
    pd()
    seth(261)
    circle(1.45 * x, 35)
    lt(9)
    circle(1.7 * x, 112)
    lt(22)
    circle(2.7 * x, 36)

    # draw shoes
    # right shoe
    pu()
    go(startRightShoe)
    seth(340)
    fillcolor(GLOVE_COLOR)
    begin_fill()
    pd()
    circle(1.4 * x, 67)
    lt(75)
    circle(1.3 * x, -26)
    seth(227)
    circle(-2.2 * x, 73)
    rt(24)
    circle(-0.65 * x, 68)
    rt(20)
    circle(-0.65 * x, 87)
    go(startRightShoe)
    end_fill()

    seth(328)
    circle(-0.7 * x, 44)
    pu()
    go(startRightShoe)
    seth(340)
    circle(1.4 * x, 11)
    pd()
    seth(328)
    circle(-0.5 * x, 44)

    # left shoe
    pu()
    go(startLeftShoe)
    seth(4)
    begin_fill()
    pd()
    circle(0.9 * x, 140)
    lt(40)
    circle(2.1 * x, -16)
    seth(319)
    circle(-1.6 * x, 90)
    rt(13)
    circle(-1 * x, 42)
    lt(11)
    circle(-0.57 * x, 133)
    go(startLeftShoe)
    end_fill()

    seth(4)
    circle(0.9 * x, 25)
    seth(353)
    circle(-0.7 * x, 50)
    pu()
    go(startLeftShoe)
    seth(4)
    circle(0.9 * x, 35)
    seth(353)
    pd()
    circle(-0.7 * x, 41)

    ht()


pu()
goto(-100, 200)
pd()
drawDipperDancing(40)
done()
