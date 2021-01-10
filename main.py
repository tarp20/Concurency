import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_mainWindow
from currency_converter import CurrencyConverter


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Currency Converter')
        self.setWindowIcon(QIcon('exchanging.png'))
        self.ui.input_currency.setPlaceholderText('From a currency:')
        self.ui.input_amount.setPlaceholderText('I have:')
        self.ui.output_currency.setPlaceholderText('Into a currency:')
        self.ui.output_amount.setPlaceholderText('I get:')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.ui.input_currency.text()
        output_currency = self.ui.output_currency.text()
        input_amount = int(self.ui.input_amount.text())
        output_amount = round(c.convert(input_amount, '%s' % (
            input_currency), '%s' % (output_currency)), 2)
        self.ui.output_amount.setText(str(output_amount))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
