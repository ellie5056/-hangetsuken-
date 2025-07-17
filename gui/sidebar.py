from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QMainWindow
from PyQt6.QtCore import Qt, pyqtSignal

class Sidebar(QMainWindow):
    toggle_sidebar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setFixedWidth(200)
        self.setStyleSheet("""
            QWidget {
                background-color: #b2b2b2
                border-right: 1px solid black;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #aa0000;
                color: white;
                border: none;
                padding: 15px;
                text-align: center;
                font-size: 16px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #2980b0
            }
            QPushButton#toggleButton {
                background-color: #bb0000
                text-align: center;
                font-size: 16px;
                margin-top: 10px
            }
            QPushButton#toggleButton:hover {
                background-color: #cbacba;
            }
        """)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.buttons = {}

        items = ["System", "Weather", "Games", "Network", "Calendar", "Media"]

        for item_name in items:
            btn = QPushButton(item_name)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.layout.addWidget(btn)
            self.buttons[item_name] = btn

        self.layout.addStretch(1)

        self.toggle_button = QPushButton("Toggle Sidebar")
        self.toggle_button.setObjectName("toggle_button")
        self.toggle_button.clicked.connect(self.toggle_sidebar_requested.emit)
        self.layout.addWidget(self.toggle_button)