import time
import interpolation
from easing_functions import *
import numpy as np
import matplotlib.pyplot as plt

# points are in the form of
# [time,volume,interpolation type]
# interpType: 0=Linear,1=Quadratic,2=Circular
points = [[0, 75, 0], [150, 80, 3], [180, 100, 2], [210, 75, -1]]


start_time = time.time()


def resetTime():
    global start_time
    start_time = time.time()


def getCurrentVol(currentTime):
    for i in range(len(points)):
        if points[i][2] == -1:
            resetTime()
            return points[i][1]

        leftPoint = points[i]
        rightPoint = points[i + 1]

        if leftPoint[0] <= currentTime and currentTime < rightPoint[0]:
            return interpolation.interp(
                leftPoint[0],
                leftPoint[1],
                rightPoint[0],
                rightPoint[1],
                currentTime,
                leftPoint[2],
            )


timeX = np.arange(0, 210, 0.2)
volY = timeX.copy()
for index, element in enumerate(timeX):
    volY[index] = getCurrentVol(element)
print(timeX)
plt.ylabel("Volume (%)")
plt.xlabel("Time (s)")
plt.title("Volume vs. Time")

plt.plot(timeX, volY)

controlPointsX = []
controlPointsY = []
for index in enumerate(points):
    controlPointsX.append(points[index][0])
    controlPointsY.append(points[index][1])


plt.scatter(controlPointsX, controlPointsY)
plt.savefig("figure.png")


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


while True:
    time_lapsed = time.time() - start_time
    print(time_lapsed, getCurrentVol(time_lapsed))
    time.sleep(0.1)
