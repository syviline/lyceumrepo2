import sys
import random

import PyQt5
from PyQt5.QtGui import QPainter, QColor
from PyQt5.Qt import QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QMainWindow
from PyQt5 import uic
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.circles = []
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        if self.do_paint:
            qp.setPen(PyQt5.QtCore.Qt.NoPen)
            radius = random.randint(10, 100)
            self.circles.append([QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), QPoint(random.randint(radius, self.width() - radius), random.randint(radius, self.height() - radius)), radius, radius])
            for i in self.circles:
                qp.setBrush(i[0])
                qp.drawEllipse(*i[1:])
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())