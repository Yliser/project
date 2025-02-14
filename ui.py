import copy
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt6.QtGui import QPixmap, QIcon, QCursor
import threading

COMPUTER_COUNT = 7


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Window")
        self.setGeometry(200, 200, 300, 200)  # Position and size of the new window



class ComputerPushButton(QPushButton):
    def __init__(self, image_path, callback, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create a QPushButton with an image
        tmpQPixmap = QPixmap(image_path)

        # Resize the image to fit the button
        tmpQPixmap = tmpQPixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)

        # Set the button icon as the image
        self.setIcon(QIcon(tmpQPixmap))
        self.setIconSize(tmpQPixmap.size())

        # Set the button style to remove borders and make it look like an image
        self.setStyleSheet("border: none;")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Connect the button's clicked signal to the callback function
        self.clicked.connect(callback)



class ImageButtonWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize the window
        self.setWindowTitle('Enter name')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #fabcf9;")

        self.qvBoxLayout = QVBoxLayout()
        self.qhBoxLayout = QHBoxLayout()
        self.qvBoxLayout.addLayout(self.qhBoxLayout)
        self.qWidget = QWidget()

        def create_handler(_index):
            return lambda: self.on_button_click(_index)

        for i in range(COMPUTER_COUNT):
            self.add_image_button('comp.png', create_handler(i))

        self.qWidget.setLayout(self.qvBoxLayout)
        self.setCentralWidget(self.qWidget)

    def add_image_button(self, image_path, callback):
        computer_button = ComputerPushButton(image_path, callback, self)
        self.qhBoxLayout.addWidget(computer_button)

    def on_button_click(self, index):
        # Action to perform when any button is clicked
        print(f"Clicked #{index}")






if __name__ == '__main__':
    qApp = QApplication(sys.argv)

    # Create and show the window
    qWin = ImageButtonWindow()
    qWin.show()

    # Run the application
    sys.exit(qApp.exec())

    #########################################################
