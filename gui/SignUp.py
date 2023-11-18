from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class SignUpWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.setWindowTitle('Sign Up')
        self.label_first = QLabel('First Name')
        self.first_name_edit = QLineEdit()
        self.label_last = QLabel('Last Name')
        self.last_name_edit = QLineEdit()
        self.label_phone = QLabel('Phone Number')
        self.phone_number_edit = QLineEdit()
        self.sign_up_button = QPushButton('Sign Up')

    


        layout.addWidget(self.label_first)
        layout.addWidget(self.first_name_edit)
        layout.addWidget(self.label_last)
        layout.addWidget(self.last_name_edit)
        layout.addWidget(self.label_phone)
        layout.addWidget(self.phone_number_edit)
        layout.addWidget(self.sign_up_button)

# Sample code to run the widget
app = QApplication([])
win = SignUpWidget()
win.show()
app.exec()
#print("NEW CUSTOMER \n" + self.first_name_edit + " " + self.last_name_edit + "\n" + "Phone: " + self.phone_number_edit)
