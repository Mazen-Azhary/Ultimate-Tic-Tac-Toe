from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication
import sys

class UltimateTicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ultimate Tic Tac Toe")
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        
        self.boards = []  # List to hold 9 inner boards

        for i in range(3):
            for j in range(3):
                board_layout = QGridLayout()
                board_buttons = []
                for x in range(3):
                    for y in range(3):
                        btn = QPushButton("")
                        btn.setFixedSize(50, 50)
                        btn.clicked.connect(lambda _, i=i, j=j, x=x, y=y: self.handle_click(i, j, x, y))
                        board_layout.addWidget(btn, x, y)
                        board_buttons.append(btn)
                board_widget = QWidget()
                board_widget.setLayout(board_layout)
                self.main_layout.addWidget(board_widget, i, j)
                self.boards.append(board_buttons)

    def handle_click(self, board_i, board_j, cell_x, cell_y):
        print(f"Clicked board ({board_i}, {board_j}) cell ({cell_x}, {cell_y})")
        # Handle move logic here...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = UltimateTicTacToe()
    game.show()
    sys.exit(app.exec_())
