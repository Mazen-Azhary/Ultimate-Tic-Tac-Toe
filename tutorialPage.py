from PyQt5.QtWidgets import QStackedWidget,QApplication, QWidget,QGridLayout,QPushButton,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
from largerBoard import LargerBoard
class tutorialPage(QWidget):
    def __init__(self):
        super().__init__()
        self.window = uic.loadUi("uiComp/tutorialUI.ui")
        # self.window.playTurnLabel.setFixedSize(300, 300)
        self.button = self.window.backToGameButton
        x1 = self.window.playTurnLabel.x() 
        y1 = self.window.playTurnLabel.y() 
        x2 = self.window.gameWinLabel.x() 
        y2 = self.window.gameWinLabel.y() 
        self.window.playTurnLabel.setGeometry(x1, y1, 400, 400)
        self.window.playTurnLabel.setScaledContents(True) 
        # self.window.gameWinLabel.setFixedSize(500, 400)  
        self.window.gameWinLabel.setGeometry(x2+155, y2, 500, 400)
        self.window.gameWinLabel.setScaledContents(True) 
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("uiComp/Ultimate_Tic_Tac_Toe.png"))
    window = tutorialPage()
    window.setWindowTitle("Tutorial - Ultimate Tic Tac Toe by Mazen Azhary")
    window.setFixedHeight(1000)
    window.setFixedWidth(1000)
    window.window.show()
    sys.exit(app.exec_())
        