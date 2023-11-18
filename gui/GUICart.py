from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class GUICart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Cart")

        # Create widgets
        self.add_product_button = QPushButton("Add Product")
        self.remove_product_button = QPushButton("Remove Product")
        self.order_id_input = QLineEdit()
        self.customer_id_input = QLineEdit()
        self.table = QTableWidget(10, 5)
        self.total_label = QLabel("Total:")
        self.purchase_date_input = QLineEdit()
        self.confirm_button = QPushButton("CONFIRM")

        # Set headers for the table
        self.table.setHorizontalHeaderLabels(["Product ID", "Product Name", "Unit (lb / #)", "Price Per Unit", "Subtotal"])

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.add_product_button)
        layout.addWidget(self.remove_product_button)
        layout.addWidget(self.order_id_input)
        layout.addWidget(self.customer_id_input)
        layout.addWidget(self.table)
        layout.addWidget(self.total_label)
        layout.addWidget(self.purchase_date_input)
        layout.addWidget(self.confirm_button)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# To test the window
app = QApplication([])
window = GUICart()
window.show()
app.exec()
