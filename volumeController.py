import time
import interpolation

# points are in the form of
# [time,volume,interpolation type]
# interpType: 0=Linear,1=Quadratic,2=Circular
points = [[0, 65, 0], [5, 85, 0], [7, 30, 0], [10, 100, -1]]

start_time = time.time()


def resetTime():
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


for i in range(11):

    getCurrentVol(i)


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


# while True:
# time_lapsed = time.time() - start_time
# print(time_lapsed)
# time.sleep(1)
