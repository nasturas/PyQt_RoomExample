import sys
from myroomgui import Ui_Form
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from datetime import datetime

class room(QWidget):
    def __init__(self, roomNr, parent=None): 
        super(room, self).__init__(parent)
        self.__isFree = True
        self.ui = Ui_Form() 
        self.ui.setupUi(self)
        self.ui.checkInOutButton.clicked.connect(self.check_in)
        self.ui.checkInDate.setText("Liber")
        self.ui.checkInDate.adjustSize()
        self.ui.roomNumberLabel.setText('Camera: '+roomNr)
        self.ui.roomNumberLabel.adjustSize()
        self.ui.cleanStatusLabel.setText("Curata")
        self.ui.cleanStatusLabel.adjustSize()

        self.ui.cleanedButton.clicked.connect(self.cleanUp)
        self.ui.cleanedButton.setText("Curatat camera")
        self.ui.cleanedButton.adjustSize()
        self.ui.checkInOutButton.setText("Cazare/Decazare")
        self.ui.checkInOutButton.adjustSize()
        self.adjustSize()

    def check_in(self):
        if(self.__isFree):
            self.ui.checkInDate.setText( 'Cazat la: '+datetime.now().strftime('%Y-%m-%d'))
            self.ui.checkInDate.adjustSize()
            self.__isFree = False
        else:
            self.ui.checkInDate.setText( 'Liber')
            self.ui.checkInDate.adjustSize()
            self.ui.cleanStatusLabel.setText("Necuratita")
            self.ui.cleanStatusLabel.adjustSize()

    def cleanUp(self):
        self.ui.cleanStatusLabel.setText("Curata")
        self.ui.cleanStatusLabel.adjustSize()
        self.__isFree = True

    def Get_IsFree(self):
        return self.__isFree

class DefinireHotel(QWidget):
    def __init__(self, parent=None):
        super(DefinireHotel, self).__init__(parent)

        layout = QVBoxLayout() 
        label = QLabel("miau") 
        line_edit = QLineEdit() 
        button = QPushButton("ready") 
        layout.addWidget(label) 
        layout.addWidget(line_edit) 
        layout.addWidget(button)
        self.setLayout(layout)
        self.adjustSize()

# Definirea funcției principale
def main():
    app = QApplication(sys.argv)

    widget = QWidget()

    layout = QGridLayout(widget)

    nrCamere = 5
    rooms = []
    rand = 0
    col = 0
    for i in range(nrCamere):
        rooms.append(room(str(i)))        
        layout.addWidget(rooms[i], rand, col)
        col+=1
        if col == 3:
            col = 0
            rand+=1
    
    widget.adjustSize()
    widget.showMaximized()
    
    sys.exit(app.exec())

# Apelarea funcției principale
if __name__ == '__main__':
    main()
