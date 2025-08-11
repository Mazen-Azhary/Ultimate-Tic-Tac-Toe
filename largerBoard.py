from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout,QLabel

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,pyqtSignal
import sys
from singleBoard import SingleBoard
from singleButton import SingleButton


class LargerBoard(QWidget):
    def updateTheme(self):
        from singleButton import THEME_DARK
        for row in range(3):
            for col in range(3):
                board = self.layout().itemAtPosition(row, col).widget()
                if board is not None:
                    board.updateTheme()
                if self.winner_labels[row][col] is not None:
                    winner_label = self.winner_labels[row][col]
                    if THEME_DARK:
                        winner_label.setStyleSheet("font-size: 72px; font-weight: bold; color: #FFD700; background-color: #222; border: 2px solid #FFD700; border-radius: 10px;")
                    else:
                        winner_label.setStyleSheet("font-size: 72px; font-weight: bold; color: #222; background-color: rgba(155,155,155,0.7); border: 2px solid #1976D2; border-radius: 10px;")
    gameOverSignal = pyqtSignal()  #game over 
    buttonClicked = pyqtSignal(str, str)  # buttonName, boardPosition
    score = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]] #each one of those is a smaller board on its own
    def __init__(self):
        super().__init__()    
        StyleSH = """background-color: gray;"""
        layout = QGridLayout()
        layout.setSpacing(3)
        self.setStyleSheet(StyleSH)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.winner_labels = [[None for _ in range(3)] for _ in range(3)]
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
                board.buttonClicked.connect(self.handleButtonClicked)
    def togglePlayer(self):
        pass  # No longer used
    def handleButtonClicked(self, buttonName, position):
        self.buttonClicked.emit(buttonName, position)
    def conquerBoard(self,position="00"):
        # print(f"Board {boardName} conquered by {player}")
        #we need to hide the 9 buttons of the smaller board and create larger widget with label 
        from singleButton import THEME_DARK
        player = SingleButton.player
        x1 = int(position[0])
        y1 = int(position[1])
        board = self.layout().itemAtPosition(x1,y1).widget()
        if board:
            for i in range(3):
                for j in range(3):
                    btn = board.layout().itemAtPosition(i, j).widget()
                    try:
                        btn.clicked.disconnect()
                    except Exception:
                        pass
                    btn.deleted = True
                    btn.clickable = False
                    btn.hide()
            winner_label = QLabel()
            winner_label.setText(player)
            winner_label.setAlignment(Qt.AlignCenter)
            LargerBoard.score[x1][y1] = 1 if player == "X" else 0
            if THEME_DARK:
                winner_label.setStyleSheet("font-size: 72px; font-weight: bold; color: #FFD700; background-color: #222; border: 2px solid #FFD700; border-radius: 10px;")
            else:
                winner_label.setStyleSheet("font-size: 72px; font-weight: bold; color: #222; background-color: rgba(155,155,155,0.7); border: 2px solid #1976D2; border-radius: 10px;")
            board.layout().addWidget(winner_label, 0, 0, 3, 3)  # Span all 3x3 cells
            self.winner_labels[x1][y1] = winner_label
        if(self.checkForCompletion(x1,y1)):
            self.gameOverSignal.emit()
    def checkForCompletion(self,x1,y1):
        checkValue = -1
        if SingleButton.player=="X":
            checkValue = 1
        elif SingleButton.player=="O":
            checkValue = 0
        else:
            return False

        #check for complete row
        if self.score[x1][0] == checkValue and self.score[x1][1] == checkValue and self.score[x1][2] == checkValue:
                return True
        #check for complete col 
        elif self.score[0][y1] == checkValue and self.score[1][y1] == checkValue and self.score[2][y1] == checkValue:
                return True
        # check main diagonal
        elif x1 == y1:
            if self.score[0][0] == checkValue and self.score[1][1] == checkValue and self.score[2][2] == checkValue:
                return True
        # check anti-diagonal
        elif x1 + y1 == 2:
            if self.score[0][2] == checkValue and self.score[1][1] == checkValue and self.score[2][0] == checkValue:
                return True
        return False

    def activateSmallerBoard(self, x, y):
        """activate smaller board with position of pressed button , deactivate all others , if it's already 
        inactive i handled it to return directly
        if it's already active i handled it to return directly
        and if it is complete then we allow all others to be active
        """
        # print("hello")
        if LargerBoard.score[x][y] != -1:  # If the board is already conquered
            for row in range(3):
                for col in range(3):
                    board = self.layout().itemAtPosition(row, col).widget()
                    if LargerBoard.score[row][col] == -1:
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
        # Fallback: if no unconquered board is active, activate all unconquered boards
        any_unconquered_active = False
        for row in range(3):
            for col in range(3):
                if LargerBoard.score[row][col] == -1:
                    board = self.layout().itemAtPosition(row, col).widget()
                    if board.isActive():
                        any_unconquered_active = True
                        break
        if not any_unconquered_active:
            for row in range(3):
                for col in range(3):
                    if LargerBoard.score[row][col] == -1:
                        board = self.layout().itemAtPosition(row, col).widget()
                        board.setActive()
                    
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("uiComp/Ultimate_Tic_Tac_Toe.png"))
    window = LargerBoard()
    window.setWindowTitle("Ultimate Tic Tac Toe by Mazen Azhary")
    window.setFixedHeight(940)
    window.setFixedWidth(955)
    window.show()
    sys.exit(app.exec_())