from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
import sys


class SingleButtonWidget(QPushButton):
    def __init__(self,Name="btn",position="00"): #00 is top left
        super().__init__()
        self.position = position
        self.buttonName = Name
        self.clicked.connect(self.on_button_click)
        self.setStyleSheet("width:30%; height:30%; background-color: rgba(255,255,255,0.7);")  
    def on_button_click(self,player):
        if player == "1":
            self.button.setText("X")
        else:
            self.button.setText("O")
        self.setStyleSheet("background-color: rgba(100,100,100,0.7);")  
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SingleButtonWidget()
    window.show()
    sys.exit(app.exec_())