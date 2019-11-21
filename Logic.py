
from PyQt5.QtWidgets import QMainWindow
from ABC import Ui_MainWindow      # UI
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import subprocess


class MainWindow(QMainWindow, Ui_MainWindow):  
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        

    def Push(self):
        print("Push")
        PY=self.lineEdit_output.text()
        UI=self.lineEdit_inout.text()
        PY=PY.replace("/","\\")
        UI=UI.replace("/","\\")
        CMD="pyuic5 -x "+UI+" -o "+PY
        print("CMD=",CMD)
        #os.system(CMD)  
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        #si.wShowWindow = subprocess.SW_HIDE # default
        subprocess.call(CMD,startupinfo=si,shell=True)
        
        # https://stackoverflow.com/questions/7006238/how-do-i-hide-the-console-when-i-use-os-system-or-subprocess-call
        # https://blog.csdn.net/u014094184/article/details/80085336
        
        self.listWidget.addItem("Finish")
        
    def UIpath(self):
        print("UIpath")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter( QDir.Files)
        if dlg.exec_():
            filenames= dlg.selectedFiles()
            print("filenames=",filenames)
            self.lineEdit_inout.setText(filenames[0])

    def PYpath(self):
        print("PYpath")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter( QDir.Files)
        if dlg.exec_():
            filenames= dlg.selectedFiles()
            print("filenames=",filenames)
            self.lineEdit_output.setText(filenames[0])

'''        
    def sbt_exit(self):
        self.close()
'''      
        

        