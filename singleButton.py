
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
from PyQt5.QtCore import pyqtSignal
import sys


class SingleButton(QPushButton):
    clickedSignal = pyqtSignal(str,str,str) #buttonPosInSingleBoard,boardPosition,player
    player = "X" #this is a static var to be shared among the 81 buttons 
    def __init__(self,Name="btn00",position="00"): #btn00 in position 00 means it is top left button in top left singleBoard
        super().__init__()
        self.position = position
        self.buttonName = Name
        self.clicked.connect(self.on_button_click)
        self.clickable = True
        # self.setFixedHeight(60)
        # self.setFixedWidth(60)
        styleSh = """
        QPushButton {
        width:30%;
        height:30%;
        background-color: rgba(255,255,255,0.7);
        border: 1px solid black;
        border-radius: 5px;
        font-size: 30px;
        font-weight: bold;
        }
        QPushButton:hover {
        background-color: rgba(155,155,155,0.7);
            }
            """
        self.setStyleSheet(styleSh)  
    def on_button_click(self):
        if self.clickable == False or self.text() != "":
            return -1    
        self.clickable = False
        if SingleButton.player == "X":
            self.setText("X")
        else:
            self.setText("O")
        styleSh = """
        QPushButton {
        width:30%;
        height:30%;
        background-color: rgba(170,170,170,0.7);
        border: 1px solid black;
        border-radius: 5px;
        font-size: 30px;
       }
        QPushButton:hover {
        background-color: rgba(155,155,155,0.7);
            }
            """
        self.setStyleSheet(styleSh)
        # return self.position


        self.clickedSignal.emit(self.buttonName, self.position, SingleButton.player)  # Emit the signal with the position
        self.togglePlayer()  # Toggle the player after a succesful click
    def togglePlayer(self):
        if SingleButton.player == "X":
            SingleButton.player = "O"
        else:
            SingleButton.player = "X"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SingleButton("btn00", "01")
    window.setFixedHeight(100)
    window.setFixedWidth(100)
    window.show()
    sys.exit(app.exec_())