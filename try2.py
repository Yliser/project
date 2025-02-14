import sys
import psutil  # Import psutil to get CPU usage
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt6.QtGui import QPixmap, QIcon, QCursor

COMPUTER_COUNT = 7


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Window")
        self.setGeometry(200, 200, 800, 500)
        self.setStyleSheet("background-color: #f0f0f0;")

        layout = QVBoxLayout()
        label = QLabel("This is a new window", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)


class ComputerPushButton(QPushButton):
    def __init__(self, image_path, callback, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tmpQPixmap = QPixmap(image_path).scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)

        self.setIcon(QIcon(tmpQPixmap))
        self.setIconSize(tmpQPixmap.size())
        self.setStyleSheet("border: none;")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.clicked.connect(callback)


class ImageButtonWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Enter name')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #fabcf9;")

        self.qvBoxLayout = QVBoxLayout()
        self.qhBoxLayout = QHBoxLayout()
        self.qvBoxLayout.addLayout(self.qhBoxLayout)
        self.qWidget = QWidget()

        self.windows = []  # Store references to prevent garbage collection
        self.computer_buttons=[]

        def create_handler(_index):
            return lambda: self.on_button_click(_index)

        for i in range(COMPUTER_COUNT):
            self.add_image_button('comp.png', create_handler(i))

        self.qWidget.setLayout(self.qvBoxLayout)
        self.setCentralWidget(self.qWidget)

        # ✅ Timer to print CPU usage every 3 seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.print_cpu_usage)
        self.timer.start(3000)  # 3 seconds interval

    def add_image_button(self, image_path, callback):
        computer_button = ComputerPushButton(image_path, callback, self)
        self.computer_buttons.append(computer_button)
        self.qhBoxLayout.addWidget(computer_button)


    def on_button_click(self, index):
        print(f"Clicked #{index}")
        new_window = SecondWindow()
        self.windows.append(new_window)  # Keep reference to avoid garbage collection
        new_window.show()

    def print_cpu_usage(self):
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage
        print(f"CPU Usage: {cpu_usage}%")  # Print every 3 sec


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    qWin = ImageButtonWindow()
    qWin.show()
    sys.exit(qApp.exec())
