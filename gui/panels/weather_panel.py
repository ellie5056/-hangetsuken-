from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class WeatherPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Weather Panel"))