from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QVBoxLayout, QHBoxLayout, QButtonGroup, QCheckBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Aplication(QWidget):
    def __init__(self):
        super(Aplication,self).__init__()
        self.resize(300,400)
        self.setWindowTitle("Encuesta")
        self.display_widgets()

    def display_widgets(self):
        lbl_titulo = QLabel("Encuesta Curso", self)
        lbl_titulo.setFont(QFont("Arial",20))
        lbl_titulo.setAlignment(Qt.AlignCenter)

        lbl_pregunta = QLabel("Puntuacion del Curso?",self)
        lbl_pregunta.setFont(QFont("Arial",10))
        lbl_pregunta.setAlignment(Qt.AlignCenter)

        calificaciones = ["Muy Malo", "Malo", "Bueno", "Muy Bueno"]
        hlyt_lbl_cal = QHBoxLayout()

        for cal in calificaciones:
            lbl_cal = QLabel(cal,self)
            hlyt_lbl_cal.addWidget(lbl_cal)

        hlyt_chbox = QHBoxLayout()
        grupo_chbox = QButtonGroup()
        for cal in range(len(calificaciones)):
            chbox = QCheckBox(str(cal),self)
            grupo_chbox.addButton(chbox)
            hlyt_chbox.addWidget(chbox)

        btn_close = QPushButton("Cerrar",self)
        btn_close.clicked.connect(self.close)
        grupo_chbox.buttonClicked.connect(self.click)

        vlyt_principal = QVBoxLayout()
        vlyt_principal.addWidget(lbl_titulo)
        vlyt_principal.addWidget(lbl_pregunta)
        vlyt_principal.addStretch(1)
        vlyt_principal.addLayout(hlyt_lbl_cal)
        vlyt_principal.addLayout(hlyt_chbox)
        vlyt_principal.addStretch(2)
        vlyt_principal.addWidget(btn_close)
        self.setLayout(vlyt_principal)

    def click(self, texto):
        print(f"La casilla {texto.text()} ha sido modificada")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_())
