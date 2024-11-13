import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton


class IncrementApp(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Increment App")
        self.setGeometry(100, 100, 300, 100)


        self.layout = QVBoxLayout()


        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter a number")


        self.button = QPushButton("Increment", self)
        self.button.clicked.connect(self.increment_number)


        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def increment_number(self):
        # Get text from input, convert it to an integer, increment by 1
        try:
            number = int(self.input_field.text())
            number += 1
            self.input_field.setText(str(number))
        except ValueError:
            self.input_field.setText("Enter a valid number")



app = QApplication(sys.argv)
window = IncrementApp()
window.show()
sys.exit(app.exec_())
