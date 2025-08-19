from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QErrorMessage
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
from weatherAPI import *
import sys, os

def resource_path(relative_path):
    """Retorna o caminho absoluto do recurso (funciona no exe e no dev)"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)  # Executável
    return os.path.join(os.path.abspath("."), relative_path)  # Código normal

class ApiKeyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("API key")
        self.setGeometry(1300, 200, 300, 150)
        self.layout = QVBoxLayout()
        self.chave = QLineEdit(self)
        self.done_button = QPushButton("Done", self)
        self.weather_key = ""
        self.initUI()
        
    def initUI(self):
        self.chave.setPlaceholderText("API key")
        self.chave.setEchoMode(QLineEdit.Password)
        self.done_button.setStyleSheet("font-size: 30px")
        self.done_button.clicked.connect(self.on_click)
        self.layout.addWidget(self.chave)
        self.layout.addWidget(self.done_button)
        self.setLayout(self.layout)
    
    def on_click(self):
        if self.chave.text() == "":
            error_vazio = QErrorMessage()
            error_vazio.showMessage("Digite a API key cara pelo amor ne")
            error_vazio.exec_()
        else:
            self.weather_key = self.chave.text()
            self.hide()
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pesquisar Clima")
        self.setGeometry(600, 200, 700, 700)
        self.label_title = QLabel("Clima", self)
        self.button = QPushButton("Pesquisar", self)
        self.cidade = QLineEdit(self)
        self.terminal = QLabel("", self)
        self.api_button = QPushButton("API key", self)
        self.setWindowIcon(QIcon("clima.png"))
        self.api_key = ""
        self.apiwindow = None
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
        
        self.api_button.setGeometry(250, 600, 200, 70)
        self.api_button.setStyleSheet("font-size: 30px")
        self.api_button.clicked.connect(self.on_click_api_button)
        
        
    def on_click_api_button(self):
        if self.apiwindow == None:
            self.apiwindow = ApiKeyWindow()
            self.apiwindow.show()
        else:
            self.apiwindow.show()
            
                
    
    def on_click(self):
        if self.apiwindow == None or self.apiwindow.weather_key == "":
            error_key = QErrorMessage()
            error_key.showMessage("Coloque sua API key antes de prosseguir")
            error_key.exec_()
        else:
            cidade_escolhida = self.cidade.text()
            if cidade_escolhida == "":
                error_vazio = QErrorMessage()
                error_vazio.showMessage("Digite o nome da cidade")
                error_vazio.exec_()
            else:
                temperatura = buscarClima(cidade_escolhida, self.apiwindow.weather_key)
                self.terminal.setText(f"A cidade {cidade_escolhida} está com uma temperatura de {temperatura}")
                humidade = buscarHumidade(cidade_escolhida, self.apiwindow.weather_key)
    
    def closeEvent(self, event):
        if self.apiwindow != None:
            self.apiwindow.close()
        else:
            pass