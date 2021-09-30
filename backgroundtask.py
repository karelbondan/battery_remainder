from battery import *
import psutil
import playsound
import subprocess
import time
import os
import signal

# initialize battery instance
battery_obj = Battery()

# global variable to check if user has seen the dialog box and dismissed it
prompted = False

# global variable to check the current and previous battery percentage to reset the prompt
current = 0

# loop to check for battery
while True:
    # returns a tuple
    battery = psutil.sensors_battery()
    config = battery_obj.readFile()
    print(config)

    print("Battery percentage : ", battery.percent)
    print("Power plugged in : ", battery.power_plugged)

    # converting seconds to hh:mm:ss
    print("Battery left : ", convertTime(battery.secsleft))

    # reset the prompt
    if battery.percent != current:
        current = battery.percent
        prompted = False

    # if battery is 20 percent, not charging, and user hasn't been prompted yet then open battery low dialog box
    if battery.percent == eval(config['low']) and not battery.power_plugged and not prompted:
        dialog = subprocess.Popen('python notifmain.py', shell=True,
                                  creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        prompted = True
        # time.sleep(1)
        try:
            playsound.playsound("notification/battery_low.mp3")
        except playsound.PlaysoundException:
            pass
        print("battery 20")
        battery_obj.autoClose(dialog)

    # if battery is 10 percent, not charging, and user hasn't been prompted yet then open battery critical dialog box
    elif battery.percent == eval(config['critical']) and not battery.power_plugged and not prompted:
        dialog = subprocess.Popen('python notifmain.py', shell=True,
                                  creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        prompted = True
        # time.sleep(1)
        try:
            playsound.playsound("notification/battery_critical.mp3")
        except playsound.PlaysoundException:
            pass
        print("battery 10")
        battery_obj.autoClose(dialog)

    # if battery is 80 percent, charging, and user hasn't been prompted yet then open battery almost full dialog box
    elif battery.percent == eval(config['almost_full']) and battery.power_plugged and not prompted:
        dialog = subprocess.Popen('python notifmain.py', shell=True,
                                  creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        prompted = True
        # time.sleep(1)
        try:
            playsound.playsound("notification/battery_full.mp3")
        except playsound.PlaysoundException:
            pass
        print("battery 80")
        battery_obj.autoCloseFull(dialog)

    # if battery is 100 percent, charging, and user hasn't been prompted yet then open battery full dialog box
    elif battery.percent == eval(config['full']) and battery.power_plugged and not prompted:
        dialog = subprocess.Popen('python notifmain.py', shell=True,
                                  creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        prompted = True
        # time.sleep(1)
        try:
            playsound.playsound("notification/battery_full.mp3")
        except playsound.PlaysoundException:
            pass
        print("battery 100")
        battery_obj.autoCloseFull(dialog)

    # check every 15 seconds
    time.sleep(15)
