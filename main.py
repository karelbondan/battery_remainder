import ctypes
import sys
import platform
import PyQt5
from PyQt5.QtWidgets import qApp
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QPainterPath)
from PySide2.QtWidgets import *

from configgui import Ui_MainWindow
from configguiconfig import *
from battery import *
import psutil
import atexit
import pygetwindow

myappid = u'wolf.wolf.battery_reminder.1.0.0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class MainWindow(QMainWindow):
    tray_icon = None

    # initial constructor
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._exit = False
        self._battery = Battery()
        self._config = self._battery.readFile()
        self.ui.config.setCurrentWidget(self.ui.page_fullycharged)
        self.ui.navbar.setCurrentWidget(self.ui.page_nextonly)
        self._info = QMessageBox()
        self._info.setWindowTitle("Battery Remainder")
        self._info.setWindowIcon(QtGui.QIcon('images/icon.ico'))

        # updating the percentage value set by user
        def update(self, state, value: int):
            try:
                value = int(value)
            except ValueError:
                self._info.setText("Value must be in integer")
                self._info.show()

            if state == "fully_charged":
                try:
                    self._battery.full = value
                except ValueError:
                    self._info.setText("Value must be between 95 and 100")
                    self._info.show()
                except SystemError:
                    self._info.setText(f"Value must be greater than {self._battery.almostFull}")
                    self._info.show()
                print(self._battery.full)

            elif state == "nearly_charged":
                try:
                    self._battery.almostFull = value
                except ValueError:
                    self._info.setText(f"Value must be between 60 and {int(self._battery.full)-1}")
                    self._info.show()
                except SystemError:
                    self._info.setText(f"Value must be greater than {self._battery.low}")
                    self._info.show()
                print(self._battery.almostFull)

            elif state == "low":
                try:
                    self._battery.low = value
                except ValueError:
                    self._info.setText(f"Value must be between 10 and {int(self._battery.almostFull)-1}")
                    self._info.show()
                except SystemError:
                    self._info.setText(f"Value must be greater than {self._battery.critical}")
                    self._info.show()
                print(self._battery.low)

            elif state == "critical":
                try:
                    self._battery.critical = value
                except ValueError:
                    self._info.setText(f"Value must be between 1 and {int(self._battery.low)-1}")
                    self._info.show()
                print(self._battery.critical)

        def refresh(self):
            self._config = self._battery.readFile()
            self.ui.fully_charged_edit.setText(str(self._config['full']))
            self.ui.nearlycharged_edit.setText(str(self._config['almost_full']))
            self.ui.low_edit.setText(str(self._config['low']))
            self.ui.criticallow_edit.setText(str(self._config['critical']))

        # handling button click if user wants to go to the next page
        def next(self):
            if self.ui.config.currentWidget() is self.ui.page_fullycharged:
                self.ui.config.setCurrentWidget(self.ui.page_nearlycharged)
            elif self.ui.config.currentWidget() is self.ui.page_nearlycharged:
                self.ui.config.setCurrentWidget(self.ui.page_low)
            elif self.ui.config.currentWidget() is self.ui.page_low:
                self.ui.config.setCurrentWidget(self.ui.page_criticallow)
            navbar(self)

        # handling button click if user wants to go to the previous page
        def previous(self):
            if self.ui.config.currentWidget() is self.ui.page_nearlycharged:
                self.ui.config.setCurrentWidget(self.ui.page_fullycharged)
            elif self.ui.config.currentWidget() is self.ui.page_low:
                self.ui.config.setCurrentWidget(self.ui.page_nearlycharged)
            elif self.ui.config.currentWidget() is self.ui.page_criticallow:
                self.ui.config.setCurrentWidget(self.ui.page_low)
            navbar(self)

        # deciding what navigation should be displayed to the user
        def navbar(self):
            if self.ui.config.currentWidget() is self.ui.page_fullycharged:
                self.ui.navbar.setCurrentWidget(self.ui.page_nextonly)
            elif (self.ui.config.currentWidget() is self.ui.page_nearlycharged or
                  self.ui.config.currentWidget() is self.ui.page_low):
                self.ui.navbar.setCurrentWidget(self.ui.page_nextprevious)
            elif self.ui.config.currentWidget() is self.ui.page_criticallow:
                self.ui.navbar.setCurrentWidget(self.ui.page_previousonly)
            refresh(self)

        # deciding whether to quit or to minimize the app to tray
        def exitProgram(self, state: bool):
            self._exit = state
            self.close()

        # method to summon the background process
        def background():
            bg = subprocess.Popen('python backgroundtask.py', shell=True,
                                      creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            return bg

        # method to kill the background process when the main GUI is exited
        def kill_background(child_pid):
            proc_pid = child_pid.pid
            if proc_pid is None:
                pass
            else:
                child_pid.send_signal(signal.CTRL_BREAK_EVENT)

        # move event to handle the window-dragging
        def move_window(event):
            # moves the windows if the left mouse button is pressed
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.body.mouseMoveEvent = move_window

        # initializing button clicks
        self.ui.button_check_fullcharge.clicked.connect(
            lambda: update(self, "fully_charged", self.ui.fully_charged_edit.text()))
        self.ui.button_check_nearlycharged.clicked.connect(
            lambda: update(self, "nearly_charged", self.ui.nearlycharged_edit.text()))
        self.ui.button_check_low.clicked.connect(lambda: update(self, "low", self.ui.low_edit.text()))
        self.ui.button_check_criticallow.clicked.connect(
            lambda: update(self, "critical", self.ui.criticallow_edit.text()))
        self.ui.next_one.clicked.connect(lambda: next(self))
        self.ui.next_two.clicked.connect(lambda: next(self))
        self.ui.previous_two.clicked.connect(lambda: previous(self))
        self.ui.previous_three.clicked.connect(lambda: previous(self))

        # setting the app icon to show on the taskbar
        self.setWindowIcon(QtGui.QIcon('images/icon.ico'))

        # initializing QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon('images/icon.ico'))
        self.quit_action = QAction("Exit", self)
        self.quit_action.triggered.connect(qApp.quit)
        self.tray_menu = QMenu()
        self.tray_menu.addAction(self.quit_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()
        self.tray_icon.setToolTip("Wolf - Battery Remainder")
        self.tray_icon.activated.connect(self.icon_click)

        # setting respective text bars based on each values
        refresh(self)

        # removing title bar
        UIFunctions.removeTitle(self)

        # closes the app when the close button is pressed
        self.ui.close.clicked.connect(lambda: exitProgram(self, True))

        # minimizes the app to system tray when the minimize button is pressed
        self.ui.minimize.clicked.connect(lambda: exitProgram(self, False))

        # summoning the background task
        bg_task = background()

        # killing the background task when exit
        atexit.register(kill_background, bg_task)

        # showing the dialog box
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def closeEvent(self, event):
        if not self._exit:
            event.ignore()
            self.hide()
        else:
            self.close()
            
    def setToFocus(self):
        wolf = pygetwindow.getWindowsWithTitle('Wolf - Battery Remainder')[0]
        if wolf.isMinimized:
            wolf.restore()
        if not wolf.isActive:
            wolf.minimize()
            wolf.restore()
        else:
            pass

    def icon_click(self, reason):
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            self.show()
            self.setToFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Wolf - Battery Remainder")
    sys.exit(app.exec_())
