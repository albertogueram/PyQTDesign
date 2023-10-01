from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton
import sys

class Aplication(QWidget):
    def __init__(self):
        super(Aplication,self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("QTextEdit")
        self.display_widget()

    def display_widget(self):
        self.btn_borrar = QPushButton("Borrar", self)
        self.btn_salto = QPushButton("Salto", self)
        self.btn_borrar.move(215,20)

        self.editor = QTextEdit(self)
        self.editor.resize(300,300)
        self.editor.move(100,100)

        self.btn_borrar.clicked.connect(self.borrar)
        self.btn_salto.clicked.connect(self.salto_linea)

    def borrar(self):
        self.editor.clear()

    def salto_linea(self):
        print(self.editor.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_())