from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout,QPushButton,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
from largerBoard import LargerBoard



class mainApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(1000)
        self.setFixedWidth(1000)
        
        self.setStyleSheet("background-color: gray;")
        
        layout = QGridLayout()
        layout.setSpacing(1)  # Remove all spacing between grid items
        # layout.setContentsMargins(1, 1, 1, 1)  # Remove all margins
        self.setLayout(layout)
        
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
        playerTurnLabel = QLabel("Player Turn: X")
        playerTurnLabel.setAlignment(Qt.AlignCenter)  # tried text align centre but it didn't work
        playerTurnLabel.setStyleSheet("""
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
        playerTurnWidget.layout().addWidget(playerTurnLabel)
        
        topWidget = QWidget()
        topLayout = QGridLayout()
        topLayout.setSpacing(5)  
        topLayout.setContentsMargins(5, 5, 5, 5)  
        topWidget.setLayout(topLayout)
        topWidget.layout().addWidget(darkThemeWidget, 0, 0)
        topWidget.layout().addWidget(newGameWidget, 0, 2)
        topWidget.layout().addWidget(playerTurnWidget, 0, 1)        
        
        # Add top controls to row 0, board to row 1
        layout.addWidget(topWidget, 0, 0)
        
        board = LargerBoard()
        layout.addWidget(board, 1, 0)
        
        # set row strtch to minimize space for top controls and maximize for board
        layout.setRowStretch(0, 0)  # Top controls take minimal space
        layout.setRowStretch(1, 1)  # Board takes maximum available space
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("uiComp/Ultimate_Tic_Tac_Toe.png"))
    
    window = mainApplication()
    window.setWindowTitle("Ultimate Tic Tac Toe by Mazen Azhary")
    window.show()
    sys.exit(app.exec_())