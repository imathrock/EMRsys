import mysql.connector
import ast
mydb = mysql.connector.connect(
  host='www.ecxsg.com',
  user='ecxsgs9y_atharv',
  password='Athack@301104',
  database='ecxsgs9y_atharv'
)

showdata_in_initial_screen =  """SELECT patient_id,pt_firstname,pt_middlename,pt_lastname,pt_Mobilenumber1,pt_Treating_doctor,Age FROM patient_identity_details """
add_new_patient =  "INSERT INTO patient_identity_details (pt_Firstname,pt_Middlename,pt_Lastname,pt_DOB,Age,pt_sex,pt_blood_grp,pt_Mobilenumber1,pt_Mobilenumber2," \
                   "pt_Aadharcard_no,pt_PAN_Card_no,pt_Address,pt_Treating_doctor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
select_patient = """SELECT patient_id,pt_firstname,pt_middlename,pt_lastname,pt_Mobilenumber1,pt_Treating_doctor FROM patient_identity_details WHERE """
select_end_stmt = """ = %s"""
select_patient_uid = """SELECT patient_id FROM patient_identity_details WHERE """
history_load_sql_stmt = """ SELECT Tx_ID,pt_temperature,pt_pulse_rate,pt_bp_Systolic,pt_bp_Diastolic,pt_oxygen_level,pt_RBS,pt_weight,
pt_procedure_1,pt_procedure_2,pt_procedure_3,pt_Patient_complaints,pt_clinical_notes,pt_treatment_advised,Update_Date FROM patient_history WHERE pt_UID = %s """
Insert_into_history_sql_stmt = """ INSERT INTO patient_history (Visit_type,pt_temperature,pt_pulse_rate,pt_bp_Systolic,pt_bp_Diastolic,
pt_oxygen_level,pt_RBS,pt_weight,pt_procedure_1,pt_procedure_2,pt_procedure_3,pt_Patient_complaints,pt_clinical_notes,pt_treatment_advised,pt_UID )
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
Get_patient_Name_from_UID = "SELECT pt_firstname,pt_lastname FROM patient_identity_details WHERE patient_id = %s"
delete_record = "DELETE FROM patient_history WHERE Tx_ID = %s"
Insery_into_bill_table = "INSERT INTO Billing (pt_UID,Tx_ID,Bill_Amount,Amount_Paid,Status) VALUES (%s,%s,%s,%s,%s)"
Show_entire_bill_table = "SELECT * FROM Billing"
Show_all_patient_details = "SELECT * FROM patient_identity_details WHERE patient_id = %s"
bill_data_call1 = "SELECT pt_firstname,pt_lastname,pt_Mobilenumber1,pt_Address,pt_Treating_doctor FROM patient_identity_details WHERE patient_id = %s"
bill_data_call2 = "SELECT Tx_ID,pt_procedure_1,pt_procedure_2,pt_procedure_3,pt_Patient_complaints,pt_clinical_notes,pt_treatment_advised " \
                  "FROM patient_history WHERE (pt_UID = %s AND Tx_ID = %s)"
bill_data_call3 = "SELECT * FROM Billing WHERE (pt_UID = %s AND Tx_ID = %s)"
extract_visit_typee = "SELECT Visit_type FROM patient_history WHERE (pt_UID = %s AND Tx_ID = %s)"
extract_procedure_dataa = "SELECT pt_procedure_1,pt_procedure_2,pt_procedure_3 FROM patient_history WHERE (pt_UID = %s AND Tx_ID = %s)"
get_procedure_charge = "SELECT Charge FROM Procedure_Charge WHERE Procedure_Name = (%s)"
load_bill_historyy = "SELECT * FROM Billing WHERE pt_UID = %s"
checkrepeatbill = "SELECT * FROM Billing WHERE Tx_ID = %s"
def myconvert(data):
    def cvt(temp):
        try:
            return ast.literal_eval(temp)
        except Exception:
            return str(temp)
    return tuple(map(cvt,data)) #returning data in a tuple format

def load_patient_list():
    mycursor = mydb.cursor()
    mycursor.execute(showdata_in_initial_screen)
    result = mycursor.fetchall()
    mycursor.close()
    return result

def search_doubleclicked(fltr,val):
    mycursor = mydb.cursor()
    sql = select_patient + fltr + select_end_stmt
    mycursor.execute(sql,(val,))
    result = mycursor.fetchall()
    mycursor.close()
    return result

def add_new_patient_to_table(val):
    mycursor = mydb.cursor()
    sql = add_new_patient
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()

def search_UID_of_doubleclicked(fltr,val):
    mycursor = mydb.cursor()
    sql = select_patient_uid + fltr + select_end_stmt
    mycursor.execute(sql,(val,))
    result = mycursor.fetchall()
    mycursor.close()
    return result

def load_patient_history(pt_UID):
    mycursor = mydb.cursor()
    mycursor.execute(history_load_sql_stmt, (pt_UID))
    result = mycursor.fetchall()
    mycursor.close()
    return result

def load_bill_history(pt_UID):
    mycursor = mydb.cursor()
    mycursor.execute(load_bill_historyy, (pt_UID))
    result = mycursor.fetchall()
    mycursor.close()
    return result

def load_into_patient_history(val):
    mycursor = mydb.cursor()
    mycursor.execute(Insert_into_history_sql_stmt,val)
    mydb.commit()
    mycursor.close()

def send_name(pt_UID):
    mycursor = mydb.cursor()
    mycursor.execute(Get_patient_Name_from_UID,(pt_UID[0]))
    result = mycursor.fetchall()
    mycursor.close()
    return result

def delete_entry(Tx_ID):
    mycursor = mydb.cursor()
    mycursor.execute(delete_record,(Tx_ID,))
    mydb.commit()
    mycursor.close()

def Insert_bill(val):
    mycursor = mydb.cursor()
    mycursor.execute(Insery_into_bill_table,val)
    mydb.commit()
    mycursor.close()

def shobilltable():
    mycursor = mydb.cursor()
    mycursor.execute(Show_entire_bill_table)
    result = mycursor.fetchall()
    mycursor.close()
    return result

def bill_print_data(pt_UID):
    mycursor = mydb.cursor()
    mycursor.execute(bill_data_call1,(pt_UID,))
    result = mycursor.fetchall()
    print(result)
    mycursor.close()
    return result

def bill_print_data1(val):
    mycursor = mydb.cursor()
    mycursor.execute(bill_data_call2, (val))
    result = mycursor.fetchall()
    print(result)
    mycursor.close()
    return result

def bill_print_data2(val):
    mycursor = mydb.cursor()
    mycursor.execute(bill_data_call3, (val))
    result = mycursor.fetchall()
    print(result)
    mycursor.close()
    return result

def show_patient_details(pt_UID):
    mycursor = mydb.cursor()
    mycursor.execute(Show_all_patient_details,pt_UID)
    result = mycursor.fetchall()
    return result

def extract_visit_type(val):
    mycursor = mydb.cursor()
    mycursor.execute(extract_visit_typee,(val))
    result = mycursor.fetchall()
    return result

def extract_procedure_data(val):
    mycursor = mydb.cursor()
    mycursor.execute(extract_procedure_dataa,(val))
    result = mycursor.fetchall()
    return result

def get_charge(procedure):
    mycursor = mydb.cursor()
    mycursor.execute(get_procedure_charge,(procedure,))
    result = mycursor.fetchall()
    return result

def check_repeat_transaction(Tx_ID):
    mycursor = mydb.cursor()
    mycursor.execute(checkrepeatbill, (Tx_ID,))
    rezult = mycursor.fetchall()
    if rezult != []:
        return True
    else:
        return False