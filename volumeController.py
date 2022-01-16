# windows only
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

try:
    devices = AudioUtilities.GetSpeakers()
except:
    print("No audio device detected, plug one in")
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()


def setVolume(vol):
    global volume
    print("The volume is set to:", vol)
    volume.SetMasterVolumeLevelScalar(vol / 100, None)
