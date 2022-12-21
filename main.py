from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys


class Window(QMainWindow):

   def __init__(self):
      super().__init__()
      self.setWindowTitle("Камень ножницы бумага")
      self.setGeometry(100, 100, 320, 400)
      self.UiComponents()
      self.show()
   def UiComponents(self):
      self.counter = -1
      self.choice = 0
      head = QLabel("Камень ножницы бумага", self)
      head.setGeometry(20, 10, 280, 60)
      font = QFont('Times', 15)
      head.setFont(font)
      head.setAlignment(Qt.AlignCenter)
      self.vs = QLabel("vs", self)
      self.vs.setGeometry(150, 110, 30, 50)
      font.setUnderline(False)
      font.setItalic(False)
      self.vs.setFont(font)
      self.user = QLabel("Вы", self)
      self.user.setGeometry(50, 100, 70, 70)
      self.user.setAlignment(Qt.AlignCenter)
      self.computer = QLabel("Комухтер", self)
      self.computer.setGeometry(200, 100, 70, 70)
      self.computer.setAlignment(Qt.AlignCenter)
      self.result = QLabel(self)
      self.result.setGeometry(25, 200, 270, 50)
      self.result.setFont(QFont('Times', 14))
      self.result.setAlignment(Qt.AlignCenter)
      self.rock = QPushButton("Камень", self)
      self.rock.setGeometry(30, 270, 80, 35)
      self.paper = QPushButton("Бумага", self)
      self.paper.setGeometry(120, 270, 80, 35)
      self.scissor = QPushButton("Ножницы", self)
      self.scissor.setGeometry(210, 270, 80, 35)
      self.rock.clicked.connect(self.rock_action)
      self.paper.clicked.connect(self.paper_action)
      self.scissor.clicked.connect(self.scissor_action)
      game_reset = QPushButton("перезагрузить", self)
      game_reset.setGeometry(100, 320, 120, 50)
      game_reset.clicked.connect(self.reset_action)
      timer = QTimer(self)
      timer.timeout.connect(self.showTime)
      timer.start(1000)

   def showTime(self):
      if self.counter == -1:
         pass
      else:
         self.computer.setText(str(self.counter))
         if self.counter == 0:
            self.comp_choice = random.randint(1, 3)
            if self.comp_choice == 1:
               self.computer.setStyleSheet(
                  "border-image : url(rock.png);")
            elif self.comp_choice == 2:
               self.computer.setStyleSheet(
                  "border-image : url(Paper.png);")
            else:
               self.computer.setStyleSheet(
                  "border-image : url(scissor.png);")
            self.who_won()
         self.counter -= 1

   def rock_action(self):
      self.choice = 1
      self.user.setStyleSheet("border-image : url(rock.png);")
      self.counter = 3
      self.rock.setDisabled(True)
      self.paper.setDisabled(True)
      self.scissor.setDisabled(True)

   def paper_action(self):
      self.choice = 2
      self.user.setStyleSheet("border-image : url(Paper.png);")
      self.counter = 3
      self.rock.setDisabled(True)
      self.paper.setDisabled(True)
      self.scissor.setDisabled(True)

   def scissor_action(self):
      self.choice = 3
      self.user.setStyleSheet("border-image : url(scissor.png);")
      self.counter = 3
      self.rock.setDisabled(True)
      self.paper.setDisabled(True)
      self.scissor.setDisabled(True)

   def reset_action(self):
      self.result.setText("")
      self.counter = -1
      self.rock.setEnabled(True)
      self.paper.setEnabled(True)
      self.scissor.setEnabled(True)
      self.user.setStyleSheet("border-image : null;")
      self.computer.setStyleSheet("border-image : null;")

   def who_won(self):
      if self.choice == self.comp_choice:
         self.result.setText("Ничья")
      else:
         if self.choice == 1:
            if self.comp_choice == 2:
               self.result.setText("Победа компьютера")
            else:
               self.result.setText("Победа юзера")
         elif self.choice == 2:
            if self.comp_choice == 3:
               self.result.setText("Победа компьютера")
            else:
               self.result.setText("Победа юзера")
         elif self.choice == 3:
            if self.comp_choice == 1:
               self.result.setText("Победа компьютера")
            else:
               self.result.setText("Победа юзера")



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
