from PyQt5.QtWidgets import QStackedWidget,QApplication, QWidget,QGridLayout,QPushButton,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
from largerBoard import LargerBoard

from singleButton import SingleButton #to use player static var
from tutorialPage import tutorialPage

class mainApplication(QStackedWidget):
    
    def __init__(self):
        super().__init__()
        self.setFixedHeight(1000)
        self.setFixedWidth(1000)
        
        self.setStyleSheet("background-color: gray;")
        self.restartable = False
        # Create the main game page as a central widget
        centralWidget = QWidget()
        layout = QGridLayout()
        layout.setSpacing(1)  # Remove all spacing between grid items
        # layout.setContentsMargins(1, 1, 1, 1)  # Remove all margins
        centralWidget.setLayout(layout)
        
        # Create top control panel to store 2 buttons and label
        darkThemeWidget = QWidget()
        darkThemeButton = QPushButton("🌙")
        #darkThemeButton = QPushButton("☀️")
        
        # darkThemeButton.setStyleSheet("width:300px;font-size: 10px;font-weight: bold;")
        darkThemeLayout = QGridLayout()
        darkThemeLayout.setContentsMargins(0, 0, 0, 0)  
        darkThemeWidget.setLayout(darkThemeLayout)
        #i made an rgba border to add smooth transition for human eye between black and gray 
        darkThemeButton.setStyleSheet("""background-color: #2C2C2C;
                                      border: 2px solid rgba(0,0,0,0.5);
                                      height:30px;
                                      border-radius: 5px;
                                      color:#FFD700
                                      """)
        darkThemeWidget.layout().addWidget(darkThemeButton)
        
        newGameButton = QPushButton()        
        newGameWidget = QWidget()
        newGameLayout = QGridLayout()
        newGameLayout.setContentsMargins(0, 0, 0, 0)  
        newGameWidget.setLayout(newGameLayout)
        newGameButton.setText("New Game")
        newGameButton.setStyleSheet("""
                                    background-color: #F0F0F0;
                                    width:300px;
                                    height:30px;
                                    font-size: 16px;
                                    font-weight: bold;
                                    border-radius: 5px;
                                    border: 2px solid rgba(0,0,0,0.5);
                                    color: black;""")
        newGameWidget.layout().addWidget(newGameButton)
        
        playerTurnWidget = QWidget()
        playerTurnLayout = QGridLayout()
        playerTurnLayout.setContentsMargins(0, 0, 0, 0)  
        playerTurnWidget.setLayout(playerTurnLayout)
        self.playerTurnLabel = QLabel("Player Turn: "+SingleButton.player)
        self.playerTurnLabel.setAlignment(Qt.AlignCenter)  # tried text align centre but it didn't work
        self.playerTurnLabel.setStyleSheet("""
                                    background-color: #D32F2F;
                                    width:300px;
                                    height:30px;
                                    font-size: 16px;
                                    font-weight: bold;
                                    border-radius: 5px;
                                    border: 2px solid rgba(0,0,0,0.7);
                                    """)
        ##D32F2F for X
        # #1976D2 for O
        playerTurnWidget.layout().addWidget(self.playerTurnLabel)
        
        
        tutorialPageButton = QPushButton("How to Play")
        tutorialPageButton.setStyleSheet(""" background-color: #F0F0F0;
                                        width:300px;
                                        height:30px;
                                        font-size: 16px;
                                        font-weight: bold;
                                        border-radius: 5px;
                                        border: 2px solid rgba(0,0,0,0.5);
                                        color: black;                                    
                                         """)
        tutorialPageWidget = QWidget()
        tutorialPageLayout = QGridLayout()
        tutorialPageLayout.setContentsMargins(0, 0, 0, 0)
        tutorialPageWidget.setLayout(tutorialPageLayout)
        tutorialPageWidget.layout().addWidget(tutorialPageButton)
        
        topWidget = QWidget()
        topLayout = QGridLayout()
        topLayout.setSpacing(5)  
        topLayout.setContentsMargins(5, 5, 5, 5)  
        topWidget.setLayout(topLayout)
        topWidget.layout().addWidget(darkThemeWidget, 0, 0)
        topWidget.layout().addWidget(newGameWidget, 0, 2)
        topWidget.layout().addWidget(playerTurnWidget, 0, 1)        
        topWidget.layout().addWidget(tutorialPageWidget, 0, 3)
        # Add top controls to row 0, board to row 1
        layout.addWidget(topWidget, 0, 0)
        
        board = LargerBoard()
        layout.addWidget(board, 1, 0)
        
        # set row strtch to minimize space for top controls and maximize for board
        layout.setRowStretch(0, 0)  # Top controls take minimal space
        layout.setRowStretch(1, 1)  # Board takes maximum available space
        
        # Add the central widget (main game page) to the stacked widget
        self.addWidget(centralWidget)  # index 0
        
        # Create and add the tutorial page (index 1)
        tutorialPageObj = tutorialPage()
        self.addWidget(tutorialPageObj.window)  # index 1, use .window for the loaded UI
        
        tutorialPageButton.clicked.connect(lambda: self.setCurrentIndex(1))
        tutorialPageObj.button.clicked.connect(lambda: self.setCurrentIndex(0))
        board.gameOverSignal.connect(self.endGame)
        board.toggleSignal_to_main.connect(self.togglePlayer)
        newGameButton.clicked.connect(self.newGame)  
    def togglePlayer(self):
        self.restartable = True
        if SingleButton.player == "O":
            self.playerTurnLabel.setText("Player Turn: "+"X")
            self.playerTurnLabel.setStyleSheet("""
                                    background-color: #D32F2F;
                                    width:300px;
                                    height:30px;
                                    font-size: 16px;
                                    font-weight: bold;
                                    border-radius: 5px;
                                    border: 2px solid rgba(0,0,0,0.7);
                                    """)
        else:        
            self.playerTurnLabel.setText("Player Turn: "+"O")
            self.playerTurnLabel.setStyleSheet("""
                                    background-color: #1976D2;
                                    width:300px;
                                    height:30px;
                                    font-size: 16px;
                                    font-weight: bold;
                                    border-radius: 5px;
                                    border: 2px solid rgba(0,0,0,0.7);
                                    """)
        ##D32F2F for X
        # #1976D2 for O
        
    def endGame(self):
        # Remove all widgets from the main game page and show a winner label
        
        
        # Toggle player to show the winner , as the winner is the one who just played
        winner = SingleButton.player
        if winner == "X":
            winner = "O"
        else: 
            winner = "X"
        winner_label = QLabel(f"Winner: {winner}")
        winner_label.setAlignment(Qt.AlignCenter)
        winner_label.setStyleSheet("""
            background-color: #222;
            color: #FFD700;
            font-size: 56px;
            font-weight: bold;
            border-radius: 20px;
            border: 4px solid #FFD700;
            padding: 80px 30px 80px 30px;
            min-height: 400px;
        """)
        centralWidget = self.widget(0)
        layout = centralWidget.layout()
        # Remove all widgets except those in the top row (row 0)
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item is not None:
                pos = layout.getItemPosition(i)
                row_idx = pos[0]
                if row_idx != 0:
                    widget = item.widget()
                    if widget is not None:
                        widget.setParent(None)
        # Add the winner label to occupy the grid area (row 1, col 0, spanning all columns)
        layout.addWidget(winner_label, 1, 0, 1, layout.columnCount())
    def newGame(self):
        # Check if the board has any played cells
        
        if not self.restartable:
            # print("Game has just started, nothing to reset.")
            return

        # Remove the current LargerBoard from the layout
        centralWidget = self.widget(0)
        layout = centralWidget.layout()
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item is not None:
                pos = layout.getItemPosition(i)
                row_idx = pos[0]
                col_idx = pos[1] if len(pos) > 1 else None
                if row_idx == 1 and (col_idx == 0 or col_idx is None):
                    widget = item.widget()
                    if widget is not None:
                        widget.setParent(None)
                        widget.deleteLater()

        # Reset static variables
        LargerBoard.score = [[-1 for _ in range(3)] for _ in range(3)]
        SingleButton.player = "X"
        self.playerTurnLabel.setText("Player Turn: X")
        self.playerTurnLabel.setStyleSheet("""
                                    background-color: #D32F2F;
                                    width:300px;
                                    height:30px;
                                    font-size: 16px;
                                    font-weight: bold;
                                    border-radius: 5px;
                                    border: 2px solid rgba(0,0,0,0.7);
                                    """)

        # Create and add a new LargerBoard
        new_board = LargerBoard()
        layout.addWidget(new_board, 1, 0)
        new_board.gameOverSignal.connect(self.endGame)
        new_board.toggleSignal_to_main.connect(self.togglePlayer)
        # print("New game started!")


        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("uiComp/Ultimate_Tic_Tac_Toe.png"))    
    window = mainApplication()
    window.setWindowTitle("Ultimate Tic Tac Toe by Mazen Azhary")
    window.show()
    sys.exit(app.exec_())