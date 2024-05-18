import win32api
import os
import keyboard
import screen_brightness_control as sbc
from time import sleep
from get_uid import  get_power_schemes

current_brightness = sbc.get_brightness()

complete_heating_off = True # this tells the script if it needs to turn the heat off completely, it will affect the performance tho.
try:
    all_power_schemes = get_power_schemes()
    for i in range(len(all_power_schemes)):

        if(all_power_schemes[i]["name"] == "supercool"):
            cool_mode_guid = all_power_schemes[i]["guid"]
        elif(all_power_schemes[i]["name"] == 'High Performance'):
            high_performance_mode_guid = all_power_schemes[i]["guid"]
        elif(all_power_schemes[i]["name"] == 'Balanced'):
            balanced = all_power_schemes[i]["guid"]

except Exception as e:

    print(f"an unexpected error occured: {e}, put this issue on pc-cooler or see if there's any solution already, follow the link here. : https://github.com/snehccurry/PC-cooler/issues ")
    exit()





def rest():
    global current_brightness
    #print(current_brightness)
    os.system(f"cmd /C  powercfg /S {cool_mode_guid}") #coolmode
    #print("on a cooldown")
    #print("switched to cool mode")
    #sbc.set_brightness(current_brightness, display=0)
    #print("changed current_brightness for cool mode")
    sleep(0.5)
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
            os.system(f"cmd /C powercfg /S {high_performance_mode_guid}")         #high perf.
            #print("switched to high performance")
            #sbc.set_brightness(current_brightness, display=0)
            #print("Changed current_brightness for highperformance")
            sleep(2)
            #sleep(5) on click

        elif (keyboard.read_key!=None and complete_heating_off==False):
            #print(keyboard.read_key())
            os.system(f"cmd /C powercfg /S {balanced}")  # high perf.
            #print("turned on balanced")
        else:
            rest()
    except Exception as e:
        print("error occured",e)
        break
        #sleep(1)

















