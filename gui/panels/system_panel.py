from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class SystemPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("System Panel"))