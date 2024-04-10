import sys
import csv
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # window title
        self.setWindowTitle("GUI-Programmierung")
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # menu bar
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        # connect action buttons to functions
        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        # add action buttons to menubar
        filemenu.addAction(save)
        filemenu.addAction(quit)
        
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
        self.button = QPushButton("Speichern")
        self.button.clicked.connect(self.write_file)
        
        # add layout fields
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtsdatum:", self.datumDateEdit)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.landComboBox)
        layout.addRow(self.button)
        
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

    def menu_quit(self):
        self.close()  
        
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
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# vorgegeben zum applikationsstart        
def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()