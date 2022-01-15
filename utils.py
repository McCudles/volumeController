from easing_functions import *
import numpy as np
import math

stepSize = 0.1
x = []
y = []


def init(controlPoints):
    maxTime = controlPoints[len(controlPoints) - 1][0]
    # len -1 because len() starts with 1 not 0
    timeArray = np.arange(0, maxTime, stepSize)
    global x
    global y
    x = timeArray.copy()
    y = timeArray.copy()
    for i in range(len(x)):
        y[i] = calculateVolume(x[i], controlPoints)
    return [x, y]


def calculateVolume(time, controlPoints):
    leftTime = 0
    rightTime = 0
    leftVolume = 0
    rightVolume = 0
    interpType = 0
    maxTime = len(controlPoints)
    for i in range(maxTime):
        leftPoint = i
        rightPoint = i + 1
        if time >= controlPoints[leftPoint][0] and time < controlPoints[rightPoint][0]:
            interpType = controlPoints[leftPoint][2]

            leftTime = controlPoints[leftPoint][0]
            rightTime = controlPoints[rightPoint][0]

            leftVolume = controlPoints[leftPoint][1]
            rightVolume = controlPoints[rightPoint][1]
            break
    return interp(leftTime, leftVolume, rightTime, rightVolume, time, interpType)


def getVolume(time):  # time = currentTime-startTime
    global y
    print("the time in getVolume is:", time)
    # index=(timeRoundedDown)/stepSize
    index = math.trunc(time / stepSize) - 1
    return round(y[index], 4)


def interp(leftTime, leftVolume, rightTime, rightVolume, currentTime, interpType):

    if interpType == 0:
        a = LinearInOut(leftVolume, rightVolume, rightTime - leftTime)
        return a(currentTime - leftTime)
    elif interpType == 1:
        a = SineEaseInOut(leftVolume, rightVolume, rightTime - leftTime)
        return a(currentTime - leftTime)
    elif interpType == 2:
        a = CircularEaseInOut(leftVolume, rightVolume, rightTime - leftTime)
        return a(currentTime - leftTime)
    elif interpType == 3:
        a = QuarticEaseInOut(leftVolume, rightVolume, rightTime - leftTime)
        return a(currentTime - leftTime)
    elif interpType == 4:
        a = ExponentialEaseInOut(leftVolume, rightVolume, rightTime - leftTime)
        return a(currentTime - leftTime)
