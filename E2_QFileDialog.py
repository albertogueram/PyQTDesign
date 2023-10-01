from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton
import sys

class Aplication(QWidget):
    def __init__(self):
        super(Aplication,self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(500,500)
        self.setWindowTitle("QFileDialog")
        self.display_widget()

    def display_widget(self):
        self.btn_abrir = QPushButton("Abrir", self)
        self.btn_abrir.move(215,20)
        self.btn_abrir.clicked.connect(self.open)

        self.btn_save = QPushButton("Guardar", self)
        self.btn_save.move(215,100)
        self.btn_save.clicked.connect(self.save)

    def open(self):
        file_name = QFileDialog.getOpenFileName(self,"Abrir archivos",
                                                "../../../../../alber/Desktop",
                                                "AllFiles(*);;Archivos de text(*.pdf")
        print(file_name)

    def save(self):
        file_name = QFileDialog.getSaveFileName(self,"Abrir archivos",
                                                "../../../../../alber/Desktop",
                                                "AllFiles(*);;Archivos de text(*.pdf")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_())