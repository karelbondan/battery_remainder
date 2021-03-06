import ctypes
import sys
import platform
import PyQt5
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QPainterPath)
from PySide2.QtWidgets import *

from notifgui import Ui_MainWindow
from notifguiconfig import *
from battery import *
import psutil

# telling Windows that this is a different process so the icon can be set
myappid = u'wolf.wolf.battery_reminder.1.0.0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(QMainWindow):
    # initial constructor
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.battery = psutil.sensors_battery()
        self._battery_obj = Battery()
        self._config = self._battery_obj.readFile()

        try:
            file = open('config.json', 'r+', encoding='utf-8')
            self._config = eval(file.read())
            file.close()
        except FileNotFoundError:
            file = open('config.json', 'w+', encoding='utf-8')
            file.write(f'{self._config}')
            file.close()

        def move_window(event):
            # moves the windows if the left mouse button is pressed
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.body.mouseMoveEvent = move_window

        if self.battery.percent == eval(self._config['low']):
            self.ui.percentage.setText(f"{self._config['low']}%")
            self.ui.todo.setText("Plug your charger in!")
            self.ui.info.setText("This message will automatically disappear after you plug your charger in")
            self.ui.body.setStyleSheet(
                'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(59, 150, 70, 255), stop:1 rgba(188, 182, 0, 255));'
                'border-radius: 30px;')

        elif self.battery.percent == eval(self._config['critical']):
            self.ui.percentage.setText(f"{self._config['critical']}%")
            self.ui.todo.setText("Plug your charger in immediately!")
            self.ui.info.setText("This message will disappear after you plug your charger in")
            self.ui.body.setStyleSheet(
                'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 0, 0, 255), stop:1 rgba(25, 10, 5, 255));'
                'border-radius: 30px;')
            self.ui.close.hide()

        elif self.battery.percent == eval(self._config['almost_full']):
            self.ui.percentage.setText(f"{self._config['almost_full']}%")
            self.ui.todo.setText("Unplug your charger!")
            self.ui.info.setText("This message will automatically disappear after you unplug your charger")
            self.ui.body.setStyleSheet(
                'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00568182 rgba(65, 146, 189, 255), stop:1 rgba(55, 85, 151, 255));'
                'border-radius: 30px;')

        elif self.battery.percent == eval(self._config['full']):
            self.ui.percentage.setText(f"{self._config['full']}%")
            self.ui.todo.setText("Unplug your charger immediately!")
            self.ui.info.setText("This message will disappear after you unplug your charger")
            self.ui.close.hide()

        # setting the app icon to show on the taskbar
        self.setWindowIcon(QtGui.QIcon('images/icon.ico'))

        # preventing the dialog box from moving into the background
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)

        # removing title bar
        UIFunctions.removeTitle(self)

        # showing the dialog box
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
