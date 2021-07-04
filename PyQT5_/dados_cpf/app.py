import sys
from Modulos.PyQT5_.dados_cpf.validador_cpf import valida_cpf
from Modulos.PyQT5_.dados_cpf.gerador_cpf import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importando o layout criado no qtdesing

from Modulos.PyQT5_.dados_cpf import design_cpf


class GeravalidaCPF(QMainWindow, design_cpf.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCPF.clicked.connect(self.gera_cpf)
        self.btnValidaCPF.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.labelRetorno.setText(
            str(gera_cpf())
        )

    def valida_cpf(self):
        cpf = self.inputValidaCPF.text()
        self.labelRetorno.setText(
            str(valida_cpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeravalidaCPF()
    gera_valida_cpf.show()
    qt.exec_()
