import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QTimer

class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 48px; background-color: black; color: white;")
        self.setCentralWidget(self.label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
