""""
PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para criação de aplicações GUI (Interface
Gráfica). Também inclui diversas funcionalidades, como:
Acesso a base dedados
Threads
Comunicação de rede e etc.

"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('Texto do Botão')
        self.btn.setStyleSheet(('font-size: 40px;'))

        self.btn.clicked.connect(self.acao)

        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.setCentralWidget(self.cw)

    def acao(self):
        print('Alguma coisa....')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
