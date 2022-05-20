from turtle import *
from math import *

speed(0)


def go(tup):
    goto(tup[0], tup[1])


def mark():
    dot(4, "black")


def changePenColor():
    pencolor('red')


def oval(r):
    for loop in range(2):
        circle(r, 90)
        circle(r/2, 90)


def calculateAngle(tup1, tup2):
    dy = tup2[1] - tup1[1]
    dx = tup2[0] - tup1[0]
    angle = atan(abs(dy / dx))
    return angle / pi * 180


def drawHunter(x):
    FACE_COLOR = '#b8967d'
    FACE_SHADE_COLOR = '#91787a'
    SCLERA_COLOR = '#ece3d4'
    PUPIL_COLOR = '#963662'
    IRIS_COLOR_1 = '#030000'
    IRIS_COLOR_2 = '#fbfeff'
    EYE_SHADING_COLOR = '#765d5c'
    EYEBROW_COLOR = '#030603'
    EAR_COLOR = '#92787c'
    SCAR_COLOR = '#b27662'
    SCAR_LINE_COLOR = '#a2705a'
    SCAR_SHADE_COLOR = '#734847'
    SCAR_SHADE_LINE_COLOR = '#886c6a'
    BANDAGE_COLOR = '#e5dcd1'
    HAIR_COLOR_1 = '#594b42'
    HAIR_COLOR_2 = '#89795c'
    HAIR_COLOR_3 = '#786864'
    HAIR_COLOR_4 = '#b8a98c'
    HAIR_COLOR_5 = '#796965'
    BURNT_HAIR_COLOR_1 = '#564133'
    BURNT_HAIR_COLOR_2 = '#392927'
    COAT_COLOR = '#d1ccb4'
    COAT_SHADE_COLOR = '#878084'

    # draw face
    fillcolor(FACE_COLOR)
    begin_fill()
    startFace = pos()
    seth(350)
    fd(0.55 * x)
    lt(90)
    circle(-3.9 * x, 45)
    rt(10)
    circle(-2.7 * x, 45)
    rt(28)
    startHair3 = pos()
    circle(-3 * x, 14)
    midHairTop = pos()
    lt(10)
    circle(-2.2 * x, 67)
    preStartEye = pos()
    lt(63)
    circle(-2.7 * x, 49)
    seth(162)
    fd(0.7 * x)
    seth(265)
    fd(0.95 * x)
    seth(210)
    fd(0.4 * x)
    startMouth = pos()
    seth(269)
    circle(-2.6 * x, 43)
    midFaceShading = pos()
    circle(-0.6 * x, 48)
    lt(4)
    circle(-3.65 * x, 29)
    seth(238)
    fd(0.3 * x)
    startCoat = pos()
    seth(126)
    circle(5.7 * x, 34)
    startHair1 = pos()
    rt(103)
    circle(-1.4 * x, 57)
    seth(85)
    fd(0.9 * x)
    seth(184)
    circle(-1.4 * x, -25)
    circle(-1.4 * x, 77)
    startFaceShading = pos()
    rt(3)
    circle(-6.5 * x, 31)
    preStartEar = pos()
    rt(82)
    circle(-3.8 * x, 39)
    lt(7)
    circle(-0.8 * x, 82)
    midHairTop2 = pos()
    go(startFace)
    end_fill()

    # draw mouth
    pu()
    go(startMouth)
    pd()
    seth(164)
    circle(-2.3 * x, 35)
    pu()
    seth(32)
    fd(0.25 * x)
    pd()
    seth(135)
    circle(0.3 * x, 100)

    # draw eye
    # sclera part
    pu()
    go(preStartEye)
    seth(125)
    fd(0.6 * x)
    pd()
    fillcolor(SCLERA_COLOR)
    begin_fill()
    seth(120)
    circle(0.9 * x, 90)
    startEyeShading = pos()
    lt(58)
    circle(2.3 * x, 33)
    seth(-60)
    circle(0.4 * x, 80)
    startEyeShadingOverlapPart = pos()
    pu()
    circle(0.4 * x, 60)
    pd()
    pu()
    seth(225)
    fd(0.17 * x)
    seth(90)
    fd(0.03 * x)
    pd()
    startPupil = pos()
    seth(33)
    r = 0.6 * x
    for loop in range(2):
        circle(r/10, -90)
        circle(r, -90)
    circle(r, 80)
    seth(198)
    circle(-0.11 * x, -130)
    end_fill()

    # pupil part
    pu()
    go(startPupil)
    pd()
    fillcolor(PUPIL_COLOR)
    begin_fill()
    seth(33)
    r = 0.6 * x
    for loop in range(2):
        circle(r / 10, -90)
        circle(r, -90)
    end_fill()

    # iris part
    pu()
    circle(r / 10, -90)
    circle(r, -30)
    pd()
    fillcolor(IRIS_COLOR_1)
    begin_fill()
    circle(r, -38)
    seth(130)
    circle(0.3 * x, -103)
    end_fill()

    pu()
    seth(0)
    fd(0.26 * x)
    seth(90)
    fd(0.2 * x)
    pd()
    fillcolor(IRIS_COLOR_2)
    begin_fill()
    rt(56)
    r1 = 0.25 * x
    for loop in range(2):
        circle(r1, 90)
        circle(r1/4, 90)
    end_fill()

    # eye shading
    pu()
    go(startEyeShading)
    fillcolor(EYE_SHADING_COLOR)
    begin_fill()
    seth(253)
    circle(1.7 * x, 64)
    pd()
    lt(10)
    circle(0.3 * x, 100)
    rt(20)
    pu()
    circle(0.1 * x, 170)
    pd()
    go(startEyeShadingOverlapPart)
    seth(20)
    circle(0.4 * x, -80)
    seth(301)
    circle(2.3 * x, -33)
    end_fill()

    # draw eyebrow
    pu()
    go(preStartEye)
    seth(142)
    fd(2.6 * x)
    startEyebrow = pos()
    fillcolor(EYEBROW_COLOR)
    begin_fill()
    pd()
    seth(40)
    circle(-1.5 * x, 55)
    rt(17)
    circle(-1.9 * x, 28)
    seth(90)
    fd(0.15 * x)
    seth(-70)
    circle(-0.9 * x, 52)
    seth(123)
    fd(1.05 * x)
    rt(12)
    circle(0.45 * x, 100 - 10)
    go(startEyebrow)
    end_fill()

    pu()
    go(preStartEye)
    seth(120)
    fd(0.65 * x)
    seth(90)
    fd(0.02 * x)
    pd()
    seth(100)
    circle(1.2 * x, 23)

    # draw bandage
    pu()
    go(preStartEye)
    seth(117)
    fd(2.4 * x)
    startBandage = pos()
    fillcolor(BANDAGE_COLOR)
    begin_fill()
    pd()
    seth(177)
    circle(2.9 * x, 35)
    rt(111)
    fd(0.7 * x)
    seth(212)
    circle(2.9 * x, -35)
    go(startBandage)
    end_fill()

    # draw ear
    pu()
    go(preStartEar)
    seth(-35)
    fd(0.8 * x)
    pd()
    lt(12)
    circle(-2.4 * x, 6)
    fillcolor(EAR_COLOR)
    begin_fill()
    circle(-2.4 * x, 49)
    circle(-2.4 * x, -8)
    seth(160)
    pu()
    circle(-1.72 * x, 59)
    end_fill()

    # draw the shade on the face
    pu()
    go(startFaceShading)
    fillcolor(FACE_SHADE_COLOR)
    begin_fill()
    seth(-16)
    circle(2.5 * x, 37)
    circle(-0.3 * x, 140)
    lt(20)
    circle(2.5 * x, 43)
    lt(8)
    circle(7.15 * x, 25.5)
    go(midFaceShading)
    pd()
    seth(226)
    circle(-0.6 * x, 48)
    lt(4)
    circle(-3.65 * x, 29)
    seth(238)
    fd(0.3 * x)
    seth(126)
    circle(5.7 * x, 34)
    rt(103)
    circle(-1.4 * x, 57)
    seth(85)
    fd(0.9 * x)
    seth(184)
    circle(-1.4 * x, 52)
    end_fill()

    # draw the scar
    pu()
    go(preStartEye)
    seth(241)
    fd(5.1 * x)
    seth(270)
    fd(0.2 * x)
    seth(180)
    fd(0.2 * x)
    pd()
    startScar = pos()
    seth(155)
    circle(-5.1 * x, 22)
    lt(8)
    circle(-1.55 * x, 56)
    circle(-1.55 * x, -36)
    fillcolor(SCAR_COLOR)
    begin_fill()
    startScarShading = pos()
    circle(-1.55 * x, -20)
    rt(8)
    circle(-5.1 * x, -7)
    pencolor(SCAR_LINE_COLOR)
    pensize(2)
    seth(78)
    circle(-5.15 * x, 25)
    seth(197)
    circle(3.5 * x, 34.5)
    end_fill()

    # draw shading on the scar
    pu()
    go(startScarShading)
    fillcolor(SCAR_SHADE_COLOR)
    begin_fill()
    seth(121)
    circle(-1.55 * x, -20)
    rt(8)
    circle(-5.1 * x, -7)
    pd()
    pencolor(SCAR_SHADE_LINE_COLOR)
    seth(78)
    circle(-5.15 * x, 5.5)
    rt(116)
    pu()
    circle(7.15 * x, -4.5)
    seth(304)
    circle(2.5 * x, -9)
    pd()
    rt(73)
    circle(3.5 * x, 8.5)
    end_fill()
    pensize(1)
    pencolor('black')

    # redraw scar
    pu()
    go(startScar)
    pd()
    seth(155)
    circle(-5.1 * x, 22)
    lt(8)
    circle(-1.55 * x, 56)

    # draw hair
    # part in the back
    pu()
    go(startHair1)
    fillcolor(HAIR_COLOR_1)
    begin_fill()
    pd()
    seth(150)
    circle(3.1 * x, 28)
    seth(129)
    circle(-4.8 * x, 59)
    startHairTop = pos()
    pu()
    rt(9)
    circle(-2.9 * x, 35)
    startHairMiddle = pos()
    rt(141)
    circle(1.3 * x, 46.8)
    pd()
    lt(80)
    circle(-3.8 * x, -4.5)
    lt(82)
    circle(-6.5 * x, -31)
    lt(3)
    circle(-1.4 * x, -52)
    seth(85)
    bk(0.9 * x)
    seth(0)
    circle(-1.4 * x, -57)
    end_fill()

    # draw the top part of the hair
    pu()
    go(startHairTop)
    fillcolor(HAIR_COLOR_4)
    begin_fill()
    pd()
    seth(203)
    circle(-1.7 * x, 44)
    rt(125)
    circle(2.2 * x, 49)
    rt(7)
    circle(-2.1 * x, 71)
    lt(160)
    circle(-1.7 * x, 40)
    rt(136)
    circle(2.5 * x, 54)
    rt(20)
    circle(-2.8 * x, 68)
    seth(116)
    circle(-2 * x, -8)
    circle(-2 * x, 44)
    seth(281)
    circle(2 * x, 83)
    rt(4)
    fd(0.8 * x)
    circle(-1.25 * x, 98)
    rt(2)
    circle(-2.4 * x, 52.5)
    go(midHairTop)
    seth(298)
    circle(-3 * x, -14)
    lt(28)
    circle(-2.7 * x, -45)
    lt(10)
    circle(-3.9 * x, -45)
    rt(90)
    bk(0.55 * x)
    go(midHairTop2)
    seth(262)
    circle(-0.8 * x, -82)
    rt(7)
    circle(-3.8 * x, -34.5)
    seth(291.8)
    circle(1.3 * x, -46.8)
    lt(141)
    circle(-2.9 * x, -35)
    end_fill()

    # shading part on the top
    fillcolor(HAIR_COLOR_5)
    begin_fill()
    seth(203)
    circle(-1.7 * x, 44)
    rt(125)
    circle(2.2 * x, 49)
    rt(7)
    circle(-2.1 * x, 71)
    lt(160)
    circle(-1.7 * x, 40)
    rt(136)
    circle(2.5 * x, 54)
    rt(20)
    circle(-2.8 * x, 10)
    pu()
    seth(244)
    circle(-1.85 * x, 61)
    lt(137)
    circle(1.8 * x, 25)
    rt(159)
    circle(2.2 * x, 67)
    rt(8)
    circle(-1.9 * x, 26)
    lt(133 + 3)
    circle(2.5 * x, 30)
    pd()
    seth(26)
    circle(-2.9 * x, -35)
    end_fill()

    # part in the middle
    pu()
    go(startHairMiddle)
    pd()
    fillcolor(HAIR_COLOR_2)
    begin_fill()
    seth(245)
    circle(1.3 * x, 46.8)
    lt(80)
    circle(-3.8 * x, 34.5)
    lt(7)
    circle(-0.8 * x, 82)
    go(startFace)
    seth(350)
    fd(0.55 * x)
    lt(90)
    circle(-3.9 * x, 45)
    pu()
    seth(125)
    circle(2.2 * x, 60)
    lt(28)
    circle(-2 * x, -15)
    startHair2 = pos()
    circle(-2 * x, 75)
    circle(-2 * x, -4)
    lt(34)
    circle(2.7 * x, 21)
    end_fill()

    # shading part in the middle
    pu()
    go(startHair2)
    fillcolor(HAIR_COLOR_3)
    begin_fill()
    pd()
    seth(228)
    circle(-2 * x, 75)
    seth(22)
    circle(2.2 * x, 25)
    pu()
    rt(151)
    circle(-1.15 * x, 30)
    lt(116)
    circle(2 * x, 50)
    end_fill()

    pu()
    go(startHair3)
    fillcolor(HAIR_COLOR_2)
    begin_fill()
    pd()
    seth(124)
    circle(3.2 * x, 21)
    pu()
    circle(3.2 * x, 33)
    lt(152)
    circle(-3.3 * x, 31)
    pd()
    lt(69)
    circle(-2.7 * x, 28)
    end_fill()

    # front part of the hair
    pu()
    go(midHairTop)
    fillcolor(HAIR_COLOR_5)
    begin_fill()
    pd()
    seth(207.5)
    circle(-2.4 * x, -21)
    seth(32)
    circle(-2.1 * x, 28)
    rt(17)
    circle(-0.55 * x, 85)
    seth(240)
    circle(2.2 * x, 25)
    rt(15)
    circle(1.2 * x, 42)
    lt(2)
    startBurntHair1 = pos()
    circle(-1.45 * x, 46)
    seth(96)
    circle(1.3 * x, 30)
    circle(1.3 * x, -20)
    seth(158)
    fd(0.45 * x)
    seth(68)
    fd(0.15 * x)
    bk(0.5 * x)
    seth(112)
    fd(0.8 * x)
    circle(-1.5 * x, 58)
    seth(72)
    circle(0.4 * x, 61)
    lt(97)
    circle(-2.2 * x, -7)
    circle(-2.2 * x, 30)
    lt(85)
    circle(-2.2 * x, -17)
    end_fill()

    pu()
    go(midHairTop)
    fillcolor(HAIR_COLOR_4)
    begin_fill()
    pd()
    seth(207.5)
    circle(-2.4 * x, -21)
    seth(32)
    circle(-2.1 * x, 28)
    rt(17)
    circle(-0.55 * x, 85)
    seth(240)
    circle(2.2 * x, 25)
    rt(15)
    circle(1.2 * x, 42)
    rt(-2)
    circle(-1.45 * x, 46)
    seth(96)
    circle(1.3 * x, 10)
    seth(158)
    fd(0.2 * x)
    pu()
    seth(117)
    circle(-2.9 * x, 53)
    circle(0.2 * x, 127)
    lt(12)
    circle(4 * x, 20)
    lt(77)
    circle(-2.2 * x, -9)
    end_fill()

    # draw the burnt part
    pu()
    go(startBurntHair1)
    fillcolor(BURNT_HAIR_COLOR_1)
    begin_fill()
    pd()
    seth(294)
    circle(-1.45 * x, 46)
    seth(96)
    circle(1.3 * x, 10)
    seth(158)
    fd(0.2 * x)
    seth(117)
    circle(-2.9 * x, 13)
    startBurntHair2 = pos()
    seth(0)
    pu()
    circle(0.6 * x, 53)
    end_fill()

    pu()
    go(startBurntHair2)
    fillcolor(BURNT_HAIR_COLOR_2)
    begin_fill()
    pd()
    seth(104)
    circle(-2.9 * x, -13)
    seth(158)
    fd(0.25 * x)
    seth(68)
    bk(0.35 * x)
    seth(112)
    fd(0.8 * x)
    rt(48)
    pu()
    circle(-0.3 * x, 96)
    end_fill()

    # draw coat
    pu()
    go(startCoat)
    pd()
    fillcolor(COAT_COLOR)
    begin_fill()
    seth(126)
    circle(5.7 * x, 34)
    seth(150)
    circle(3.1 * x, 28)
    lt(3)
    circle(2.55 * x, 15)
    startCoatShade1 = pos()
    circle(2.55 * x, 33)
    circle(2.3 * x, 100)
    rt(10)
    startCoat2 = pos()
    circle(2 * x, 47)
    seth(16)
    fd(2.5 * x)
    rt(5)
    circle(-3.1 * x, 62)
    lt(112)
    circle(1 * x, 39)
    lt(6)
    circle(3.8 * x, 42)
    end_fill()

    pu()
    go(startCoatShade1)
    pd()
    fillcolor(COAT_SHADE_COLOR)
    begin_fill()
    seth(196)
    circle(2.55 * x, 33)
    circle(2.3 * x, 100)
    rt(10)
    circle(2 * x, 47)
    seth(16)
    fd(2.5 * x)
    rt(5)
    circle(-3.1 * x, 27)
    pu()
    lt(133)
    circle(1.4 * x, 58)
    seth(188)
    circle(-8.2 * x, 20)
    seth(160)
    circle(-2 * x, 117)
    end_fill()

    pu()
    go(startCoat2)
    pd()
    fillcolor(COAT_COLOR)
    begin_fill()
    seth(319)
    circle(2 * x, 47)
    seth(16)
    fd(2.5 * x)
    rt(5)
    circle(-3.1 * x, 62)
    circle(-2 * x, 43)
    seth(180)
    fd(9.3 * x)
    rt(116)
    circle(-6.5 * x, 27)
    end_fill()

    pu()
    go(startCoat2)
    pd()
    fillcolor(COAT_SHADE_COLOR)
    begin_fill()
    seth(319)
    circle(2 * x, 47)
    pu()
    rt(146)
    circle(5 * x, 26)
    pd()
    seth(180)
    fd(2.1 * x)
    rt(116)
    circle(-6.5 * x, 27)
    end_fill()

    ht()


pu()
goto(-50, 57)
pd()
drawHunter(38.5)
done()