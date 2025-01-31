import sys
import requests
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget

SERVER_URL = "http://127.0.0.1:5000"

class InventoryUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Manager")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()
        
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.refresh_button = QPushButton("Refresh Inventory")
        self.refresh_button.clicked.connect(self.load_inventory)
        layout.addWidget(self.refresh_button)

        self.buy_button = QPushButton("Buy Item")
        self.buy_button.clicked.connect(lambda: self.update_item("add-item"))
        layout.addWidget(self.buy_button)

        self.return_button = QPushButton("Return Item")
        self.return_button.clicked.connect(lambda: self.update_item("remove-item"))
        layout.addWidget(self.return_button)

        self.setLayout(layout)
        self.load_inventory()

    def load_inventory(self):
        self.list_widget.clear()
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory")
        items = cursor.fetchall()
        conn.close()
        for item in items:
            self.list_widget.addItem(f"{item[0]} - {item[1]} pcs")

    def update_item(self, endpoint):
        if self.list_widget.currentItem():
            item_name = self.list_widget.currentItem().text().split(" - ")[0]
            requests.post(f"{SERVER_URL}/{endpoint}", json={"name": item_name, "quantity": 1})
            self.load_inventory()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryUI()
    window.show()
    sys.exit(app.exec_())
