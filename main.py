import sys
import os.path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


class App(QWidget):

  def __init__(self):
    super().__init__()
    self.title = "Reminder"
    self.left = 10
    self.top = 10
    self.width = 640
    self.height = 480
    self.initUI()

  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    gridLayout = QGridLayout()
    self.setLayout(gridLayout)

    self.remind = self.textReading()
    self.label = QLabel(self)
    self.label.setText(self.remind)
    self.label.resize(200, 180)
    self.label.setStyleSheet(
      "color: red;"
      "margin-left: 10px;"
    )

    self.textbox = QLineEdit(self)
    self.textbox.move(20, 180)
    self.textbox.resize(280, 40)

    self.writeButton = QPushButton('Hatırlatıcı ekle', self)
    self.writeButton.move(20, 230)

    self.writeButton.clicked.connect(self.writeRemind)
    self.show()

  def textReading(self):
    if os.path.exists('remind.txt'):

      f = open("remind.txt", "r")
      if f.mode == 'r':
        remind = f.read()
        f.close()
        return remind

    return "Yapılacak iş yok"

  def writeRemind(self):
    textBoxValue = self.textbox.text()

    f = open("remind.txt", "a")
    f.write(textBoxValue + "\n")
    f.close()



if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = App()
  sys.exit(app.exec_())