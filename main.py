import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 150)
        self.move(400, 300)
        self.setWindowTitle('Advent')


class AdventCalendar(QGridLayout):
    def __init__(self):
        super().__init__()

        for row in range(0, 6):
            for col in range(0, 4):
                self.addWidget(self.create_button(row, col), row, col)

    def create_button(self, row, col):
        return QPushButton(self.create_row_col_text(row, col))

    @staticmethod
    def create_row_col_text(row, col):
        return str(row * 4 + col + 1)


def main():
    print("hello")
    app = QApplication(sys.argv)

    window = Window()
    calendar = AdventCalendar()

    window.setLayout(calendar)
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
