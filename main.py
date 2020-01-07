from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
import sqlite3
import sys


class CoffeeShow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.load_button.clicked.connect(self.load)
        self.coffee_table_widget.setColumnCount(7)
        self.coffee_table_widget.setHorizontalHeaderLabels(
            ["id", "variety", "degree_of_roasting",
             "ground", "taste_description", "price", "volume"]
        )
        self.coffee_table_widget.resizeColumnsToContents()

    def load(self):
        cur = self.connection.cursor()
        data = cur.execute("""SELECT * FROM coffee""").fetchall()
        for i, part in enumerate(data):
            self.coffee_table_widget.setRowCount(self.coffee_table_widget.rowCount() + 1)
            for j, item in enumerate(part):
                self.coffee_table_widget.setItem(i, j, QTableWidgetItem(str(item)))
        self.coffee_table_widget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee_show = CoffeeShow()
    coffee_show.show()
    sys.exit(app.exec())
