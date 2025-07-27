from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout
from PyQt5.QtGui import QIcon
import sys
from singleBoard import SingleBoard


class LargerBoard(QWidget):
    def __init__(self):
        super().__init__()    
        StyleSH = """background-color: gray;"""
        layout = QGridLayout()
        layout.setSpacing(3)
        self.setStyleSheet(StyleSH)
        self.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(layout)
        for rows in range(3):
            for cols in range(3):
                board = SingleBoard(self)
                board.setFixedSize(310, 310)
                StyleSH = board.styleSheet()
                if rows==0:
                    StyleSH += "border-bottom: 2px solid black;"
                elif rows==1:
                    StyleSH += "border-bottom: 2px solid black;"
                    StyleSH += "border-top: 2px solid black;"
                else:
                    StyleSH += "border-top: 2px solid black;"
                if(cols==0):
                    StyleSH += "border-right: 2px solid black;"
                elif(cols==1):
                    StyleSH += "border-right: 2px solid black;"
                    StyleSH += "border-left: 2px solid black;"
                else:
                    StyleSH += "border-left: 2px solid black;"
                
                board.setStyleSheet(StyleSH)       
                layout.addWidget(board, rows, cols)
                


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("uiComp/Ultimate_Tic_Tac_Toe.png"))
    window = LargerBoard()
    window.setWindowTitle("Ultimate Tic Tac Toe by Mazen Azhary")
    window.setFixedHeight(940)
    window.setFixedWidth(955)
    window.show()
    sys.exit(app.exec_())