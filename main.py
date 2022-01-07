import time
import utils
from easing_functions import *
import numpy as np
import controlPoints as ctrlPnts
import volumeController


controlPoints = ctrlPnts.points
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
    volumeController.setVolume(newVolume)
    time.sleep(0.05)
