import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QComboBox, QDoubleSpinBox, QMessageBox

class GroceryStoreApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Product selection layout
        productLayout = QHBoxLayout()
        self.productComboBox = QComboBox()
        self.productComboBox.addItems(['Apples', 'Bananas', 'Carrots', 'Donuts', 'Eggs'])
        self.productPriceDict = {'Apples': 0.5, 'Bananas': 0.3, 'Carrots': 0.8, 'Donuts': 1.2, 'Eggs': 2.0}
        self.productSpinBox = QDoubleSpinBox()
        self.productSpinBox.setRange(1, 100)
        self.productSpinBox.setPrefix('$')
        self.productSpinBox.setValue(self.productPriceDict[self.productComboBox.currentText()])
        self.productComboBox.currentIndexChanged.connect(self.updatePrice)
        self.addButton = QPushButton('Add to Cart')
        self.addButton.clicked.connect(self.addToCart)

        productLayout.addWidget(self.productComboBox)
        productLayout.addWidget(self.productSpinBox)
        productLayout.addWidget(self.addButton)
        layout.addLayout(productLayout)

        # Cart layout
        self.cartList = QListWidget()
        layout.addWidget(self.cartList)
        self.cartData = {}

        # Checkout layout
        checkoutLayout = QHBoxLayout()
        self.totalLabel = QLabel('Total: $0.0')
        self.removeButton = QPushButton('Remove Selected')
        self.removeButton.clicked.connect(self.removeFromCart)
        self.checkoutButton = QPushButton('Checkout')
        self.checkoutButton.clicked.connect(self.checkout)
        checkoutLayout.addWidget(self.removeButton)
        checkoutLayout.addWidget(self.totalLabel)
        checkoutLayout.addWidget(self.checkoutButton)
        layout.addLayout(checkoutLayout)

        self.setLayout(layout)
        self.setWindowTitle('Grocery Store Cart')
        self.setGeometry(100, 100, 400, 300)

    def updatePrice(self):
        product = self.productComboBox.currentText()
        self.productSpinBox.setValue(self.productPriceDict[product])

    def addToCart(self):
        product = self.productComboBox.currentText()
        price = self.productSpinBox.value()
        if product in self.cartData:
            self.cartData[product] += price
        else:
            self.cartData[product] = price
        self.refreshCart()

    def removeFromCart(self):
        currentItem = self.cartList.currentItem()
        if currentItem:
            product = currentItem.text().split(' - ')[0]
            if product in self.cartData:
                del self.cartData[product]
            self.refreshCart()

    def checkout(self):
        total = sum(self.cartData.values())
        QMessageBox.information(self, 'Checkout', f'Total Amount: ${total:.2f}\nThanks for shopping with us!', QMessageBox.StandardButton.Ok)
        self.cartData = {}
        self.refreshCart()

    def refreshCart(self):
        self.cartList.clear()
        for product, price in self.cartData.items():
            self.cartList.addItem(f'{product} - ${price:.2f}')
        total = sum(self.cartData.values())
        self.totalLabel.setText(f'Total: ${total:.2f}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GroceryStoreApp()
    window.show()
    sys.exit(app.exec())
