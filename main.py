import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import unicodedata


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Работа с текстом с PyQt5')

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        text = self.textEdit_text.toPlainText()
        normalized_text = unicodedata.normalize('NFC', text)
        longest_sequence = self.find_longest_sequence(normalized_text, 'а')
        self.textEdit_words.setPlainText(longest_sequence)

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()

    def find_longest_sequence(self, text, target):
        max_sequence = ''
        current_sequence = ''
        for char in text:
            if char.casefold() == target:
                current_sequence += char
                if len(current_sequence) > len(max_sequence):
                    max_sequence = current_sequence
            else:
                current_sequence = ''
        return max_sequence


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
