import time
import utils
from easing_functions import *
import numpy as np
import matplotlib.pyplot as plt

# points are in the form of
# [time,volume,interpolation type]
# interpType: 0=Linear,1=Quadratic,2=Circular
controlPoints = [[0, 75, 0], [150, 80, 3], [180, 100, 2], [210, 75, -1]]
startTime = time.time()


while True:
    currentTime = time.time()
    timeElapsed = currentTime - startTime
    newVolume = utils.getVolume(timeElapsed)
    utils.setVolume(newVolume)
    time.sleep(1)
