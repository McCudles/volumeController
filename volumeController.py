import time
import utils
from easing_functions import *
import numpy as np


# points are in the form of
# [time, volume, interpType]
# interpType: 0=Linear,1=SinInOut,2=CircularInOut,3=QuarticEaseInOut,4=ExponentialEaseInOut
# controlPoints = [[0, -10, 0], [2, -9, 3], [5, 0, 2], [7, -10, -1]]
controlPoints = [[0, -10, 1], [2, 0, 1], [4, -10, 1], [6, 0, -1]]
startTime = time.time()


def restartTime():
    global startTime
    startTime = time.time()


dataPlot = utils.init(controlPoints)

while True:
    currentTime = time.time()
    timeElapsed = currentTime - startTime
    if timeElapsed >= controlPoints[len(controlPoints) - 1][0]:
        restartTime()
    newVolume = utils.getVolume(timeElapsed)
    utils.setVolume(newVolume)
    time.sleep(0.1)
