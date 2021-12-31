from ctypes import cast, POINTER
from datetime import datetime
import time
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.SetMasterVolumeLevel(-25.0, None)


# notes about the timer at 9R
# 2.5 mins during green timer vol=80%
# 0.5 mins yellow timer vol=95%
# 0.5 mins red timer vol=70%
time_diff = 0
startTime = datetime.now().strftime("%H:%M:%S")
print(startTime)
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("current time =", current_time)
    time.sleep(1.0)
    time_diff = current_time - startTime
    print(time_diff)
