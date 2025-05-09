from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Label_BadID.hide()
        self.Label_GoodID.hide()
        self.Label_Thanks.hide()
        self.Label_Write1.hide()
        self.Label_Write2.hide()
        self.Button_WI_P.hide()
        self.Button_WI_VP.hide()
        self.Input_P.hide()
        self.Input_VP.hide()
        self.Push_P1.hide()
        self.Push_P2.hide()
        self.Push_VP2.hide()
        self.Push_VP1.hide()
        self.Label_P.hide()
        self.Label_VP.hide()
        self.Label_Candidate.hide()
        self.Button_Submit.hide()
        self.Button_Sumbit_ID.clicked.connect(lambda : self.submit_id())
        self.Button_WI_P.clicked.connect(lambda : self.show_pres())
        self.Button_WI_VP.clicked.connect(lambda : self.show_vice())
        self.Button_Submit.clicked.connect(lambda : self.submit())
        self.Push_P1.clicked.connect(lambda : self.hide_WI_P())
        self.Push_P2.clicked.connect(lambda : self.hide_WI_P())
        self.Push_VP1.clicked.connect(lambda : self.hide_WI_VP())
        self.Push_VP2.clicked.connect(lambda : self.hide_WI_VP())

    def submit_id(self):
        x = self.Input_ID.text()
        good_ID = True
        x = int(x)
        if x < 1000 or x > 9999:
            good_ID = False
            self.Label_BadID.show()
            self.Input_ID.clear()
        else:
            x = str(x)
            with open('ballot_results.csv', 'r') as voter_ids:
                content = csv.reader(voter_ids)
                for line in content:
                    if len(line) > 0:
                        if line[0] == x:
                            good_ID = False
                            self.Label_BadID.show()
                            self.Input_ID.clear()

        if good_ID == True:
            self.Label_BadID.hide()
            self.Label_GoodID.show()
            self.Push_P1.show()
            self.Push_P2.show()
            self.Push_VP2.show()
            self.Push_VP1.show()
            self.Label_P.show()
            self.Label_VP.show()
            self.Button_Submit.show()
            self.Button_WI_P.show()
            self.Button_WI_VP.show()
            self.Label_Candidate.show()

    def show_pres(self):
        self.Label_Write1.show()
        self.Input_P.show()

    def show_vice(self):
        self.Label_Write2.show()
        self.Input_VP.show()

    def hide_WI_P(self):
        self.Label_Write1.hide()
        self.Input_P.hide()

    def hide_WI_VP(self):
        self.Label_Write2.hide()
        self.Input_VP.hide()

    def submit(self):
        with open('ballot_results.csv', 'a', newline="") as ballot_output:
            content = csv.writer(ballot_output)
            if self.Push_P1.isChecked():
                if self.Push_VP1.isChecked():
                    content.writerow([self.Input_ID.text(), '1', '1'])
                elif self.Push_VP2.isChecked():
                    content.writerow([self.Input_ID.text(), '1', '2'])
                else:
                    content.writerow([self.Input_ID.text(), '1', self.Input_VP.text()])
            elif self.Push_P2.isChecked():
                if self.Push_VP1.isChecked():
                    content.writerow([self.Input_ID.text(), '2', '1'])
                elif self.Push_VP2.isChecked():
                    content.writerow([self.Input_ID.text(), '2', '2'])
                else:
                    content.writerow([self.Input_ID.text(), '2', self.Input_VP.text()])
            else:
                if self.Push_VP1.isChecked():
                    content.writerow([self.Input_ID.text(), self.Input_P.text(), '1'])
                elif self.Push_VP2.isChecked():
                    content.writerow([self.Input_ID.text(), self.Input_P.text(), '2'])
                else:
                    content.writerow([self.Input_ID.text(), self.Input_P.text(), self.Input_VP.text()])
        self.Label_Thanks.show()

