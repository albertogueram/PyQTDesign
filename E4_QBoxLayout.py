from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
import sys

class Aplication(QWidget):
    def __init__(self):
        super(Aplication,self).__init__()
        ## box = QHBoxLayout(self)
        box = QVBoxLayout(self)
        boton = QPushButton("Press",self)

        box.addStretch()
        box.addWidget(boton)
        box.addStretch()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_())