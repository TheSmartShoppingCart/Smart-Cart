from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget

class HistoryWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.setWindowTitle('History')
        self.table = QTableWidget(10, 4)  # Adjust number of rows and columns accordingly
        self.table.setHorizontalHeaderLabels(['Order ID', 'Customer ID', 'Total Price', 'Purchase Date'])

        layout.addWidget(self.table)

# Sample code to run the widget
app = QApplication([])
win = HistoryWidget()
win.show()
app.exec()
