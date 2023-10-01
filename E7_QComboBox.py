from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, \
    QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Aplication(QWidget):
    def __init__(self):
        super(Aplication,self).__init__()
        self.resize(250,250)
        self.setWindowTitle("QComboBox")
        self.display_widgets()

    def display_widgets(self):
        self.lbl_titulo = QLabel("Escoge los articulos")
        self.lbl_titulo.setFont(QFont("Arial",20))
        self.lbl_titulo.setAlignment(Qt.AlignCenter)

        hlyt_combobox = QHBoxLayout()
        self.lista_comida = {"Escoge producto":0,"Huevo":17,"Sandwich":20,"Queso":9}
        cobox_comida1 = QComboBox(self)
        cobox_comida2 = QComboBox(self)
        cobox_comida1.addItems(self.lista_comida)
        cobox_comida2.addItems(self.lista_comida)
        hlyt_combobox.addWidget(cobox_comida1)
        hlyt_combobox.addWidget(cobox_comida2)

        self.lbl_productos = QLabel("Escoge dos productos",self)
        self.lbl_total = QLabel("Total: $")
        self.lbl_total.setFont(QFont("Arial",13))
        self.lbl_total.setAlignment(Qt.AlignRight)

        self.btn_pagar = QPushButton("Pagar")
        self.btn_pagar.close()

        self.spbox1 = QSpinBox(self)
        self.spbox2 = QSpinBox(self)

        self.spbox1.setRange(1,10)
        self.spbox2.setRange(1,10)
        self.spbox1.setPrefix("Cantidad: ")
        self.spbox2.setPrefix("Cantidad: ")
        hlyt_spbox = QHBoxLayout()
        hlyt_spbox.addWidget(self.spbox1)
        hlyt_spbox.addWidget(self.spbox2)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.addWidget(self.lbl_titulo)
        vlyt_principal.addLayout(hlyt_combobox)
        vlyt_principal.addLayout(hlyt_spbox)
        vlyt_principal.addStretch(1)
        vlyt_principal.addWidget(self.lbl_productos)
        vlyt_principal.addWidget(self.lbl_total)
        vlyt_principal.addWidget(self.btn_pagar)

        self.seleccion1 = ""
        self.seleccion2 = ""

        cobox_comida1.activated[str].connect(self.escogido1)
        cobox_comida2.activated[str].connect(self.escogido2)
        self.spbox1.valueChanged.connect(self.fun_seleccion)
        self.spbox2.valueChanged.connect(self.fun_seleccion)

    def escogido1(self, seleccion):
        if seleccion != "Escoge producto":
            self.seleccion1 = seleccion
            self.fun_seleccion()

    def escogido2(self,seleccion):
        if seleccion != "Escoge producto":
            self.seleccion2 = seleccion
            self.fun_seleccion()

    def fun_seleccion(self):
        cantidad1 = self.spbox1.value()
        cantidad2 = self.spbox2.value()
        try:
            self.lbl_total.setText(f"Total ${(self.lista_comida[self.seleccion1]*cantidad1) + (cantidad2*self.lista_comida[self.seleccion2])}")
            self.lbl_productos.setText(f"Has escogido: {self.seleccion1} y {self.seleccion2}")
            self.btn_pagar.show()
        except:
            self.lbl_productos.setText("Escoja el segundo producto")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_())