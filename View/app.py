import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QLineEdit, QPushButton
from Controller.csvParser import csvUsername, writeUsername
from Controller.askQuestion import askQuestions
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatCSIfElse")
        self.setGeometry(100, 200, 500, 200)

        self.layout = QVBoxLayout()
        self.nameInput = QLineEdit()
        self.chatbotOutputLabel = QLabel()
        self.chatbotOutputLabel.setText('Enter your name to start chatting!')


        self.layout.addWidget(self.chatbotOutputLabel)

        self.layout.addWidget(self.nameInput)
        self.nameInput.setStyleSheet("padding: 10px;")
        
        self.nameButton = QPushButton('Enter')
        self.layout.addWidget(self.nameButton)
        self.nameButton.setStyleSheet("padding: 12px;")
        self.nameButton.clicked.connect(self.nameButtonClicked) 

        # Set the layout for the main window
        self.setLayout(self.layout)

    def nameButtonClicked(self):
        # ถ้าเคยใช้งานมาแล้วจะขึ้นข้อความคนละแบบ กับคนที่ไม่เคยใข้งานมาก่อน
        self.name = self.nameInput.text()
        data = csvUsername()
        if self.name in data:
            self.chatbotOutputLabel.setText(f'Welcome again {self.name}! Any things else today?')
        else:
            self.chatbotOutputLabel.setText(f'Welcome {self.name} to ChatCSIfElse, the best chat AI in the world! What can I help you ?')
            writeUsername(self.name)
        self.resetInputFields()
        self.nameInput.deleteLater()
        self.nameButton.deleteLater()

        self.askQuestionsField(self.name)

    def askQuestionsField(self, name):
        self.questionInput = QLineEdit()
        self.layout.addWidget(self.questionInput)
        self.questionInput.setStyleSheet("padding: 10px;")

        self.askButton = QPushButton('Ask')
        self.layout.addWidget(self.askButton)
        self.askButton.setStyleSheet("padding: 12px;")
        self.askButton.clicked.connect(self.askButtonClicked)

        self.quitButton = QPushButton('Quit')
        self.layout.addWidget(self.quitButton)
        self.quitButton.setStyleSheet("padding: 12px;")
        self.quitButton.clicked.connect(self.close)

    def askButtonClicked(self):
        question = self.questionInput.text()
        answer = askQuestions(self.name,question)
        self.chatbotOutputLabel.setText(answer)
        self.questionInput.clear()

    def resetInputFields(self):
        self.nameInput.clear()

