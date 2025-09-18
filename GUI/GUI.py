import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("The orca app")
#         self.setGeometry(100, 100, 400, 300)
#         self.setWindowIcon(QIcon("orca.png"))
        

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#      main()



#LABELS
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("The orca app")
#         self.setGeometry(100, 100, 400, 300)
#         self.setWindowIcon(QIcon("orca.png"))

#         layout = QVBoxLayout()

#         label1 = QLabel("ORCA")
#         label1.setStyleSheet("color: blue; font-size: 20px; background-color: lightgray;")
#         label1.setAlignment(Qt.AlignCenter)
#         layout.addWidget(label1)

#         label2 = QLabel("VS")
#         label2.setStyleSheet("color: red; font-size: 16px; background-color: lightblue;")
#         label2.setAlignment(Qt.AlignCenter)
#         layout.addWidget(label2)

#         label3 = QLabel("PYTHON")
#         label3.setStyleSheet("color: green; font-size: 18px; background-color: lightgreen;")
#         label3.setAlignment(Qt.AlignCenter)
#         layout.addWidget(label3)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#      main()


# IMAGES
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("The orca app")
#         self.setGeometry(100, 100, 400, 300)
#         self.setWindowIcon(QIcon("orca.png"))

#         layout = QVBoxLayout()

#         image_label = QLabel()
#         pixmap = QPixmap("orca.png")
#         image_label.setPixmap(pixmap)
#         image_label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(image_label)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#      main()



# BUTTONS
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.button = QPushButton("Click me!", self)
#         self.initUI()

#     def initUI(self):
#         self.button.setGeometry(150, 200, 200, 100)
#         self.button.setStyleSheet("font-size: 30px;")
#         self.button.clicked.connect(self.on_click)

#     def on_click(self):
#         print("Button clicked!")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())



# #CHECKOBX
# from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.checkbox = QCheckBox("Do you like food?", self)
#         self.initUI()

#     def initUI(self):
#         self.checkbox.setGeometry(10, 0, 500, 100)
#         self.checkbox.setStyleSheet("font-size: 50px;"
#                                                             "font-family: Arial;")
#         self.checkbox.stateChanged.connect(self.checkbox_changed)

#     def checkbox_changed(self, state):
#         if state == Qt.Checked:
#             print("Are you a human")
#         else:
#             print("You are no longer a human ")

# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    window = MainWindow()
#    window.show()
#    sys.exit(app.exec_())




#RADIO BUTTONS
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.radio1 = QRadioButton("Visa", self)
#         self.radio2 = QRadioButton("Mastercard", self)
#         self.radio3 = QRadioButton("Gift Card", self)
#         self.radio4 = QRadioButton("In-Store", self)
#         self.radio5 = QRadioButton("Online", self)
#         self.button_group1 = QButtonGroup(self)
#         self.button_group2 = QButtonGroup(self)
#         self.initUI()

#     def initUI(self):
#         self.radio1.setGeometry(0, 0, 300, 50)
#         self.radio2.setGeometry(0, 50, 300, 50)
#         self.radio3.setGeometry(0, 100, 300, 50)
#         self.radio4.setGeometry(0, 150, 300, 50)
#         self.radio5.setGeometry(0, 200, 300, 50)

#         self.setStyleSheet("QRadioButton{"
#                                          "font-size: 40px;"
#                                          "font-family: Arial;"
#                                          "padding: 10px;"
#                                          "}")

#         self.button_group1.addButton(self.radio1)
#         self.button_group1.addButton(self.radio2)
#         self.button_group1.addButton(self.radio3)
#         self.button_group2.addButton(self.radio4)
#         self.button_group2.addButton(self.radio5)

#         self.radio1.toggled.connect(self.radio_button_changed)
#         self.radio2.toggled.connect(self.radio_button_changed)
#         self.radio3.toggled.connect(self.radio_button_changed)
#         self.radio4.toggled.connect(self.radio_button_changed)
#         self.radio5.toggled.connect(self.radio_button_changed)

#     def radio_button_changed(self):
#         radio_button = self.sender()
#         if radio_button.isChecked():
#             print(f"{radio_button.text()} is selected")

# if __name__ == '__main__':
#   app = QApplication(sys.argv)
#   window = MainWindow()
#   window.show()
#   sys.exit(app.exec_())



#LINE EDIT
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.line_edit = QLineEdit(self)
#         self.button = QPushButton("Submit", self)
#         self.initUI()

#     def initUI(self):
#         self.line_edit.setGeometry(10, 10, 200, 40)
#         self.button.setGeometry(210, 10, 100, 40)
#         self.line_edit.setStyleSheet("font-size: 25px;"
#                                                          "font-family: Arial")
#         self.button.setStyleSheet("font-size: 25px;"
#                                                       "font-family: Arial")
#         self.line_edit.setPlaceholderText("Enter your name")

#         self.button.clicked.connect(self.submit)

#     def submit(self):
#         text = self.line_edit.text()
#         print(f"Hello {text}")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
