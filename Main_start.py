import sys
from PyQt5.QtWidgets import QApplication
from Logic import MainWindow
from PyQt5.QtCore import QCoreApplication

if __name__ == "__main__":
    #app = QApplication(sys.argv)
    app = QCoreApplication.instance() # second not die
    if app is None:
        app = QApplication(sys.argv)
    mainWindow = MainWindow()  # Logic.py
    mainWindow.show()
    sys.exit(app.exec_())
   