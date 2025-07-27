
from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout
import sys
from singleButton import SingleButton

class SingleBoard(QWidget):
    def __init__(self, Name="board0",position="0"): 
        super().__init__()
        self.position = position
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
                index = 3*row + col 
                button = SingleButton(Name=f"{Name}_btn_{index}", position=f"{row}{col}", parent=self)
                button.setFixedSize(100, 100)
                layout.addWidget(button, row, col)
    def isActive(self):
        return self.active
    
    def setActive(self, active):
        if self.active == active:
            return
        self.active = active
        for i in range(3):
            for j in range(3):
                button = self.layout().itemAtPosition(i, j).widget()
                button.clickable = active
        self.setStyleSheet("background-color: rgba(255,255,255,0.8);border: 2px solid black;border-radius: 5px;")
    def setInActive(self):
        if not self.isActive():
            return
        self.setActive(False)
        for i in range(3):
            for j in range(3):
                button = self.layout().itemAtPosition(i, j).widget()
                button.clickable = False
        self.setStyleSheet("background-color: rgba(155,155,155,0.8);border: 2px solid black;border-radius: 5px;")
    
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SingleBoard("TestBoard", "00")
    window.setFixedHeight(330)
    window.setFixedWidth(330)
    window.show()
    sys.exit(app.exec_())
    