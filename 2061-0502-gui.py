import sys
import csv
import urllib.parse
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QDesktopServices

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # window title
        self.setWindowTitle("GUI-Programmierung")
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # menu bar
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        viewmenu = menubar.addMenu("View")

        # connect action buttons to functions
        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        load = QAction("Load", self)
        load.triggered.connect(self.menu_load)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)
        map = QAction("Map", self)
        map.triggered.connect(self.menu_view)

        # add action buttons to menubar
        filemenu.addAction(save)
        filemenu.addAction(load)
        filemenu.addAction(quit)
        viewmenu.addAction(map)
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # form fields
        layout = QFormLayout()
        
        # build text inputs
        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.datumDateEdit = QDateEdit()
        
        # build combo box
        self.landComboBox = QComboBox()
        self.landComboBox.addItems(["Schweiz", "Deutschland", "Österreich"])
        
        # build button
        self.buttonMap = QPushButton("Auf Karte zeigen")
        self.buttonMap.clicked.connect(self.view_map)
        
        self.buttonLoad = QPushButton("Laden")
        self.buttonLoad.clicked.connect(self.load_file)        
        
        self.buttonSave = QPushButton("Speichern")
        self.buttonSave.clicked.connect(self.write_file)
        
        # add layout fields
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtsdatum:", self.datumDateEdit)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.landComboBox)
        layout.addRow(self.buttonLoad)
        layout.addRow(self.buttonSave)
        layout.addRow(self.buttonMap)
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # vorgegeben zum applikationsstart
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        
    # menu bar functions    
    def menu_save(self):
        self.write_file()
        
    def menu_load(self):
        self.load_file()
        
    def menu_load(self):
        self.load_file()

    def menu_quit(self):
        self.close()  
        
    def menu_view(self):
        self.view_map()
        
    # form functions
    def write_file(self):

        # load form data to array
        formfields = []
        formfields.append(self.vornameLineEdit.text())
        formfields.append(self.nameLineEdit.text())
        formfields.append(self.datumDateEdit.text())
        formfields.append(self.adresseLineEdit.text())
        formfields.append(self.plzLineEdit.text())
        formfields.append(self.ortLineEdit.text())
        formfields.append(self.landComboBox.currentText())

        # write array to csv file
        file = open("output.csv", "w", encoding="utf-8")
        writer = csv.writer(file, delimiter=",", lineterminator="\n")
        writer.writerow(formfields)
        file.close()
        
    def load_file(self):
        
        formfields = []
        
        # read array from csv file
        file = open("output.csv", "r", encoding="utf-8")
        reader = csv.reader(file, delimiter=",", lineterminator="\n")
        for row in reader:
            formfields = row
        file.close()
        
        # fill form with array data
        self.vornameLineEdit.setText(formfields[0]) 
        self.nameLineEdit.setText(formfields[1])
        self.adresseLineEdit.setText(formfields[3])
        self.plzLineEdit.setText(formfields[4])
        self.ortLineEdit.setText(formfields[5])
        self.landComboBox.setCurrentText(formfields[6])
        
        dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat) 
        self.datumDateEdit.setDate(QDate.fromString(formfields[2], dformat))
        
    def view_map(self):
        
        url = 'https://www.google.ch/maps/place/'
        
        if self.adresseLineEdit.text():
            url += self.adresseLineEdit.text() + '+'
        if self.plzLineEdit.text():
            url += self.plzLineEdit.text() + '+'
        if self.ortLineEdit.text():
            url += self.ortLineEdit.text() + '+'
        if self.landComboBox.currentText():
            url += self.landComboBox.currentText()
        
        urllib.parse.quote(url)
        
        QDesktopServices.openUrl(QUrl(url))
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# vorgegeben zum applikationsstart        
def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()