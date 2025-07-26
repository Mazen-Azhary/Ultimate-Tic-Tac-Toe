
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
import sys


class SingleButton(QPushButton):
    def __init__(self,Name="btn",position="00"): #00 is top left
        super().__init__()
        
        self.position = position
        self.buttonName = Name
        self.clicked.connect(self.on_button_click)
        self.clickable = True
        # self.setFixedHeight(60)
        # self.setFixedWidth(60)
        styleSh = """
        QPushButton {
        width:30%;
        height:30%;
        background-color: rgba(255,255,255,0.7);
        border: 1px solid black;
        border-radius: 5px;
        font-size: 30px;
        }
        QPushButton:hover {
        background-color: rgba(155,155,155,0.7);
            }
            """
        self.setStyleSheet(styleSh)  
    def on_button_click(self,player="1"):
        
        if self.clickable == False:
            return -1    
        self.clickable = False
        if player == "1":
            self.setText("X")
        else:
            self.setText("O")
        styleSh = """
        QPushButton {
        width:30%;
        height:30%;
        background-color: rgba(170,170,170,0.7);
        border: 1px solid black;
        border-radius: 5px;
        font-size: 30px;
       }
        QPushButton:hover {
        background-color: rgba(155,155,155,0.7);
            }
            """
        self.setStyleSheet(styleSh)
        return self.position

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SingleButton("TestButton", "01")
    window.setFixedHeight(100)
    window.setFixedWidth(100)
    window.show()
    sys.exit(app.exec_())