from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QGridLayout
from PyQt5.QtCore import pyqtSignal
import sys
from singleButton import SingleButton
class SingleBoard(QWidget):
    conqueredSignal = pyqtSignal(str, str)  # class attribute, correct PyQt usage
    smallerBoardActivationSignal = pyqtSignal(int, int)  # Signal to Larger board activate a smaller board according to button press 
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
                button = SingleButton(Name=f"btn{row}{col} ", position=boardPosition)
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
                button.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(255,255,255,0.8);
                        font-size:40px;
                        font-weight:Bold;
                        border: 2px solid black;
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: rgba(155,155,155,0.7);
                    }
                """)
    def setInActive(self):
        if not self.isActive():
            return
        self.active = False
        for i in range(3):
            for j in range(3):
                button = self.layout().itemAtPosition(i, j).widget()
                button.clickable = False
                button.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(55,55,55,0.8);
                        font-size:40px;
                        font-weight:Bold;
                        border: 2px solid black;
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: rgba(155,155,155,0.7);
                    }
                """)
                
    def conquerButton(self,buttonName="btn00",position="00",player="X"):
        self.setInActive()
        buttonName = buttonName.strip() #faced a problem with whitespace 
        x1 = int(buttonName[-2])
        y1 = int(buttonName[-1])
        self.smallerBoardActivationSignal.emit(x1,y1) #send to larger board        
        if player=="X":
            self.score[x1][y1] = 1
        elif player=="O":
            self.score[x1][y1] = 0
        if(self.checkForCompletion(player,position)):
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
        # print("hehehe")
        return False
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SingleBoard("TestBoard00")
    window.setFixedHeight(330)
    window.setFixedWidth(330)
    window.show()
    sys.exit(app.exec_())
