from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget

class InventoryWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.add_button = QPushButton("Add Product")
        self.remove_button = QPushButton("Remove Product")
        self.table = QTableWidget(10, 4)  # Adjust number of rows and columns accordingly
        self.table.setHorizontalHeaderLabels(['Product ID', 'Product Name', 'Available Unit (lb/#)', 'Price Per Unit'])

        layout.addWidget(self.add_button)
        layout.addWidget(self.table)
        layout.addWidget(self.remove_button)

# Sample code to run the widget
app = QApplication([])
win = InventoryWidget()
win.show()
app.exec()
