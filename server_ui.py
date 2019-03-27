import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from threading import Thread

from main import app as flask_app


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Run recognition endpoint'
        self.left = 300
        self.top = 300
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Run!', self)
        button.setToolTip('Run recognition endpoint')
        button.move(100, 100)
        button.clicked.connect(self.run_server)

        self.show()

    def run_server(self):
        print('Run server')
        app_thread = Thread(target=flask_app.run)
        app_thread.daemon = True
        app_thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
