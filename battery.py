# python script showing battery details
import psutil
import time
import subprocess
import playsound
import signal


# function returning time in hh:mm:ss
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


# global variable to check if user has seen the dialog box and dismissed it
prompted = False

# global variable to check the current and previous battery percentage to reset the prompt
current = 0

def autoClose(dialog_address):
    while True:
        print(psutil.sensors_battery().power_plugged)
        if psutil.sensors_battery().power_plugged:
            dialog_address.send_signal(signal.CTRL_BREAK_EVENT)
            break
        if not psutil.pid_exists(dialog_address.pid):
            break
        time.sleep(1)

def autoCloseFull(dialog_address):
    while True:
        print(psutil.sensors_battery().power_plugged)
        if not psutil.sensors_battery().power_plugged:
            dialog_address.send_signal(signal.CTRL_BREAK_EVENT)
            break
        if not psutil.pid_exists(dialog_address.pid):
            break
        time.sleep(1)

# loop to check for battery
while True:
    # returns a tuple
    battery = psutil.sensors_battery()

    print("Battery percentage : ", battery.percent)
    print("Power plugged in : ", battery.power_plugged)

    # converting seconds to hh:mm:ss
    print("Battery left : ", convertTime(battery.secsleft))

    # reset the prompt
    if battery.percent != current:
        current = battery.percent
        prompted = False

    # if battery is 20 percent, not charging, and user hasn't been prompted yet then open battery low dialog box
    if battery.percent == 20 and not battery.power_plugged and not prompted:
        dialog = subprocess.Popen('python main.py', shell=True,
                                  creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        prompted = True
        time.sleep(1)
        playsound.playsound("D:/Projects/Battery_Remainder/notification/battery_low.wav")
        print("battery 20")
        autoClose(dialog)

    # if battery is 10 percent, not charging, and user hasn't been prompted yet then open battery critical dialog box
    elif battery.percent == 10 and not battery.power_plugged and not prompted:
        dialog = subprocess.Popen('python main.py', shell=True,
                                  creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        prompted = True
        time.sleep(1)
        playsound.playsound("D:/Projects/Battery_Remainder/notification/battery_critical.wav")
        print("battery 10")
        autoClose(dialog)

    # if battery is 80 percent, charging, and user hasn't been prompted yet then open battery almost full dialog box
    elif battery.percent == 80 and battery.power_plugged and not prompted:
        dialog = subprocess.Popen('python main.py', shell=True,
                                  creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        prompted = True
        time.sleep(1)
        playsound.playsound("D:/Projects/Battery_Remainder/notification/battery_full.wav")
        print("battery 80")
        autoCloseFull(dialog)

    # if battery is 100 percent, charging, and user hasn't been prompted yet then open battery full dialog box
    elif battery.percent == 100 and battery.power_plugged and not prompted:
        dialog = subprocess.Popen('python main.py', shell=True,
                                  creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        prompted = True
        time.sleep(1)
        playsound.playsound("D:/Projects/Battery_Remainder/notification/battery_full.wav")
        print("battery 100")
        autoCloseFull(dialog)

    # check every 15 seconds
    time.sleep(15)
