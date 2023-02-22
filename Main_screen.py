from PyQt5 import QtCore, QtGui, QtWidgets
from Second_screen import Ui_MainWindoww
import os
import mysql.connector
import connection
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import datetime
date = datetime.date.today()
mydb = connection.mydb

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1346, 863)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Maintabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Maintabs.setGeometry(QtCore.QRect(10, 10, 1331, 821))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Maintabs.setFont(font)
        self.Maintabs.setObjectName("Maintabs")
        self.Maintabs.setStyleSheet("background-color: turquoise")
        self.Maintabs.setFont(font)
        valedatur = QRegExpValidator(QRegExp(r'[a-zA-Z]+'))
        self.Search_existing_and_added_patients = QtWidgets.QWidget()
        self.Search_existing_and_added_patients.setObjectName("Search_existing_and_added_patients")
        self.label = QtWidgets.QLabel(self.Search_existing_and_added_patients)
        self.label.setGeometry(QtCore.QRect(70, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Search_text = QtWidgets.QLineEdit(self.Search_existing_and_added_patients)
        self.Search_text.setGeometry(QtCore.QRect(70, 90, 511, 41))
        self.Search_text.setObjectName("lineEdit")
        self.Search_text.setStyleSheet("background-color: lightgrey")
        self.Search_text.setFont(font)
        self.Search = QtWidgets.QPushButton(self.Search_existing_and_added_patients,clicked = lambda : self.search_details()) #lambda function example
        self.Search.setGeometry(QtCore.QRect(590, 90, 131, 41))
        self.Search.setObjectName("Search")
        self.Search.setStyleSheet("background-color: lightgrey")
        self.Search.setFont(font)
        self.First_Name_search_filter = QtWidgets.QRadioButton(self.Search_existing_and_added_patients)
        self.First_Name_search_filter.setGeometry(QtCore.QRect(760, 100, 151, 21))
        self.First_Name_search_filter.setObjectName("First_Name_search_filter")
        self.First_Name_search_filter.setChecked(True)
        self.First_Name_search_filter.setFont(font)
        self.UID_search_filter = QtWidgets.QRadioButton(self.Search_existing_and_added_patients)
        self.UID_search_filter.setGeometry(QtCore.QRect(760, 130, 151, 21))
        self.UID_search_filter.setObjectName("UID_search_filter")
        self.UID_search_filter.setFont(font)
        self.Last_Name_Search_filter = QtWidgets.QRadioButton(self.Search_existing_and_added_patients)
        self.Last_Name_Search_filter.setGeometry(QtCore.QRect(760, 160, 151, 21))
        self.Last_Name_Search_filter.setObjectName("Last_Name_Search_filter")
        self.Last_Name_Search_filter.setFont(font)
        self.List_of_patients = QtWidgets.QTableWidget(self.Search_existing_and_added_patients)
        self.List_of_patients.setGeometry(QtCore.QRect(70, 200, 1201, 481))
        self.List_of_patients.setObjectName("List_of_patients")
        self.List_of_patients.setColumnCount(0)
        self.List_of_patients.setRowCount(0)
        self.List_of_patients.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.List_of_patients.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.List_of_patients.doubleClicked.connect(self.Second_screen_launch)
        self.List_of_patients.setStyleSheet("background-color: skyblue")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.List_of_patients.setFont(font)
        self.Search_result_label = QtWidgets.QLabel(self.Search_existing_and_added_patients)
        self.Search_result_label.setGeometry(QtCore.QRect(70, 160, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Search_result_label.setFont(font)
        self.Search_result_label.setObjectName("Search_result_label")
        self.pushButton = QtWidgets.QPushButton(self.Search_existing_and_added_patients,clicked = lambda : self.close_app())
        self.pushButton.setGeometry(QtCore.QRect(1080, 690, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: lightgrey")
        self.label_2 = QtWidgets.QLabel(self.Search_existing_and_added_patients)
        self.label_2.setGeometry(QtCore.QRect(1040, 30, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Maintabs.addTab(self.Search_existing_and_added_patients, "")
        self.Add_New_Patient = QtWidgets.QWidget()
        self.Add_New_Patient.setObjectName("Add_New_Patient")
        self.label_3 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_3.setGeometry(QtCore.QRect(1070, 30, 221, 101))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        fton = QtGui.QFont()
        fton.setPointSize(14)
        self.First_Name = QtWidgets.QLineEdit(self.Add_New_Patient)
        self.First_Name.setGeometry(QtCore.QRect(60, 70, 261, 41))
        self.First_Name.setObjectName("First_Name")
        self.First_Name.setValidator(valedatur)
        self.First_Name.setStyleSheet("background-color: lightgrey")
        self.First_Name.setFont(fton)
        self.Middle_Name = QtWidgets.QLineEdit(self.Add_New_Patient)
        self.Middle_Name.setGeometry(QtCore.QRect(60, 150, 261, 41))
        self.Middle_Name.setObjectName("Middle_Name")
        self.Middle_Name.setValidator(valedatur)
        self.Middle_Name.setStyleSheet("background-color: lightgrey")
        self.Middle_Name.setFont(fton)
        self.Last_name = QtWidgets.QLineEdit(self.Add_New_Patient)
        self.Last_name.setGeometry(QtCore.QRect(60, 230, 261, 41))
        self.Last_name.setObjectName("Last_name")
        self.Last_name.setValidator(valedatur)
        self.Last_name.setStyleSheet("background-color: lightgrey")
        self.Last_name.setFont(fton)
        validator = QRegExpValidator(QRegExp(r'[0-9]+'))
        self.Mobile_number1 = QtWidgets.QLineEdit(self.Add_New_Patient)
        self.Mobile_number1.setGeometry(QtCore.QRect(60, 420, 261, 41))
        self.Mobile_number1.setObjectName("Mobile_number1")
        self.Mobile_number1.setValidator(validator)
        self.Mobile_number1.setStyleSheet("background-color: lightgrey")
        self.Mobile_number1.setFont(fton)
        self.Mobile_number2 = QtWidgets.QLineEdit(self.Add_New_Patient)
        self.Mobile_number2.setGeometry(QtCore.QRect(60, 510, 261, 41))
        self.Mobile_number2.setObjectName("Mobile_number2")
        self.Mobile_number2.setValidator(validator)
        self.Mobile_number2.setStyleSheet("background-color: lightgrey")
        self.Mobile_number2.setFont(fton)
        self.Aadhaar_number = QtWidgets.QLineEdit(self.Add_New_Patient)
        self.Aadhaar_number.setGeometry(QtCore.QRect(60, 640, 261, 41))
        self.Aadhaar_number.setObjectName("Aadhaar_number")
        self.Aadhaar_number.setValidator(validator)
        self.Aadhaar_number.setStyleSheet("background-color: lightgrey")
        self.Aadhaar_number.setFont(fton)
        self.PAN_number = QtWidgets.QLineEdit(self.Add_New_Patient)
        self.PAN_number.setGeometry(QtCore.QRect(480, 70, 261, 41))
        self.PAN_number.setObjectName("PAN_number")
        self.PAN_number.setValidator(validator)
        self.PAN_number.setStyleSheet("background-color: lightgrey")
        self.PAN_number.setFont(fton)
        self.Doctorname = QtWidgets.QComboBox(self.Add_New_Patient)
        self.Doctorname.setGeometry(QtCore.QRect(820, 190, 241, 51))
        self.Doctorname.setObjectName("Doctorname")
        self.Doctorname.addItem("")
        self.Doctorname.addItem("")
        self.Doctorname.addItem("")
        self.Doctorname.addItem("")
        self.Doctorname.setStyleSheet("background-color: lightgrey")
        self.Doctorname.setFont(fton)
        self.Address = QtWidgets.QLineEdit(self.Add_New_Patient)
        self.Address.setGeometry(QtCore.QRect(490, 600, 381, 101))
        self.Address.setObjectName("Address")
        self.Address.setStyleSheet("background-color: lightgrey")
        self.Address.setFont(fton)
        self.Bloodgroup = QtWidgets.QComboBox(self.Add_New_Patient)
        self.Bloodgroup.setGeometry(QtCore.QRect(490, 350, 231, 51))
        self.Bloodgroup.setObjectName("Bloodgroup")
        self.Bloodgroup.addItem("")
        self.Bloodgroup.addItem("")
        self.Bloodgroup.addItem("")
        self.Bloodgroup.addItem("")
        self.Bloodgroup.addItem("")
        self.Bloodgroup.addItem("")
        self.Bloodgroup.addItem("")
        self.Bloodgroup.addItem("")
        self.Bloodgroup.setStyleSheet("background-color: lightgrey")
        self.Bloodgroup.setFont(fton)
        self.Male = QtWidgets.QRadioButton(self.Add_New_Patient)
        self.Male.setGeometry(QtCore.QRect(500, 460, 101, 20))
        self.Male.setObjectName("radioButton")
        self.Male.setStyleSheet("background-color: lightgrey")
        self.Male.setFont(fton)
        self.Female = QtWidgets.QRadioButton(self.Add_New_Patient)
        self.Female.setGeometry(QtCore.QRect(500, 490, 111, 20))
        self.Female.setObjectName("radioButton_2")
        self.Female.setStyleSheet("background-color: lightgrey")
        self.Female.setFont(fton)
        self.Others = QtWidgets.QRadioButton(self.Add_New_Patient)
        self.Others.setGeometry(QtCore.QRect(500, 520, 101, 20))
        self.Others.setObjectName("radioButton_3")
        self.Others.setStyleSheet("background-color: lightgrey")
        self.Others.setFont(fton)
        self.Date_of_Birth = QtWidgets.QDateEdit(self.Add_New_Patient)
        self.Date_of_Birth.setGeometry(QtCore.QRect(480, 200, 251, 51))
        self.Date_of_Birth.setObjectName("Date_of_Birth")
        self.Date_of_Birth.setStyleSheet("background-color: lightgrey")
        self.label_4 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_4.setGeometry(QtCore.QRect(60, 30, 161, 31))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(fton)
        self.label_5 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_5.setGeometry(QtCore.QRect(60, 120, 161, 31))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(fton)
        self.label_6 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_6.setGeometry(QtCore.QRect(60, 200, 161, 31))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(fton)
        self.label_7 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_7.setGeometry(QtCore.QRect(60, 390, 171, 31))
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(fton)
        self.label_8 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_8.setGeometry(QtCore.QRect(60, 480, 191, 31))
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(fton)
        self.label_9 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_9.setGeometry(QtCore.QRect(60, 610, 161, 31))
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(fton)
        self.label_10 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_10.setGeometry(QtCore.QRect(480, 40, 221, 31))
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(fton)
        self.label_11 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_11.setGeometry(QtCore.QRect(480, 170, 161, 31))
        self.label_11.setObjectName("label_11")
        self.label_11.setFont(fton)
        self.label_12 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_12.setGeometry(QtCore.QRect(490, 320, 161, 31))
        self.label_12.setObjectName("label_12")
        self.label_12.setFont(fton)
        self.label_13 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_13.setGeometry(QtCore.QRect(490, 570, 161, 31))
        self.label_13.setObjectName("label_13")
        self.label_13.setFont(fton)
        self.label_14 = QtWidgets.QLabel(self.Add_New_Patient)
        self.label_14.setGeometry(QtCore.QRect(820, 160, 161, 31))
        self.label_14.setObjectName("label_14")
        self.label_14.setFont(fton)
        self.inputerrormessege = QtWidgets.QLabel(self.Add_New_Patient)
        self.inputerrormessege.setGeometry(QtCore.QRect(950, 300, 401, 101))
        self.inputerrormessege.setText("")
        self.inputerrormessege.setObjectName("inputerrormessege")
        self.Add = QtWidgets.QPushButton(self.Add_New_Patient,clicked = lambda : self.Addpatient())
        self.Add.setGeometry(QtCore.QRect(1090, 700, 131, 51))
        self.Add.setObjectName("Add")
        self.Add.setStyleSheet("background-color: lightgrey")
        self.Add.setFont(fton)
        self.Maintabs.addTab(self.Add_New_Patient, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1346, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.Maintabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.default_load()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EMRsys"))
        self.label.setText(_translate("MainWindow", "Search:"))
        self.Search.setText(_translate("MainWindow", ">>"))
        self.First_Name_search_filter.setText(_translate("MainWindow", "First name"))
        self.UID_search_filter.setText(_translate("MainWindow", "UID"))
        self.Last_Name_Search_filter.setText(_translate("MainWindow", "Last name"))
        self.Search_result_label.setText(_translate("MainWindow", "Search Result:"))
        self.pushButton.setText(_translate("MainWindow", "Close"))
        self.label_2.setText(_translate("MainWindow", "EMRsys"))
        self.Maintabs.setTabText(self.Maintabs.indexOf(self.Search_existing_and_added_patients), _translate("MainWindow", "Search Patients"))
        self.label_3.setText(_translate("MainWindow", "EMRsys"))
        self.Doctorname.setItemText(0, _translate("MainWindow", "Dr Satish Kamat"))
        self.Doctorname.setItemText(1, _translate("MainWindow", "Dr Sunita Kamat"))
        self.Doctorname.setItemText(2, _translate("MainWindow", "Dr Sonal Bhalerao"))
        self.Doctorname.setItemText(3, _translate("MainWindow", "Dr"))
        self.Bloodgroup.setItemText(0, _translate("MainWindow", "N/A"))
        self.Bloodgroup.setItemText(1, _translate("MainWindow", "B+"))
        self.Bloodgroup.setItemText(2, _translate("MainWindow", "B-"))
        self.Bloodgroup.setItemText(3, _translate("MainWindow", "A+"))
        self.Bloodgroup.setItemText(4, _translate("MainWindow", "A-"))
        self.Bloodgroup.setItemText(5, _translate("MainWindow", "AB+"))
        self.Bloodgroup.setItemText(6, _translate("MainWindow", "AB-"))
        self.Bloodgroup.setItemText(7, _translate("MainWindow", "o+"))
        self.Bloodgroup.setItemText(8, _translate("MainWindow", "o-"))
        self.Male.setText(_translate("MainWindow", "Male"))
        self.Female.setText(_translate("MainWindow", "Female"))
        self.Others.setText(_translate("MainWindow", "Others"))
        self.label_4.setText(_translate("MainWindow", "First name"))
        self.label_5.setText(_translate("MainWindow", "Middle name"))
        self.label_6.setText(_translate("MainWindow", "Last Name"))
        self.label_7.setText(_translate("MainWindow", "Mobile number 1"))
        self.label_8.setText(_translate("MainWindow", "Mobile number 2"))
        self.label_9.setText(_translate("MainWindow", "Aadhar number"))
        self.label_10.setText(_translate("MainWindow", "PAN number(if any)"))
        self.label_11.setText(_translate("MainWindow", "Date of birth "))
        self.label_12.setText(_translate("MainWindow", "Blood group"))
        self.label_13.setText(_translate("MainWindow", "Address"))
        self.label_14.setText(_translate("MainWindow", "Treating Doctor"))
        self.Add.setText(_translate("MainWindow", "Add"))
        self.Maintabs.setTabText(self.Maintabs.indexOf(self.Add_New_Patient), _translate("MainWindow", "Add New Patient"))

    def default_load(self):
        self.List_of_patients.clear()              #
        self.List_of_patients.setRowCount(0)       #
        self.List_of_patients.setColumnCount(7)    #
        self.List_of_patients.setColumnWidth(0,175)#
        self.List_of_patients.setColumnWidth(1,175)# irrelevant part
        self.List_of_patients.setColumnWidth(2,175)#
        self.List_of_patients.setColumnWidth(3,175)#
        self.List_of_patients.setColumnWidth(4,175)#
        self.List_of_patients.setColumnWidth(5,175)#
        self.List_of_patients.setHorizontalHeaderLabels(['Patient ID / UID', 'First Name', 'Middle Name', 'Last Name','Contact No #','Treating Doctor','Age'])
        for row in connection.load_patient_list():
            self.Addtotable(connection.myconvert(row)) #Calling the Addtotable function and retriving data from myconvert function

    def search_details(self):
        empty_tuple = []
        self.List_of_patients.clear()
        self.List_of_patients.setRowCount(0)
        global Search_filter_by
        search_filter_by = ''
        if self.First_Name_search_filter.isChecked():
            search_filter_by = 'pt_firstname'
        if self.Last_Name_Search_filter.isChecked():
            search_filter_by = 'pt_lastname'
        if self.UID_search_filter.isChecked():
            search_filter_by = 'patient_id'
        result = connection.search_doubleclicked(search_filter_by,self.Search_text.text())

        self.List_of_patients.setHorizontalHeaderLabels(['Patient ID / UID', 'First Name', 'Middle Name', 'Last Name','Contact No #','Treating Doctor'])
        if result == empty_tuple:
            self.Search_result_label.setText("Patient not found, Try entering the full name or UID")
            self.Search_result_label.setStyleSheet("background-color: lightgreen")
        else:
            self.Search_result_label.setText("Search Result:")
            self.Search_result_label.setStyleSheet("background-color: white")
            for row in result:
                self.Addtotable(connection.myconvert(row))
        self.Search_text.clear()

    def Second_screen_launch(self):
        d = self.List_of_patients.item(self.List_of_patients.currentRow(),0).text()
        myresult = connection.search_UID_of_doubleclicked('patient_id',d)
        rez = connection.send_name(myresult)
        self.window = QtWidgets.QMainWindow()
        self.uii = Ui_MainWindoww()
        self.uii.setupUi(self.window,myresult,rez)
        self.window.show()

    def Addtotable(self,coloumn):
        rownum = self.List_of_patients.rowCount()
        self.List_of_patients.insertRow(rownum)
        for i, coloumn in enumerate(coloumn):
            self.List_of_patients.setItem(rownum,i,QtWidgets.QTableWidgetItem(str(coloumn)))

    def close_app(self):
        Ui_MainWindow.close_app(self)


    def mobnumcheck(self, value):
        if len(value) < 10 or len(value) > 10:
            return 0
        else:
            return value
    def digichek(self, value):
        if len(value) < 12 or len(value) > 12:
            return 0
        else:
            return value

    def Addpatient(self):
        pt_sex = "GGG"
        if self.First_Name.text() or self.Middle_Name.text() or self.Last_name.text() or self.Address.text() != "":
            contac1 = self.mobnumcheck(self.Mobile_number1.text())
            contac2 = self.mobnumcheck(self.Mobile_number2.text())
            aadhar = self.digichek(self.Aadhaar_number.text())
            if contac1 == 0:
                self.inputerrormessege.setText("Mobile number is not 10 digit")
                self.inputerrormessege.setStyleSheet("background-color: red")
                font = QtGui.QFont()
                font.setPointSize(16)
                self.inputerrormessege.setFont(font)
            elif aadhar == 0:
                self.inputerrormessege.setText("Aadhar number is not 12 digit")
                self.inputerrormessege.setStyleSheet("background-color: red")
                font = QtGui.QFont()
                font.setPointSize(16)
                self.inputerrormessege.setFont(font)
            else:
                pt_Firstname = self.First_Name.text()
                pt_Middlename = self.Middle_Name.text()
                pt_Lastname = self.Last_name.text()
                pt_DOB = self.Date_of_Birth.date().toPyDate()
                pt_bloodgroup = self.Bloodgroup.currentText()
                pt_Aadharcard_no = aadhar
                pt_PAN_card_no = self.PAN_number.text()
                pt_contact_no = contac1
                pt_contact_no_2 = contac2
                pt_address = self.Address.text()
                pt_Treating_doctor = self.Doctorname.currentText()
                if self.Others.isChecked():
                    pt_sex = "O"
                if self.Male.isChecked():
                    pt_sex = "M"
                if self.Female.isChecked():
                    pt_sex = "F"
                Age = date.year-self.Date_of_Birth.date().toPyDate().year
                if pt_sex != "GGG":
                    val = (pt_Firstname, pt_Middlename, pt_Lastname, pt_DOB, Age, pt_sex, pt_bloodgroup, pt_contact_no, pt_contact_no_2,pt_Aadharcard_no, pt_PAN_card_no, pt_address, pt_Treating_doctor)
                    self.First_Name.clear()
                    self.Middle_Name.clear()
                    self.Last_name.clear()
                    self.Aadhaar_number.clear()
                    self.PAN_number.clear()
                    self.Mobile_number1.clear()
                    self.Mobile_number2.clear()
                    self.Address.clear()
                    self.Doctorname.clear()
                    connection.add_new_patient_to_table(val)   ## calling the create new patient function
                    self.inputerrormessege.setText("patient added")
                    self.inputerrormessege.setStyleSheet("background-color: turquoise")
                    font = QtGui.QFont()
                    font.setPointSize(16)
                    self.inputerrormessege.setFont(font)
                    self.default_load()
                else:
                    self.inputerrormessege.setText("All Fields are mandatory")
                    self.inputerrormessege.setStyleSheet("background-color: red")
                    font = QtGui.QFont()
                    font.setPointSize(16)
                    self.inputerrormessege.setFont(font)
        else:
            self.inputerrormessege.setText("All Fields are mandatory")
            self.inputerrormessege.setStyleSheet("background-color: red")
            font = QtGui.QFont()
            font.setPointSize(16)
            self.inputerrormessege.setFont(font)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()   #creating an object
    ui.setupUi(MainWindow) #passing the MainWindow widget
    MainWindow.show()
    sys.exit(app.exec_())
