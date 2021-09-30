from PySide2.QtWidgets import QGraphicsDropShadowEffect

from notifmain import *

# the function to drag the window around when pressed on the title bar, and to make the
# minimize and close button works.
class UIFunctions(MainWindow):
    def removeTitle(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        self.ui.body.setGraphicsEffect(self.shadow)



