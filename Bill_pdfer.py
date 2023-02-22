from fpdf import FPDF
import connection
import datetime
import os
date = datetime.date.today()
pdf = FPDF()
pdf.add_page()
small_sz = 15
head_sz = 24
fnt = "Arial"
Clinic_address_ = "1st Floor, Ajit Darshan Building, Near 3 Petrol Pump"  #Hiding the address in the image.
Clinic_address__ = "Lal Bahadur Shastri Rd, Naupada"
Clinic_address___ =  "Thane West, Thane, Maharashtra 400602"

def print_bill(identity_data,procedure_data,bill_data):
    pdf.set_font(fnt, size=head_sz)

    pdf.cell(180, 20, txt="EMRsys",
             ln = 5, align='R') 
    pdf.set_font(fnt, size=small_sz)
    pdf.cell(180, 5, txt=Clinic_address_,
             ln = 5, align='R')
    pdf.cell(180, 5, txt=Clinic_address__,
              ln = 5, align='R')
    pdf.cell(180, 5, txt=Clinic_address___,
             ln = 5, align='R')
    pdf.cell(200, 10,
             txt="-----------------------------------------------------------------------------------------------",
             ln=1, align='C')
    pdf.cell(180, 20, txt= "Invoice_NO: " + str(bill_data[0][0]),ln = 5, align='L')
    pdf.cell(180, 10, txt="Invoice Date: " + str(date),ln = 5, align='L')
    pdf.cell(180, 10, txt="Patient Name: " + str(identity_data[0][0])+str(identity_data[0][1]),ln = 5, align='L')
    pdf.cell(180, 10, txt="Patient ID: " + str(bill_data[0][1]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Mobile: " + str(identity_data[0][2]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Treating Doctor: " + str(identity_data[0][4]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Address: " + str(identity_data[0][3]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Complaints: " + str(procedure_data[0][4]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Treatment Advised: " + str(procedure_data[0][6]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Procedure 1: " + str(procedure_data[0][1]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Procedure 2: " + str(procedure_data[0][2]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Procedure 3: " + str(procedure_data[0][3]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Total amount: " + str(bill_data[0][4]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Amount Paid: " + str(bill_data[0][5]), ln = 5, align='L')
    pdf.cell(180, 10, txt="Remark on paid amount: " + str(bill_data[0][6]), ln = 5, align='L')
    pdf.output(name=str(identity_data[0][0])+str(identity_data[0][1])+ ".pdf",dest='F')
    os.startfile("C:\\Users\\Atharva\\Desktop\\Atharv Bhalerao CS final IA\\Product\\"+str(identity_data[0][0])+" "+str(identity_data[0][1])+ ".pdf")