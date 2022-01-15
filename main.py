import time
import utils
from easing_functions import *
import numpy as np
import controlPoints as ctrlPnts
import volumeController

# This file should be controlled by gui.py

play = True
controlPoints = ctrlPnts.points
startTime = time.time()
stepSize = 0.2
currentTime = 0


def query():
    global controlPoints
    global startTime
    global currentTime
    timeElapsed = currentTime - startTime
    leftTime = 0
    rightTime = 0
    leftVolume = 0
    rightVolume = 0
    interpType = 0
    leftColor = ""
    rightColor = ""
    maxTime = len(controlPoints)
    for i in range(maxTime):
        leftPoint = i
        rightPoint = i + 1
        if (
            timeElapsed >= controlPoints[leftPoint][0]
            and timeElapsed < controlPoints[rightPoint][0]
        ):
            interpType = controlPoints[leftPoint][2]
            leftTime = controlPoints[leftPoint][0]
            rightTime = controlPoints[rightPoint][0]
            leftColor = controlPoints[leftPoint][3]
            rightColor = controlPoints[rightPoint][3]
            leftVolume = controlPoints[leftPoint][1]
            rightVolume = controlPoints[rightPoint][1]
            break

    return [
        currentTime,
        timeElapsed,
        [leftTime, leftVolume, leftColor],
        [rightTime, rightVolume, rightColor],
    ]


def run():
    global startTime
    global currentTime
    startTime = time.time()
    currentTime = time.time()
    while True:
        currentTime = time.time()
        timeElapsed = currentTime - startTime
        if timeElapsed >= controlPoints[len(controlPoints) - 1][0]:
            restartTime()
            timeElapsed = currentTime - startTime
        newVolume = utils.getVolume(timeElapsed)
        volumeController.setVolume(newVolume)
        time.sleep(stepSize)


def restartTime():
    global startTime
    global currentTime
    timeElapsed = currentTime - startTime
    maxTime = controlPoints[len(controlPoints) - 1][0]
    print("delta Time is:", timeElapsed - maxTime, "\nstart time is:", startTime)
    startTime += maxTime


dataPlot = utils.init(controlPoints)
