from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QTextEdit, \
    QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QFormLayout, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Aplication(QWidget):
    def __init__(self):
        super(Aplication,self).__init__()
        self.resize(300,400)
        self.setWindowTitle("Hospital")
        self.display_widgets()

    def display_widgets(self):
        lbl_titulo = QLabel("Cita Medica",self)
        lbl_titulo.setAlignment(Qt.AlignCenter)
        lbl_titulo.setFont(QFont("Arial",20))

        lned_nombre = QLineEdit(self)
        lned_direccion = QLineEdit(self)
        lned_telefono = QLineEdit(self)
        lned_telefono.setInputMask(("000-000-000;"))

        hlyt_edades = QHBoxLayout()

        lbl_edad = QLabel("Edad")
        spbox_edad = QSpinBox(self)
        spbox_edad.setRange(1, 110)

        lbl_altura = QLabel("Altura")
        lned_altura = QLineEdit(self)
        lned_altura.setPlaceholderText("cm")

        lbl_peso = QLabel("Peso")
        lned_peso = QLineEdit(self)
        lned_peso.setPlaceholderText("kg")

        hlyt_edades.addWidget(lbl_edad)
        hlyt_edades.addWidget(spbox_edad)
        hlyt_edades.addWidget(lbl_altura)
        hlyt_edades.addWidget(lned_altura)
        hlyt_edades.addWidget(lbl_peso)
        hlyt_edades.addWidget(lned_peso)

        cobox = QComboBox(self)
        cobox.addItems(["Femenino","Masculino","Sin especificar"])

        txed_cita = QTextEdit(self)
        txed_cita.setPlaceholderText("Especifique su cita")

        cobox_sangre = QComboBox(self)
        cobox_sangre.addItems(["A","B","AB","0","Sin especificar"])

        hlyt_hora = QHBoxLayout()
        spbox_hora = QSpinBox(self)
        spbox_hora.setRange(1, 12)
        cobox_min = QComboBox(self)
        cobox_min.addItems([":00",":15",":30",":45"])
        cobox_dn = QComboBox(self)
        cobox_dn.addItems(["AM","PM"])
        hlyt_hora.addWidget(spbox_hora)
        hlyt_hora.addWidget(cobox_min)
        hlyt_hora.addWidget(cobox_dn)

        envio_datos = QPushButton("Enviar Datos")
        envio_datos.clicked.connect(self.close)

        flyt_principal = QFormLayout(self)
        flyt_principal.addRow(lbl_titulo)
        flyt_principal.addRow("Nombre", lned_nombre)
        flyt_principal.addRow("Direccion", lned_direccion)
        flyt_principal.addRow("Telefono", lned_telefono)
        flyt_principal.addRow(hlyt_edades)
        flyt_principal.addRow("Genero",cobox)
        flyt_principal.addRow(txed_cita)
        flyt_principal.addRow("Tipo de sangre",cobox_sangre)
        flyt_principal.addRow("Hora",hlyt_hora)
        flyt_principal.addRow(envio_datos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_())