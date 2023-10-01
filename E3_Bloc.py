from PyQt5.QtWidgets import QApplication, QWidget,QTextEdit, QFileDialog, QPushButton, QMessageBox
import sys

class Aplication(QWidget):
    def __init__(self):
        super(Aplication,self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(500,500)
        self.setWindowTitle("Notepad")
        self.display_widget()

    def display_widget(self):
        self.btn_borrar = QPushButton("Borrar", self)
        self.btn_borrar.move(100,20)
        self.btn_borrar.clicked.connect(self.borrar)

        self.btn_save = QPushButton("Guardar", self)
        self.btn_save.move(300, 20)
        self.btn_save.clicked.connect(self.save)

        self.editor = QTextEdit(self)
        self.editor.resize(300,400)
        self.editor.move(100,80)

        self.btn_open = QPushButton("Abrir", self)
        self.btn_open.move(200, 20)
        self.btn_open.clicked.connect(self.open)

    def borrar(self):
        pregunta = QMessageBox.question(self,"Clear", "¿Seguro?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if pregunta == QMessageBox.Yes:
            self.editor.clear()
        else:
            pass

    def save(self):
        notepad_text = self.editor.toPlainText()
        ruta,tipo = QFileDialog.getSaveFileName(self,"Guardar archivo","",
                                                "ALLFILES (*);; Archivo de texto (*.txt)")
        try:
            with open(ruta,"w") as f:
                f.write(notepad_text)
        except:
            pass

    def open(self):
        ruta,tipo = QFileDialog.getOpenFileName(self,"Abrir archivo","",
                                                "ALLFILES (*);; Archivo de texto (*.txt)")
        try:
            with open(ruta,"r") as f:
                extraccion = f.read()
                self.editor.setText(extraccion)
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_())