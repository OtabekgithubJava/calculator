import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QGridLayout()

        self.display = QLineEdit()
        self.display.setStyleSheet("QLineEdit { font-size: 20px; padding: 10px; }")
        self.layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        positions = [(i, j) for i in range(1, 5) for j in range(4)]

        for position, btn_text in zip(positions, buttons):
            btn = QPushButton(btn_text)
            btn.setStyleSheet("QPushButton { font-size: 18px; padding: 10px; }")
            btn.clicked.connect(self.on_button_click)
            self.layout.addWidget(btn, *position)

        self.setLayout(self.layout)
        self.result = ''

    def on_button_click(self):
        btn = self.sender()
        btn_text = btn.text()

        if btn_text == '=':
            try:
                self.result = str(eval(self.result))
                self.display.setText(self.result)
            except Exception as e:
                self.display.setText("Error")
        elif btn_text == 'C':
            self.result = ''
            self.display.clear()
        else:
            self.result += btn_text
            self.display.setText(self.result)

def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()