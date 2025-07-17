from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QStackedWidget, QSizePolicy
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PyQt6.QtGui import QIcon

from gui.panels.weather_panel import WeatherPanel
from gui.sidebar import Sidebar
from gui.panels.system_panel import SystemPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.resize(1920, 1080)

        self.sidebar_collapsed_width = 60
        self.sidebar_expanded_ratio = 0.20
        self.is_sidebar_expanded = True

        self.buttons = {}

        container = QWidget()
        layout = QHBoxLayout()
        container.setLayout(layout)

        self.sider = Sidebar()

        self.sidebar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.sidebar.setFixedWidth(int(self.width() * self.sidebar_expanded_ratio))

        self.stack = QStackedWidget()
        self.stack.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.stack.setStyleSheet("background-color: white; border-radius: 5px; padding: 5px;")

        self.panels = {
            "SystemPanel": SystemPanel()
            "WeatherPanel": QLabel("Weather")
            "GamesPanel": QLabel("Games")
            "NetworkPanel": QLabel("Network")
            "CalendarPanel": QLabel("Calendar")
            "MediaPanel": QLabel("Media")
        }