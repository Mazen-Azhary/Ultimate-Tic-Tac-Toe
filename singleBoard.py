from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QGridLayout
from PyQt5.QtCore import pyqtSignal
import sys

class SingleButton(QPushButton):
    clickedSignal = pyqtSignal(str, str)  # class attribute, correct PyQt usage
    def __init__(self,Name="btn00",position="00",parent=None):
        super().__init__()
        self.position = position
        self.buttonName = Name
        self.clicked.connect(lambda: self.on_button_click())  # Fix: always call with no bool argument
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
    def on_button_click(self,player="X"):
        if self.clickable == False or self.text() != "":
            return -1    
        self.clickable = False
        if player == "X":
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
        self.clickedSignal.emit(self.position,player)  # Emit the signal with the position

class SingleBoard(QWidget):
    conqueredSignal = pyqtSignal(str, str)  # class attribute, correct PyQt usage
    def __init__(self, Name="board00",boardPosition="01"): 
        super().__init__()
        self.boardName = Name
        self.setStyleSheet("background-color: rgba(255,255,255,0.8);border: 2px solid black;border-radius: 5px;")
        #use grid layout , learnt it in css3
        layout = QGridLayout()
        layout.setSpacing(3)
        # layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(layout)
        self.active = True
        
        for row in range(3):
            for col in range(3):
                button = SingleButton(Name=f"btn{row}{col} ", position=boardPosition, parent=self)
                button.setFixedSize(100, 100)
                layout.addWidget(button, row, col)
                button.clickedSignal.connect(self.conquerButton)  # Connect the signal to the conquerButton method
        self.score = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]] #this will keep track of the score of this board , if we have 3 1's or 0's here we will signal for larger board to indicate this as conquered
        
    def isActive(self):
        return self.active
    
    def setActive(self):
        if self.isActive()==True:
            return
        self.active = True
        for i in range(3):
            for j in range(3):
                button = self.layout().itemAtPosition(i, j).widget()
                button.clickable = True
        self.setStyleSheet("background-color: rgba(255,255,255,0.8);border: 2px solid black;border-radius: 5px;")
    def setInActive(self):
        if not self.isActive():
            return
        self.active = False
        for i in range(3):
            for j in range(3):
                button = self.layout().itemAtPosition(i, j).widget()
                button.clickable = False
        self.setStyleSheet("background-color: rgba(155,155,155,0.8);border: 2px solid black;border-radius: 5px;")
    def conquerButton(self,position="00",player="X"):
        # position = button.on_button_click(player)
        # if  position == -1 or not self.isActive():
        #     return -1
        # button = self.layout().itemAtPosition(int(position[0]), int(position[1])).widget()
        # if self.score[int(position[0])][int(position[1])] == 0 or self.score[int(position[0])][int(position[1])] == 1:
        #     return -1 #already pressed
        
        if player=="X":
            self.score[int(position[0])][int(position[1])] = 1
        elif player=="O":
            self.score[int(position[0])][int(position[1])] = 0
        self.setInActive()
        if(self.checkForCompletion(player,position))==True:
            self.conqueredSignal.emit(position, player)
        return 0            
    def checkForCompletion(self,player="X",position="00"):
        checkValue = -1
        if player=="X":
            checkValue = 1
        elif player=="O":
            checkValue = 0
        else:
            return False
        x1 = int(position[0])
        y1 = int(position[1])
        #check for complete row
        if self.score[x1][0] == checkValue and self.score[x1][1] == checkValue and self.score[x1][2] == checkValue:
                return True
        #check for complete col 
        elif self.score[0][y1] == checkValue and self.score[1][y1] == checkValue and self.score[2][y1] == checkValue:
                return True
        #check for complete diagonal
        elif x1==y1:
            condition1 = (self.score[0][0] == checkValue and self.score[1][1] == checkValue and self.score[2][2] == checkValue)
            condition2 = self.score[0][2] == checkValue and self.score[1][1] == checkValue and self.score[2][0] == checkValue  
            if condition1 or condition2:
                return True
        return False
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SingleBoard("TestBoard00")
    window.setFixedHeight(330)
    window.setFixedWidth(330)
    window.show()
    sys.exit(app.exec_())
