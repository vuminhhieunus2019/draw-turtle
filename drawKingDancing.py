from turtle import *
from math import *

speed(0)


def go(tup):
    goto(tup[0], tup[1])


def mark():
    dot(4, "black")


def oval(r):               
    for loop in range(2):      
        circle(r, 90)    
        circle(r/2, 90) 


def calculateAngle(tup1, tup2):
    dy = tup2[1] - tup1[1]
    dx = tup2[0] - tup1[0]
    angle = atan(abs(dy / dx))
    return angle / pi * 180


def drawMusicalNote1(x):
    MAIN_COLOR = '#280615'
    REC_COLOR_1 = '#be4354'
    REC_COLOR_2 = '#721626'

    fillcolor(MAIN_COLOR)
    begin_fill()
    start = pos()
    seth(103)
    circle(0.6 * x, 103)
    lt(20)
    circle(0.55 * x, 108)
    rt(20)
    circle(0.5 * x, 125)
    seth(60)
    fd(1.7 * x)
    startReg = pos()
    seth(337)
    fd(1.5 * x)
    rt(90)
    fd(1.2 * x)
    rt(125)
    circle(1.2 * x, 32)
    lt(14)
    circle(0.4 * x, 145)
    rt(12)
    circle(0.6 * x, 100)
    lt(25)
    fd(2.3 * x)
    seth(157)
    fd(1.8 * x)
    go(start)
    end_fill()

    pu()
    go(startReg)
    seth(60)
    fd(0.05 * x)
    startReg2 = pos()
    fillcolor(REC_COLOR_1)
    begin_fill()
    pd()
    fd(0.35 * x)
    seth(337)
    fd(1.55 * x)
    seth(250)
    fd(0.35 * x)
    go(startReg2)
    end_fill()

    pu()
    go(startReg)
    seth(60)
    fd(0.42 * x)
    startReg2 = pos()
    fillcolor(REC_COLOR_2)
    begin_fill()
    pd()
    fd(0.35 * x)
    seth(337)
    fd(1.55 * x)
    seth(250)
    fd(0.35 * x)
    go(startReg2)
    end_fill()


def drawMusicalNote2(x):
    MAIN_COLOR = '#280615'
    REC_COLOR_1 = '#be4354'
    REC_COLOR_2 = '#721626'

    fillcolor(MAIN_COLOR)
    begin_fill()
    start = pos()
    seth(132)
    circle(1.1 * x, 34)
    rt(20)
    circle(0.25 * x, 180)
    rt(13)
    circle(0.8 * x, 80)
    seth(60)
    fd(1 * x)
    startReg = pos()
    seth(345)
    fd(1.2 * x)
    rt(95)
    fd(0.8 * x)
    rt(103)
    circle(0.7 * x, 25)
    rt(23)
    circle(0.25 * x, 180)
    rt(15)
    circle(0.7 * x, 33)
    circle(0.3 * x, 90)
    rt(6)
    fd(1.8 * x)
    seth(165)
    fd(1.55 * x)
    go(start)
    end_fill()

    pu()
    go(startReg)
    seth(60)
    fd(0.05 * x)
    startReg2 = pos()
    fillcolor(REC_COLOR_1)
    begin_fill()
    pd()
    fd(0.35 * x)
    seth(345)
    fd(1.2 * x)
    rt(95)
    fd(0.35 * x)
    go(startReg2)
    end_fill()

    pu()
    go(startReg)
    seth(60)
    fd(0.42 * x)
    startReg2 = pos()
    fillcolor(REC_COLOR_2)
    begin_fill()
    pd()
    fd(0.35 * x)
    seth(345)
    fd(1.15 * x)
    rt(95)
    fd(0.35 * x)
    go(startReg2)
    end_fill()


