from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QTextEdit, \
    QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QFormLayout, QLineEdit, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Calculadora(QWidget):
    def __init__(self):
        super(Calculadora,self).__init__()
        self.resize(450,400)
        self.setWindowTitle("Calculadora")
        self.display_widgets()

    def display_widgets(self):
        lbl_calculadora = QLabel("Calculadora",self)
        lbl_calculadora.setFont(QFont("Arial",20))
        lbl_calculadora.setAlignment(Qt.AlignCenter)

        self.lbl_operaciones = QLabel("",self)
        self.lbl_operaciones.setAlignment(Qt.AlignLeft)

        lbl_historial = QLabel("Historial",self)
        lbl_historial.setFont(QFont("Arial", 18))
        lbl_historial.setAlignment(Qt.AlignRight)

        self.txt_edit = QTextEdit(self)

        self.lbl_resultado = QLabel("",self)
        self.lbl_resultado.setAlignment(Qt.AlignRight)

        glyt_botones = QGridLayout()
        self.btn_0 = QPushButton("0",self)
        self.btn_1 = QPushButton("1", self)
        self.btn_2 = QPushButton("2", self)
        self.btn_3 = QPushButton("3", self)
        self.btn_4 = QPushButton("4", self)
        self.btn_5 = QPushButton("5", self)
        self.btn_6 = QPushButton("6", self)
        self.btn_7 = QPushButton("7", self)
        self.btn_8 = QPushButton("8", self)
        self.btn_9 = QPushButton("9", self)
        self.btn_punto = QPushButton(".", self)
        self.btn_igual = QPushButton("=", self)
        self.btn_sumar = QPushButton("+", self)
        self.btn_restar = QPushButton("-", self)
        self.btn_mult = QPushButton("*", self)
        self.btn_div = QPushButton("/", self)
        self.btn_borrar = QPushButton("Borrar", self)

        glyt_botones.addWidget(self.btn_borrar,0,0,1,1)
        glyt_botones.addWidget(self.btn_div,0,1,1,1)
        glyt_botones.addWidget(self.btn_mult,0,2,1,1)
        glyt_botones.addWidget(self.btn_restar,0,3,1,1)
        glyt_botones.addWidget(self.btn_7,1,0,1,1)
        glyt_botones.addWidget(self.btn_8,1,1,1,1)
        glyt_botones.addWidget(self.btn_9,1,2,1,1)
        glyt_botones.addWidget(self.btn_sumar,1,3,2,1)
        glyt_botones.addWidget(self.btn_4,2,0,1,1)
        glyt_botones.addWidget(self.btn_5,2,1,1,1)
        glyt_botones.addWidget(self.btn_6,2,2,1,1)
        glyt_botones.addWidget(self.btn_1,3,0,1,1)
        glyt_botones.addWidget(self.btn_2,3,1,1,1)
        glyt_botones.addWidget(self.btn_3,3,2,1,1)
        glyt_botones.addWidget(self.btn_igual,3,3,2,1)
        glyt_botones.addWidget(self.btn_0,4,0,1,2)
        glyt_botones.addWidget(self.btn_punto,4,2,1,1)

        glyt_principal = QGridLayout(self)
        glyt_principal.addWidget(lbl_calculadora,0,0,1,2) # Pos fila, columna, cantidad filas, cantidad columnas
        glyt_principal.addWidget(self.lbl_operaciones,1,0,1,1)
        glyt_principal.addWidget(lbl_historial,1,1,1,1)
        glyt_principal.addWidget(self.txt_edit,2,1,3,1)
        glyt_principal.addWidget(self.lbl_resultado,2,0,2,1)
        glyt_principal.addLayout(glyt_botones, 4,0)

        self.btn_0.clicked.connect(self.numero)
        self.btn_1.clicked.connect(self.numero)
        self.btn_2.clicked.connect(self.numero)
        self.btn_3.clicked.connect(self.numero)
        self.btn_4.clicked.connect(self.numero)
        self.btn_5.clicked.connect(self.numero)
        self.btn_6.clicked.connect(self.numero)
        self.btn_7.clicked.connect(self.numero)
        self.btn_8.clicked.connect(self.numero)
        self.btn_9.clicked.connect(self.numero)
        self.btn_sumar.clicked.connect(self.numero)
        self.btn_restar.clicked.connect(self.numero)
        self.btn_mult.clicked.connect(self.numero)
        self.btn_div.clicked.connect(self.numero)
        self.btn_punto.clicked.connect(self.numero)

        self.btn_igual.clicked.connect(self.resultado)
        self.btn_borrar.clicked.connect(self.borrar)

    def keyPressEvent(self, event):
        print(event.key())
        if event.text().isnumeric():
            self.operacion(event.text())
        elif event.key() in [47,42,45,43,46,40,41]:
            self.operacion(event.text())
        elif event.key() in [16777220,16777221]:
            self.resultado()
        elif event.key() == 16777219:
            self.borrar()


    def operacion(self,letra):
        texto = self.lbl_operaciones.text()
        self.lbl_operaciones.setText(texto + letra)

    def numero(self):
        sender = self.sender()
        texto = self.lbl_operaciones.text()
        if sender.text() == "*":
            self.lbl_operaciones.setText(texto+"*")
        else:
            self.lbl_operaciones.setText(texto + sender.text())


    def resultado(self):
        resultado = eval(self.lbl_operaciones.text())
        print(resultado)
        self.lbl_resultado.setText(str(resultado))
        self.historial()

    def historial(self):
        self.txt_edit.append(f"{self.lbl_operaciones.text()} = {self.lbl_resultado.text()}")

    def borrar(self):
        self.lbl_operaciones.setText(self.lbl_operaciones.text()[:-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec_())