from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout
from PyQt5.QtCore import pyqtSignal
import sys
from singleButton import SingleButton
class SingleBoard(QWidget):
    conqueredSignal = pyqtSignal(str)  # class attribute, correct PyQt usage
    buttonClicked = pyqtSignal(str, str)  # buttonName, boardPosition
    smallerBoardActivationSignal = pyqtSignal(int, int)  # Signal to Larger board activate a smaller board according to button press
    def __init__(self, Name="board00",boardPosition="01"): 
        super().__init__()
        self.boardName = Name
        layout = QGridLayout()
        layout.setSpacing(3)
        self.setLayout(layout)
        self.active = True
        for row in range(3):
            for col in range(3):
                button = SingleButton(Name=f"{row}{col} ", position=boardPosition)
                button.setFixedSize(100, 100)
                layout.addWidget(button, row, col)
                button.buttonClicked.connect(self.handleButtonClicked)
        self.score = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        self.updateTheme()
        
    def isActive(self):
        return self.active
    def togglePlayer(self):
        pass  # No longer used
    def handleButtonClicked(self, buttonName, position):
        self.conquerButton(buttonName, position)
        self.buttonClicked.emit(buttonName, position)
    def setActive(self):
        if self.isActive():
            return
        self.active = True
        for i in range(3):
            for j in range(3):
                button = self.layout().itemAtPosition(i, j).widget()
                button.clickable = True
                button.active = True
                
        self.updateTheme()
    def setInActive(self):
        if not self.isActive():
            return
        self.active = False
        for i in range(3):
            for j in range(3):
                button = self.layout().itemAtPosition(i, j).widget()
                button.clickable = False
                button.active = False
        self.updateTheme()
    def updateTheme(self):
        # Update board background based on active/inactive and theme
        from singleButton import THEME_DARK
        if self.active:
            if THEME_DARK:
                self.setStyleSheet("background-color: #444;font-size:40px;font-weight:bold; border: 3px solid #FFD700; border-radius: 8px;")
            else:
                self.setStyleSheet("background-color: rgba(255,255,255,0.8);font-size:40px; border: 2px solid black;font-weight:bold; border-radius: 5px;")
        else:
            
            if THEME_DARK:
                self.setStyleSheet("background-color: rgba(55,55,55,0.8);font-size:40px;font-weight:bold; border: 2px solid black; border-radius: 5px;")
            else:
                self.setStyleSheet("background-color: rgba(155,155,155,0.7);font-size:40px;font-weight:bold; border: 2px solid #888; border-radius: 5px;")
        for i in range(3):
            for j in range(3):
                button = self.layout().itemAtPosition(i, j).widget()
                button.updateTheme()
                
    def conquerButton(self,buttonName="btn00",position="00"):
        self.setInActive()
        buttonName = buttonName.strip() #faced a problem with whitespace 
        x1 = int(buttonName[-2])
        y1 = int(buttonName[-1])
        self.smallerBoardActivationSignal.emit(x1,y1) #send to larger board        
        player = SingleButton.player
        if player=="X":
            self.score[x1][y1] = 1
            
        elif player=="O":
            self.score[x1][y1] = 0
        if(self.checkForCompletion(x1,y1)):
            self.conqueredSignal.emit(position)
        return 0            
    def checkForCompletion(self,x1,y1):
        checkValue = -1
        if SingleButton.player=="X":
            checkValue = 1
            print("checking single board for x")
        elif SingleButton.player=="O":
            print("checking single board for O")
            checkValue = 0
        else:
            return False
        
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
