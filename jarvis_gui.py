from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
import sys

# Dummy response logic to simulate your AI
from datetime import datetime
def ask_jarvis(prompt):
    if "time" in prompt.lower():
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
    else:
        return f"You asked: {prompt}"

class JarvisGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jarvis - Virtual Assistant")
        self.setGeometry(100, 100, 600, 400)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #1e1e2f; color: white;")
        font = QFont("Segoe UI", 12)

        layout = QVBoxLayout()

        self.label = QLabel("🤖 Ask Jarvis anything:")
        self.label.setFont(font)
        layout.addWidget(self.label)

        self.input = QLineEdit()
        self.input.setFont(font)
        self.input.setPlaceholderText("e.g., What's the weather?")
        self.input.setStyleSheet("background-color: #2e2e3f; color: white; padding: 6px; border-radius: 10px;")
        layout.addWidget(self.input)

        self.button = QPushButton("Ask")
        self.button.setFont(font)
        self.button.setStyleSheet("background-color: #0078d7; color: white; padding: 8px; border-radius: 10px;")
        self.button.clicked.connect(self.respond)
        layout.addWidget(self.button)

        self.output = QTextEdit()
        self.output.setFont(font)
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: #2e2e3f; color: #9efeff; padding: 10px; border-radius: 10px;")
        layout.addWidget(self.output)

        self.setLayout(layout)

    def respond(self):
        user_input = self.input.text()
        if user_input.strip():
            response = ask_jarvis(user_input)
            self.output.append(f"🧑 You: {user_input}")
            self.output.append(f"🤖 Jarvis: {response}\n")
            self.input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JarvisGUI()
    window.show()
    sys.exit(app.exec_())
