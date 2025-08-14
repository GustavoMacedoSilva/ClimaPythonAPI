from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QErrorMessage
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
from weatherAPI import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pesquisar Clima")
        self.setGeometry(600, 200, 700, 700)
        self.label_title = QLabel("Clima", self)
        self.button = QPushButton("Pesquisar", self)
        self.cidade = QLineEdit(self)
        self.terminal = QLabel("", self)
        self.setWindowIcon(QIcon("./clima.png"))
        self.initUI()
        
        # label = QLabel("Clima", self)
        # label.setFont(QFont("Arial", 40))
        # label.setGeometry(0, 0, 700, 100)

        # label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        
    
    def initUI(self):
        self.label_title.setFont(QFont("Arial", 40))
        self.label_title.setStyleSheet("color: white;"
                            "background-color: #abdbe3;"
                            "font-weight: bold;")
        self.label_title.setGeometry(0, 0, 700, 100)
        
        self.button.setGeometry(250, 300, 200, 100)
        self.button.setStyleSheet("font-size: 30px")
        self.button.clicked.connect(self.on_click)
        
        self.cidade.setGeometry(225, 180, 250, 50)
        self.cidade.setPlaceholderText("Digite o nome da cidade")
        
        self.terminal.setGeometry(125, 450, 450, 100)
        self.terminal.setStyleSheet("background-color: black;"
                                    "color: white;"
                                    "font-style: italic;")
        self.terminal.setAlignment(Qt.AlignTop)
        self.terminal.setText("Terminal")
    
    def on_click(self):
        
        cidade_escolhida = self.cidade.text()
        if cidade_escolhida == "":
            error_vazio = QErrorMessage()
            error_vazio.showMessage("Digite o nome da cidade")
            error_vazio.exec_()
        else:
            temperatura = buscarClima(cidade_escolhida)
            self.terminal.setText(f"A cidade {cidade_escolhida} está com uma temperatura de {temperatura}")
            
            