import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        #self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        #self.button = QtWidgets.QPushButton("Click me!")
        self.breakfastButton = QtWidgets.QPushButton("Breakfast")
        self.lunchButton = QtWidgets.QPushButton("Lunch")
        self.dinnerButton = QtWidgets.QPushButton("Dinner")
        self.snackButton = QtWidgets.QPushButton("Snack")
        self.dessertButton = QtWidgets.QPushButton("Dessert")

        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.breakfastButton)
        self.layout.addWidget(self.lunchButton)
        self.layout.addWidget(self.dinnerButton)
        self.layout.addWidget(self.snackButton)
        self.layout.addWidget(self.dessertButton)

        #self.layout.addWidget(self.button)

        #self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())