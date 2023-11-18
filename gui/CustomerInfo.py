import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class CustomerInfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customer Info")
        self.setGeometry(100, 100, 600, 400)
        
        # Create Table
        self.createTable()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def createTable(self):
        # Set table dimensions
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10) # for example, setting 10 rows
        self.tableWidget.setColumnCount(5) # 5 columns as per the design

        # Set the table headers
        self.tableWidget.setHorizontalHeaderLabels(["Customer ID", "First Name", "Last Name", "Phone Number", "Credit Card Number"])

        # Set the data for rows, here as an example all cells are filled with 'Not Available'
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(i, j, QTableWidgetItem("Not Available"))

        # Update geometry to accommodate the headers
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QTableWidget.ResizeMode.Stretch)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = CustomerInfoWindow()
    mainWindow.show()
    app.exec()
