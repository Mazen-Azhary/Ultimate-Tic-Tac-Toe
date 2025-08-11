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
        playerTurnLabel = QLabel("Player Turn: "+SingleButton.player)
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
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("uiComp/Ultimate_Tic_Tac_Toe.png"))    
    window = mainApplication()
    window.setWindowTitle("Ultimate Tic Tac Toe by Mazen Azhary")
    window.show()
    sys.exit(app.exec_())