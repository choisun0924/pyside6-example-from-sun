import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

os.system("pyside6-uic ui/main.ui > ui_main.py")
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.testButton)

    def testButton(self):
        print('testButton')

if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(mainApp.exec())