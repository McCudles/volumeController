import time
import utils
from easing_functions import *
import numpy as np
import controlPoints as ctrlPnts
import volumeController

play = True
controlPoints = ctrlPnts.points
startTime = time.time()


def run():
    while True:
        currentTime = time.time()
        timeElapsed = currentTime - startTime
        if timeElapsed >= controlPoints[len(controlPoints) - 1][0]:
            restartTime()
        newVolume = utils.getVolume(timeElapsed)
        volumeController.setVolume(newVolume)
        time.sleep(0.05)


def init():
    global play
    restartTime()
    play = not (play)
    print(time.time())
    return print(f"{play}")


def restartTime():
    global startTime
    startTime = time.time()


dataPlot = utils.init(controlPoints)
