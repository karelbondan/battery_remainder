# python script showing battery details
import psutil
import time
import subprocess
import playsound
import signal
import os


# function returning time in hh:mm:ss
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


# battery class
class Battery:
    def __init__(self, full='100', almost_full='80', low='15', critical='5'):
        self._full = full
        self._almost_full = almost_full
        self._low = low
        self._critical = critical
        self._config = {'full': self._full, 'almost_full': self._almost_full, 'low': self._low, 'critical': self._critical}

        try:
            file = open('config.json', 'r', encoding='utf-8')
            self._config = eval(file.read())
            print(self._config)
            self._full = self._config['full']
            self._almost_full = self._config['almost_full']
            self._low = self._config['low']
            self._critical = self._config['critical']
            file.close()
        except FileNotFoundError:
            file = open('config.json', 'w+', encoding='utf-8')
            file.write(f'{self._config}')
            file.close()

    @property
    def full(self):
        return self._full

    @property
    def almostFull(self):
        return self._almost_full

    @property
    def low(self):
        return self._low

    @property
    def critical(self):
        return self._critical

    @property
    def config(self):
        return self._config

    @full.setter
    def full(self, full):
        if full < 95 or full > 100:
            raise ValueError(f"Value must be between 95 and 100")
        elif full < int(self._almost_full)+1:
            raise SystemError(f"Value must be greater than {int(self._almost_full)+1}")
        else:
            self._full = int(full)
            self._config.update({'full': str(self._full)})
            self.saveFile()

    @almostFull.setter
    def almostFull(self, almost_full: int):
        if almost_full < 60 or almost_full > int(self._full)-1:
            raise ValueError(f"Value must be between 60 and {int(self._full)-1}")
        elif almost_full < int(self._low)+1:
            raise SystemError(f"Value must be greater than {int(self._low)+1}")
        else:
            self._almost_full = int(almost_full)
            self._config.update({'almost_full': str(self._almost_full)})
            self.saveFile()

    @low.setter
    def low(self, low: int):
        if low > int(self._almost_full)-1 or low < 10:
            raise ValueError(f"Value must be between 10 {int(self._almost_full)-1}")
        elif low < int(self._critical)+1:
            raise SystemError(f"Value must be greater than {int(self._critical)+1}")
        else:
            self._low = int(low)
            self._config.update({'low': str(self._low)})
            self.saveFile()

    @critical.setter
    def critical(self, critical: int):
        if critical > int(self._low)-1 or critical < 1:
            raise ValueError(f"Value must be between 1 and {int(self._low)-1}")
        else:
            self._critical = int(critical)
            self._config.update({'critical': str(self._critical)})
            self.saveFile()

    @config.setter
    def config(self, config: dict):
        file = open('config.json', 'w+', encoding='utf-8')
        file.write(f'{config}')
        file.close()

    def saveFile(self):
        file = open('config.json', 'w+', encoding='utf-8')
        file.write(f'{self._config}')
        file.close()

    def readFile(self):
        file = open('config.json', 'r', encoding='utf8')
        read = eval(file.read())
        file.close()
        return read

    def autoClose(self, dialog_address):
        while True:
            print(psutil.sensors_battery().power_plugged)
            if psutil.sensors_battery().power_plugged:
                dialog_address.send_signal(signal.CTRL_BREAK_EVENT)
                break
            if not psutil.pid_exists(dialog_address.pid):
                break
            time.sleep(1)

    def autoCloseFull(self, dialog_address):
        while True:
            print(psutil.sensors_battery().power_plugged)
            if not psutil.sensors_battery().power_plugged:
                dialog_address.send_signal(signal.CTRL_BREAK_EVENT)
                break
            if not psutil.pid_exists(dialog_address.pid):
                break
            time.sleep(1)