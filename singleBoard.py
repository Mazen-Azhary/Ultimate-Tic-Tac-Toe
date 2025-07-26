
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QGridLayout
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
        
        for row in range(3):
            for col in range(3):
                index = 3*row + col 
                button = SingleButton(Name=f"{Name}_btn_{index}", position=f"{row}{col}")
                button.setFixedSize(100, 100)
                layout.addWidget(button, row, col)
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SingleBoard("TestBoard", "00")
    window.setFixedHeight(330)
    window.setFixedWidth(330)
    window.show()
    sys.exit(app.exec_())
    