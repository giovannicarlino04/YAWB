from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget

class YAWB(QMainWindow):

    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("Yet Another Web Browser - Giovanni Carlino")
        
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.urlbar = QTextEdit()
        self.urlbar.setMaximumHeight(30)
        
        self.homebtn = QPushButton("Home")
        self.homebtn.setMinimumHeight(30)
        self.gobtn = QPushButton("Vai")
        self.gobtn.setMinimumHeight(30)
        self.backbtn = QPushButton("<")
        self.backbtn.setMinimumHeight(30)
        self.forwbtn = QPushButton(">")
        self.forwbtn.setMinimumHeight(30)

        self.horizontal.addWidget(self.homebtn)
        self.horizontal.addWidget(self.urlbar)
        self.horizontal.addWidget(self.gobtn)
        self.horizontal.addWidget(self.backbtn)
        self.horizontal.addWidget(self.forwbtn)

        self.browser = QWebEngineView()

        self.homebtn.clicked.connect(lambda:self.navigate("https://www.google.com"))
        self.homebtn.clicked.connect(lambda:self.urlbar.setText("https://www.google.com"))

        self.gobtn.clicked.connect(lambda:self.navigate(self.urlbar.toPlainText()))
        self.backbtn.clicked.connect(self.browser.back)
        self.forwbtn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://www.google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.urlbar.setText(url)
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = YAWB()
app.exec()