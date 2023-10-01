from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QButtonGroup, QCheckBox
import sys

class Aplication(QWidget):
    def __init__(self):
        super(Aplication,self).__init__()
        box = QHBoxLayout(self)
        grupo = QButtonGroup(self)

        btn1 = QPushButton("1",self)
        btn2 = QCheckBox("2",self)

        box.addWidget(btn1)
        box.addWidget(btn2)

        grupo.addButton(btn1)
        grupo.addButton(btn2)

        grupo.buttonClicked.connect(self.clickeando)

    def clickeando(self,boton):
        print(f"El boton presionado ha sido {boton.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_())