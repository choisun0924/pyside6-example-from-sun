import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

os.system("pyside6-uic ui/main.ui > ui_main.py")
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(mainApp.exec())