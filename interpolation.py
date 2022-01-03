from easing_functions import *


def interp(leftTime, leftVol, rightTime, rightVol, currentTime, interpType):

    if interpType == 0:
        a = LinearInOut(leftVol, rightVol, rightTime - leftTime)
        return a(currentTime - leftTime)
    elif interpType == 1:
        a = SineEaseInOut(leftVol, rightVol, rightTime - leftTime)
        return a(currentTime - leftTime)
    elif interpType == 2:
        a = CircularEaseInOut(leftVol, rightVol, rightTime - leftTime)
        return a(currentTime - leftTime)
    elif interpType == 3:
        a = QuarticEaseInOut(leftVol, rightVol, rightTime - leftTime)
        return a(currentTime - leftTime)
    elif interpType == 4:
        a = ExponentialEaseInOut(leftVol, rightVol, rightTime - leftTime)
        return a(currentTime - leftTime)