def drawKingDancing(x):
    SKULL_COLOR = '#f0dec2'
    FIRST_EYE_COLOR = '#000000'
    SECOND_EYE_COLOR = '#f7fd3c'
    THIRD_EYE_COLOR = '#c86a8c'
    FOURTH_EYE_COLOR = '#000000'
    FIRST_HORN_COLOR = '#fdfcf5'
    SECOND_HORN_COLOR = '#edece1'
    FANG_COLOR = '#fffcf7'
    PATTERN_COLOR = '#fcfbf5'
    FUR_COLOR = '#3f434c'
    FUR_COLOR_2 = '#383944'
    FUR_COLOR_3 = '#24212d'
    COLLAR_COLOR = '#5a1d1b'
    COLLAR_COLOR_2 = '#564458'
    SHIRT_COLOR = '#f4abdb'
    PAW_COLOR = '#f0dec2'
    PAW_COLOR_2 = '#cfb9a3'
    SHADED_PAW_COLOR = '#8d8281'
    INNER_SHIRT_COLOR = '#995e92'
    PANT_COLOR = '#211e43'
    OVAL_COLOR = '#685563'
    TAIL_COLOR = '#997d7d'

    # draw the skull
    pu()
    seth(95)
    circle(-0.6 * x, 18)
    pd()
    startEye1 = pos()
    mark()
    fillcolor(SKULL_COLOR)
    begin_fill()
    circle(-0.6 * x, 78)
    startHorn1 = pos()
    lt(15)
    circle(-2 * x, 92)
    endHorn2 = pos()
    rt(10)
    circle(-1.7 * x, 55)
    rt(24)
    circle(-1.4 * x, 35)
    startPat1 = pos()
    mark()
    rt(61)
    fd(0.45 * x)
    lt(23)
    circle(0.2 * x, 100)
    rt(110)
    startFang1 = pos()
    circle(0.2 * x, 108)
    lt(22)
    fd(0.33 * x)
    rt(38)
    fd(0.4 * x)
    rt(78)
    circle(-1.1 * x, 55)
    rt(45)
    circle(-0.9 * x, 40)
    circle(-0.9 * x, -10)
    lt(57)
    circle(0.85 * x, 72)
    lt(12)
    circle(0.7 * x, 65)
    end_fill()

    # draw the right eye
    pu()
    go(startEye1)
    seth(95)
    fillcolor(FIRST_EYE_COLOR)
    pd()
    begin_fill()
    circle(-0.6 * x, -20)
    lt(100)
    circle(0.68 * x, 120)
    seth(79)
    pu()
    circle(-1.1 * x, 8)
    rt(51)
    circle(-0.9 * x, 30)
    lt(59)
    circle(0.85 * x, 72)
    lt(12)
    circle(0.7 * x, 63)
    end_fill()

    go(startEye1)
    seth(270)
    fd(0.6 * x)
    seth(25)
    pd()
    fillcolor(SECOND_EYE_COLOR)
    begin_fill()
    circle(-0.5 * x, 90)
    lt(150)
    circle(0.37 * x, 152)
    end_fill()

    # draw left eye
    pu()
    go(startEye1)
    seth(316)
    fd(2.55 * x)
    seth(0)
    pd()
    fillcolor(FIRST_EYE_COLOR)
    begin_fill()
    circle(0.65 * x)
    end_fill()

    pu()
    seth(110)
    fd(0.15 * x)
    pd()
    seth(0)
    fillcolor(SECOND_EYE_COLOR)
    begin_fill()
    circle(0.56 * x)
    end_fill()

    pu()
    seth(102)
    fd(0.45 * x)
    pd()
    seth(0)
    fillcolor(THIRD_EYE_COLOR)
    begin_fill()
    circle(0.23 * x)
    end_fill()

    pu()
    seth(90)
    fd(0.15 * x)
    pd()
    seth(0)
    fillcolor(FOURTH_EYE_COLOR)
    begin_fill()
    circle(0.08 * x)
    end_fill()

    # draw horns
    pu()
    go(startHorn1)
    seth(14)
    fillcolor(FIRST_HORN_COLOR)
    begin_fill()
    pd()
    circle(-2 * x, 41)
    startHorn2 = pos()
    lt(70)
    circle(-3.8 * x, 15)
    startHorn3 = pos()
    lt(40)
    fd(0.85 * x)
    lt(119)
    circle(3.9 * x, 39)
    end_fill()

    pu()
    go(startHorn2)
    seth(43)
    begin_fill()
    pd()
    circle(-3.8 * x, 15)
    seth(28)
    circle(-3.8 * x, 3)
    rt(115)
    pu()
    fd(0.55 * x)
    pd()
    lt(109)
    circle(-0.82 * x, 86)
    rt(66)
    endHorn3 = pos()
    fd(1.4 * x)
    go(endHorn2)
    seth(282)
    circle(-2 * x, -50)
    end_fill()

    pu()
    go(startHorn3)
    seth(31)
    pd()
    fillcolor(SECOND_HORN_COLOR)
    begin_fill()
    circle(-3.8 * x, 39)
    go(endHorn3)
    seth(293)
    pencolor('#cfcec3')
    circle(-0.8 * x, -87)
    rt(109)
    bk(0.55 * x)
    pencolor('black')
    end_fill()

    # draw nose
    pu()
    go(startEye1)
    seth(288)
    fd(1.35 * x)
    startNose = pos()
    pd()
    seth(262)
    fillcolor('black')
    begin_fill()
    circle(1.1 * x, 35)
    lt(115)
    fd(0.63 * x)
    lt(138)
    fd(0.35 * x)
    go(startNose)
    end_fill()

    # draw fangs
    pu()
    go(startFang1)
    fillcolor(FANG_COLOR)
    begin_fill()
    pd()
    seth(110)
    circle(0.2 * x, 108)
    lt(22)
    fd(0.33 * x)
    lt(53)
    fd(0.7 * x)
    lt(129)
    circle(1.7 * x, 30)
    end_fill()

    pu()
    go(startEye1)
    seth(276)
    fd(2.08 * x)
    startFang2 = pos()
    begin_fill()
    pd()
    rt(162)
    circle(-1.1 * x, 28)
    lt(136)
    circle(1.3 * x, 42)
    startSkull2 = pos()
    go(startFang2)
    end_fill()

    # draw the remaining part of the skull
    pu()
    go(startSkull2)
    seth(264)
    circle(1.3 * x, -14)
    startFace1 = pos()
    circle(1.3 * x, -11)
    fillcolor(SKULL_COLOR)
    begin_fill()
    pd()
    seth(150)
    circle(-0.6 * x, 30)
    startPat2 = pos()
    circle(-0.6 * x, 79)
    rt(123)
    circle(0.68 * x, 55)
    lt(107)
    circle(-1.1 * x, -9)
    seth(222)
    circle(1.3 * x, 17)
    end_fill()

    # draw pattern on the skull
    pu()
    go(startPat2)
    seth(105)
    pd()
    fillcolor(PATTERN_COLOR)
    begin_fill()
    circle(-0.1 * x, 244)
    rt(170)
    circle(-0.2 * x, 75)
    rt(109.5)
    circle(1.3 * x, 12.5)
    seth(150)
    circle(-0.6 * x, 29)
    end_fill()

    pu()
    go(startPat1)
    seth(108)
    pd()
    begin_fill()
    circle(-0.17 * x, 214)
    rt(175)
    circle(-0.17 * x, 197)
    rt(57)
    circle(-1.4 * x, 27)
    end_fill()

    # draw the lower part of the face
    pu()
    go(startFace1)
    seth(192)
    fillcolor(FUR_COLOR)
    begin_fill()
    pd()
    fd(0.5 * x)
    rt(102)
    circle(-0.63 * x, 48)
    lt(120)
    circle(-0.43 * x, 65)
    rt(133)
    circle(0.4 * x, 58)
    lt(75)
    circle(-0.6 * x, -53)
    lt(90)
    circle(1.3 * x, 11)
    end_fill()

    pu()
    go(startFang2)
    seth(210)
    pd()
    begin_fill()
    fd(0.35 * x)
    lt(107)
    startCollar = pos()
    circle(2.4 * x, 48)
    rt(40)
    fd(0.34 * x)
    lt(90)
    fd(0.3 * x)
    rt(100)
    circle(0.5 * x, 50)
    lt(65)
    circle(0.55 * x, 40)
    rt(90)
    circle(0.35 * x, 70)
    lt(120)
    circle(-0.6 * x, 34)
    lt(58)
    circle(-1.7 * x, 5)
    rt(33)
    circle(-1.4 * x, 37)
    rt(61)
    fd(0.45 * x)
    lt(21)
    circle(0.2 * x, 100)
    seth(91)
    circle(1.7 * x, -29)
    rt(128)
    bk(0.7 * x)
    rt(90)
    fd(0.38 * x)
    rt(78)
    circle(-1.1 * x, 10)
    end_fill()

    # draw collar
    pu()
    go(startCollar)
    seth(317)
    circle(2.4 * x, 8)
    pd()
    fillcolor(FUR_COLOR_2)
    begin_fill()
    rt(55)
    circle(0.88 * x, 150)
    rt(55)
    circle(2.4 * x, -40)
    end_fill()

    pu()
    go(startCollar)
    seth(317)
    circle(2.4 * x, 13)
    pd()
    fillcolor(COLLAR_COLOR)
    begin_fill()
    rt(55)
    circle(0.7 * x, 142)
    rt(55)
    circle(2.4 * x, -31.5)
    end_fill()

    pu()
    go(startCollar)
    seth(317)
    circle(2.4 * x, 25)
    fillcolor(COLLAR_COLOR_2)
    begin_fill()
    pd()
    rt(85)
    fd(0.5 * x)
    lt(80)
    circle(0.88 * x, 8)
    lt(90)
    fd(0.5 * x)
    seth(345)
    circle(2.4 * x, -3)
    end_fill()

    # draw the shirt
    pu()
    go(startCollar)
    seth(317)
    circle(2.4 * x, 8)
    rt(55)
    circle(0.88 * x, 10)
    pd()
    fillcolor(SHIRT_COLOR)
    begin_fill()
    rt(122)
    fd(0.5 * x)
    startHand1 = pos()
    lt(130)
    circle(-0.9 * x, 60)
    lt(132)
    fd(0.5 * x)
    lt(44)
    circle(0.85 * x, 20)
    circle(0.85 * x, -66)
    rt(104)
    circle(0.6 * x, 76)
    startLeg1 = pos()
    lt(5)
    circle(2.7 * x, 50)
    endHand1 = pos()
    seth(198)
    circle(-0.7 * x, 70)
    rt(5)
    startPaw3 = pos()
    circle(-0.4 * x, 60)
    seth(145)
    fd(0.52 * x)
    seth(340)
    circle(0.88 * x, -60)
    end_fill()

    # draw musical notes on the shirt
    pu()
    go(startEye1)
    seth(270)
    fd(3.8 * x)
    drawMusicalNote1(0.17 * x)

    pu()
    go(startEye1)
    seth(280)
    fd(4.1 * x)
    drawMusicalNote2(0.18 * x)

    # draw right hand
    pu()
    go(startHand1)
    seth(158)
    pd()
    fillcolor(FUR_COLOR)
    begin_fill()
    fd(0.9 * x)
    rt(13)
    circle(-0.68 * x, 58)
    lt(137)
    circle(1 * x, 23)
    startPaw1 = pos()
    lt(5)
    fd(0.35 * x)
    lt(96)
    circle(-1.2 * x, 31)
    rt(111)
    circle(-0.95 * x, 42)
    seth(338)
    fd(1.62 * x)
    startInnerShirt1 = pos()
    rt(96)
    circle(-0.9 * x, -47)
    end_fill()

    pu()
    go(startPaw1)
    seth(175)
    fillcolor(PAW_COLOR)
    begin_fill()
    pd()
    fd(0.7 * x)
    lt(142)
    fd(0.55 * x)
    startPaw2 = pos()
    seth(353)
    circle(-1.2 * x, 9)
    go(startPaw1)
    end_fill()

    pu()
    go(startPaw2)
    seth(358)
    pd()
    begin_fill()
    circle(-1.2 * x, 40)
    rt(111)
    circle(-0.95 * x, 42)
    rt(41)
    circle(-0.3 * x, 78)
    end_fill()

    pu()
    go(startInnerShirt1)
    seth(65)
    fillcolor(INNER_SHIRT_COLOR)
    begin_fill()
    pd()
    circle(0.9 * x, -14)
    seth(125)
    circle(-0.35 * x, 45)
    go(startInnerShirt1)
    end_fill()

    # draw left hand
    pu()
    go(startPaw3)
    seth(123)
    fillcolor(PAW_COLOR)
    begin_fill()
    pd()
    circle(-0.4 * x, 60)
    seth(145)
    fd(0.45 * x)
    bk(0.72 * x)
    fd(0.72 * x)
    rt(125)
    circle(-0.75 * x, 60)
    seth(257)
    circle(-0.9 * x, 41)
    end_fill()

    fillcolor(FUR_COLOR)
    begin_fill()
    circle(-0.9 * x, -41)
    seth(60)
    circle(-0.6 * x, 25)
    rt(130)
    fd(0.3 * x)
    lt(85)
    fd(0.5 * x)
    bk(0.35 * x)
    startShirt = pos()
    lt(45)
    circle(-0.8 * x, 34)
    rt(46)
    circle(-0.5 * x, 92)
    rt(17)
    circle(-0.9 * x, 27)
    go(endHand1)
    seth(198)
    circle(-0.7 * x, 70)
    end_fill()

    # draw the remaining part of the shirt
    pu()
    go(startShirt)
    fillcolor(SHIRT_COLOR)
    begin_fill()
    seth(350)
    pd()
    bk(0.15 * x)
    rt(85)
    bk(0.3 * x)
    lt(130)
    circle(-0.6 * x, -25)
    lt(80)
    circle(0.75 * x, 26)
    lt(27)
    circle(-0.88 * x, -45)
    lt(87)
    fd(0.3 * x)
    lt(90)
    fd(0.12 * x)
    startInnerShirt2 = pos()
    seth(341)
    circle(-0.65 * x, 60)
    seth(343)
    circle(-0.8 * x, -52)
    end_fill()

    pu()
    go(startInnerShirt2)
    seth(341)
    circle(-0.65 * x, 60)
    fillcolor(INNER_SHIRT_COLOR)
    begin_fill()
    pd()
    rt(20)
    circle(-0.65 * x, 24)
    lt(40)
    circle(-0.5 * x, -38)
    lt(44)
    circle(-0.8 * x, 18)
    end_fill()

    # draw pant
    pu()
    go(startLeg1)
    fillcolor(PANT_COLOR)
    begin_fill()
    pd()
    seth(260)
    fd(0.3 * x)
    seth(233)
    fd(0.8 * x)
    lt(145)
    startLeg2 = pos()
    circle(-0.6 * x, 112)
    seth(53)
    fd(0.6 * x)
    rt(85)
    circle(0.75 * x, 50)
    startLeg3 = pos()
    rt(15)
    fd(1.05 * x)
    bk(0.35 * x)
    lt(33)
    circle(0.83 * x, 82)
    rt(95)
    circle(2.7 * x, -48)
    end_fill()

    # draw right leg
    pu()
    go(startLeg2)
    seth(18)
    fillcolor(FUR_COLOR)
    begin_fill()
    pd()
    circle(-0.6 * x, 112)
    seth(233)
    fd(1.45 * x)
    lt(170)
    mid1 = pos()
    circle(0.25 * x, 90)
    rt(10)
    startArch = pos()
    fd(0.3 * x)
    startPaw4 = pos()
    rt(14)
    fd(0.3 * x)
    lt(45)
    fd(0.27 * x)
    seth(53)
    fd(1 * x)
    go(startLeg2)
    end_fill()

    pu()
    go(startArch)
    seth(123)
    pd()
    fillcolor(FUR_COLOR_3)
    begin_fill()
    fd(0.3 * x)
    lt(45)
    fd(0.45 * x)
    lt(83)
    endPaw1 = pos()
    fd(0.4 * x)
    lt(63)
    fd(0.52 * x)
    lt(20)
    circle(0.32 * x, 77)
    go(mid1)
    seth(43)
    circle(0.25 * x, 90)
    end_fill()

    pu()
    go(startPaw4)
    seth(109)
    fillcolor(SHADED_PAW_COLOR)
    begin_fill()
    pd()
    fd(0.3 * x)
    midPaw1 = pos()
    lt(60 - 12)
    fd(0.55 * x)
    midPaw2 = pos()
    go(endPaw1)
    go(startPaw4)
    end_fill()

    fillcolor(PAW_COLOR_2)
    begin_fill()
    go(midPaw1)
    go(midPaw2)
    go(startPaw4)
    end_fill()

    pu()
    go(endPaw1)
    fillcolor(SHADED_PAW_COLOR)
    begin_fill()
    pd()
    seth(106)
    fd(0.12 * x)
    midPaw3 = pos()
    lt(60)
    fd(0.3 * x)
    midPaw4 = pos()
    seth(270)
    circle(0.91 * x, 38)
    go(endPaw1)
    end_fill()

    fillcolor(PAW_COLOR_2)
    begin_fill()
    go(midPaw3)
    go(midPaw4)
    go(endPaw1)
    end_fill()

    pu()
    seth(290)
    fd(0.35 * x)
    pd()
    rt(30)
    fillcolor(OVAL_COLOR)
    begin_fill()
    oval(0.2 * x)
    end_fill()

    # draw right leg
    pu()
    go(startLeg3)
    seth(3)
    fillcolor(FUR_COLOR)
    begin_fill()
    pd()
    fd(1.05 * x)
    bk(0.33 * x)
    lt(33)
    circle(0.83 * x, 78)
    seth(7)
    circle(-0.95 * x, 37)
    rt(24)
    circle(-0.7 * x, 56)
    rt(15)
    circle(-2.15 * x, 31)
    startPaw4 = pos()
    rt(12)
    circle(1.15 * x, 47)
    rt(47)
    endPaw = pos()
    circle(-0.8 * x, 35)
    seth(96)
    circle(-1.1 * x, 54)
    go(startLeg3)
    end_fill()

    pu()
    go(startPaw4)
    seth(313)
    fillcolor(PAW_COLOR_2)
    begin_fill()
    pd()
    fd(0.35 * x)
    rt(123)
    fd(0.4 * x)
    lt(119)
    circle(-0.6 * x, -27)
    circle(-0.6 * x, 47)
    seth(198)
    circle(-1.2 * x, 32)
    go(endPaw)
    seth(239)
    circle(1.15 * x, -47)
    end_fill()

    # draw tail
    pu()
    go(endHand1)
    fillcolor(FUR_COLOR_2)
    begin_fill()
    pd()
    seth(25)
    circle(2.7 * x, -2)
    seth(118)
    circle(0.75 * x, -4)
    seth(7)
    circle(-0.95 * x, 37)
    rt(24)
    circle(-0.7 * x, 56)
    rt(14)
    circle(-2.15 * x, 25)
    seth(346)
    circle(1.6 * x, 64)
    lt(7)
    startTailPat = pos()
    circle(-0.9 * x, 51)
    lt(113)
    circle(1.5 * x, 84)
    lt(45)
    circle(-0.5 * x, 9)
    seth(223 - 30)
    circle(-0.9 * x, 18)
    end_fill()

    # draw pattern on the tail
    pu()
    go(startTailPat)
    seth(57)
    fillcolor(TAIL_COLOR)
    begin_fill()
    pd()
    circle(-0.9 * x, 51)
    lt(113)
    circle(1.5 * x, 45)
    pu()
    seth(217)
    fd(0.45 * x)
    lt(100)
    fd(0.5 * x)
    rt(98)
    fd(0.5 * x)
    go(startTailPat)
    end_fill()

    ht()


pu()
goto(-100, 150)
pd()
drawKingDancing(50)
done()