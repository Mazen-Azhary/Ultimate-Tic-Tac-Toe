from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSignal

# Global theme token
THEME_DARK = False

class SingleButton(QPushButton):
    toggleSignal = pyqtSignal()  # Signal to toggle player in main application
    clickedSignal = pyqtSignal(str, str, str)  # buttonPosInSingleBoard, boardPosition, player
    buttonClicked = pyqtSignal(str, str)  # buttonPosInSingleBoard, boardPosition
    player = "X"  # static var to be shared among the 81 buttons

    def __init__(self, Name="btn00", position="00"):
        super().__init__()
        self.position = position
        self.buttonName = Name
        self.clicked.connect(self.on_button_click)
        self.clickable = True
        self.active = True  # Track if the button is active (enabled for play)
        self.updateTheme()
        self.deleted = False  # Track if the button is deleted/hidden

    def updateTheme(self):
        # Use self.active to determine style
        if THEME_DARK:
            if self.active:
                styleSh = """
                    QPushButton {
                        width:30%;
                        height:30%;
                        background-color: #2c2c2c;
                        color: #FFD700;
                        border: 1px solid #FFD966;
                        border-radius: 5px;
                        font-size: 30px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #3a3a3a;
                    }
                """
            else:
                styleSh = """
                    QPushButton {
                        width:30%;
                        height:30%;
                        background-color: #1e1e1e;
                        color: #b3b3b3;
                        border: 1px solid #555;
                        border-radius: 5px;
                        font-size: 30px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #1e1e1e;
                    }
                """
        else:
            # Light theme
            if self.active:
                # Active button in light theme
                styleSh = """
                   QPushButton {
        width:30%;
        height:30%;
        background-color: rgba(255,255,255,0.7);
        border: 1px solid black;
        border-radius: 5px;
        font-size: 30px;
        font-weight: bold;
        }
        QPushButton:hover {
        background-color: rgba(155,155,155,0.7);
            }
                """
            else:
                # Inactive button in light theme
                styleSh = """
                    QPushButton {
                        width:30%;
                        height:30%;
                        background-color: rgba(170,170,170,0.7);
                        border: 1px solid #bbb;
                        border-radius: 5px;
                        font-size: 30px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: rgba(155,155,155,0.7);
                    }
                """
        self.setStyleSheet(styleSh)

    def on_button_click(self):
        if self.deleted:
            return -1
        if self.clickable is False or self.text() != "":
            return -1
        self.clickable = False
        self.setText(SingleButton.player)
        self.updateTheme()
        self.buttonClicked.emit(self.buttonName, self.position)  # Only emit signal upward

    def togglePlayer(self):
        if self.deleted:
            return
        pass  # No longer used; toggling is handled only in main
