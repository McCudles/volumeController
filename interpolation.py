from easing_functions import *


def interp(leftTime, leftVol, rightTime, rightVol, currentTime, interpType):

    print("Time:", currentTime)
    print("Left:", leftTime, "Volume:", leftVol)
    print("Right:", rightTime, "Volume:", rightVol)

    a = LinearInOut(leftVol, rightVol, rightTime - leftTime)
    print(a(currentTime - leftTime))
    return a(currentTime - leftTime)
