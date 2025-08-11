from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout,QLabel

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
from singleBoard import SingleBoard
from singleButton import SingleButton


class LargerBoard(QWidget):
    def __init__(self):
        super().__init__()    
        StyleSH = """background-color: gray;"""
        layout = QGridLayout()
        layout.setSpacing(3)
        self.setStyleSheet(StyleSH)
        self.setContentsMargins(0, 0, 0, 0)
        self.score = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]] #each one of those is a smaller board on its own
        self.setLayout(layout)
        for rows in range(3):
            for cols in range(3):
                board = SingleBoard(f"board{rows}{cols}",f"{rows}{cols}")
                board.setFixedSize(310, 310)
                board.setActive()
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
                board.conqueredSignal.connect(self.conquerBoard) 
                board.smallerBoardActivationSignal.connect(self.activateSmallerBoard)  
    def conquerBoard(self,position="00"):
        # print(f"Board {boardName} conquered by {player}")
        #we need to hide the 9 buttons of the smaller board and create larger widget with label 
        player = SingleButton.player
        x1 = int(position[0])
        y1 = int(position[1])
        board = self.layout().itemAtPosition(x1,y1).widget()
        if board:
            for i in range(3):
                for j in range(3):
                    btn = board.layout().itemAtPosition(i, j).widget()
                    btn.hide()
            winner_label = QLabel()
            winner_label.setText(player)
            winner_label.setAlignment(Qt.AlignCenter)
            self.score[x1][y1] = 1 if player == "X" else 0
            winner_label.setStyleSheet("font-size: 72px; font-weight: bold; color: #222; background-color: rgba(155,155,155,0.7);")
            board.layout().addWidget(winner_label, 0, 0, 3, 3)  # Span all 3x3 cells

    def activateSmallerBoard(self, x, y):
        """activate smaller board with position of pressed button , deactivate all others , if it's already 
        inactive i handled it to return directly
        if it's already active i handled it to return directly
        and if it is complete then we allow all others to be active
        """
        # print("hello")
        if self.score[x][y] != -1:  # If the board is already conquered
            for row in range(3):
                for col in range(3):
                    board = self.layout().itemAtPosition(row, col).widget()
                    if self.score[row][col] == -1:
                        board.setActive()
                    else:
                        board.setInActive()
            return
        # If the board is not conquered, we need to activate it and deactivate all others
        for row in range(3):
                for col in range(3):
                    if row == x and col == y:
                        board = self.layout().itemAtPosition(x, y).widget()
                        board.setActive()                       
                        continue
                    board = self.layout().itemAtPosition(row, col).widget()
                    board.setInActive()
                    
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("uiComp/Ultimate_Tic_Tac_Toe.png"))
    window = LargerBoard()
    window.setWindowTitle("Ultimate Tic Tac Toe by Mazen Azhary")
    window.setFixedHeight(940)
    window.setFixedWidth(955)
    window.show()
    sys.exit(app.exec_())