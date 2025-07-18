from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
import sys

def launch_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    launch_app()
