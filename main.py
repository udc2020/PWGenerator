"""
============ PWGenerator ============
* By UltrasdzCoder 
* Python 3.9.5
* We Used PySide6 With QTDesiner
* And Also sys,time,csv 
"""

import sys
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from PySide6.QtUiTools import loadUiType
import src_img_rc

import time 

from  passgenerator import final_pass
from database import add_to_db , search_from_db

from mainui import Ui_MainWindow as MainUI

# main_window, _ = loadUiType("./mainui.ui")

class MainApp (QMainWindow, MainUI):
   def __init__(self):
      QMainWindow.__init__(self)
      self.setupUi(self)


      # ====== Buttons ====== #
      self.submitbtn.clicked.connect(self.add_to_db)
      self.generatepass.clicked.connect(self.generate_pass)
      self.getinfo.clicked.connect(self.search)

   # ====== Add Data to CSV ====== #
   def add_to_db(self):
      data = [self.website.text() , self.email.text() , self.password.text()]
   
      add_to_db(*data)
      
     
      time.sleep(1)
      self.website.setText("")
      self.email.setText("")
      self.password.setText("")
      
      
   # ====== Search From Csv ====== #
   def search(self):
      if self.web_search.text() == "":
         return 0
      data = search_from_db(self.web_search.text())
   
      self.lineEdit_5.setText(data[1])
      self.lineEdit_6.setText(data[2])
   
      
      
   # ====== Generate PassWord ====== #   
   def generate_pass(self):
      self.password.setText(final_pass())





def main():
    app = QApplication(sys.argv)
    win = MainApp()
    win.show()
    app.exec()


if "__main__" == __name__:
    main()
