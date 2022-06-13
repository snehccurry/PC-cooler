import win32api
import os
from pynput import keyboard
import screen_brightness_control as sbc
from time import sleep

current_brightness=sbc.get_brightness()

def rest():
    global current_brightness
    print(current_brightness)
    os.system('cmd /C "powercfg /S 8ab6f04d-cba8-4fcf-8dbb-751546bb7f2e"') #coolmode
    print("switched to cool mode")
    sbc.set_brightness(current_brightness, display=0)
    print("changed current_brightness for cool mode")
    sleep(2.5)
    #current_brightness=sbc.get_brightness 
    #os.system('cmd /C "powercfg /S 125a7300-96d9-4d55-901e-d0d12f0e4f6d"') #cool balanced perf.
    #sleep(2)
    #sbc.set_brightness(current_brightness=sbc.get_brightness, display=0)

savedpos = win32api.GetCursorPos()

while(True):
    try:

        curpos = win32api.GetCursorPos()
        if savedpos != curpos:
            savedpos = curpos
            current_brightness=sbc.get_brightness() 
            os.system('cmd /C "powercfg /S 637d3e2d-0c49-46e5-be77-1a408d584551"')         #high perf.
            print("switched to high performance")
            sbc.set_brightness(current_brightness, display=0)
            print("Changed current_brightness for highperformance")
            sleep(5)
        else:
            rest()
    except:
        pass
        #sleep(1)




















'''def on_press(key):
        try:
            os.system('cmd /C "powercfg /S e3b323ca-f4c7-439d-b77e-fbd97baf2ca1"') #high perf.
            sleep(0.5)
            current_brightness=sbc.get_brightness
            sbc.set_brightness(current_brightness=sbc.get_brightness, display=0)

        except AttributeError:
            os.system('cmd /C "powercfg /S e3b323ca-f4c7-439d-b77e-fbd97baf2ca1"') #high perf
            sbc.set_brightness(current_brightness=sbc.get_brightness, display=0)

            sleep(0.5)
        rest()
'''    


