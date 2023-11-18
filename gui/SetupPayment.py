from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class PaymentWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.setWindowTitle('Setup Payment')
        self.phone_number_edit = QLineEdit()
        self.name_on_card_edit = QLineEdit()
        self.card_number_edit = QLineEdit()
        self.expiry_edit = QLineEdit()
        self.cvc_edit = QLineEdit()
        self.done_button = QPushButton("Done")

        layout.addWidget(self.phone_number_edit)
        layout.addWidget(self.name_on_card_edit)
        layout.addWidget(self.card_number_edit)
        layout.addWidget(self.expiry_edit)
        layout.addWidget(self.cvc_edit)
        layout.addWidget(self.done_button)

# Sample code to run the widget
app = QApplication([])
win = PaymentWidget()
win.show()
app.exec()
