#The Code hang-outs here

from share import SharedClass as s
from tkinter import messagebox
from tkinter import *
import mysql.connector






#A function to check whether the entered data is correct
def check_data_in():
    e1 = s.f_name.get()
    e2 = s.l_name.get()
    e5 = s.wing.get()
    e7 = s.pur.get()

    if e1=='' or e2=='':
        messagebox.showerror(title="ERROR",message="First and Last names cannot be empty. ")
        return
    elif e1.isalpha() and e2.isalpha():
        a=True
        pass
    else:
        messagebox.showerror(title="ERROR",message="First and Last names cannot contain any numerical values or any special characters")  

    try:
        e3 = int(s.mob.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Mobile Number")
        a=False
        return
    else:
        a=True

    if e5=='':
        messagebox.showerror(title="ERROR",message="Please enter a valid Wing ")
        a=False
        return
    else:
        a=True

    try:
        e6 = int(s.flat.get())
        if (len(str(e3)) != 10):
            messagebox.showerror(title = "INPUT ERROR", message = "Mobile number must contain 10 digits")
            a = False
            return

    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Flat Number ")
        a=False
        return
    else:
        a=True
    

    if e7=='':
        messagebox.showerror(title="ERROR",message="Purpose cannot be empty")
        return

    try:
        e13 = int(s.wt_code.get())
    except:
        messagebox.showerror(title="ERROR",message="Please enter a valid Watchman Code")
        a = False
        return
    else:
        a = True

    return a





#A function to check weather the entered data is correct for SVR(Check-IN)
def check_data_out():
    e1 = s.f_name.get()
    e2 = s.l_name.get()
    e5 = s.wing.get()
    db = mysql.connector.connect(host = "localhost", port = 3306, user ="root", passwd = "ark18", db = "society_visitors")
    try:
        a = False
        e0 = int(s.vc_code.get())
        cq = db.cursor()
        cq.execute("SELECT sr_no FROM visitors")
        records=cq.fetchall()
        for record in records:
            for i in record:
                if i==e0:
                    a = True
                    break
        if a is False:
            messagebox.showerror(title = "ERROR", message = "The entered visitor code was not found in the database. ")
            db.close()
            return

    except:
        messagebox.showerror(title = "ERROR", message = "Please enter a valid visitor code. ")
        db.close()
        a = False
        return
    else:
        a = True


    if e1 == '' or e2 == '':
        messagebox.showerror(title="ERROR", message="First and Last names cannot be empty. ")
        return
    elif e1.isalpha() and e2.isalpha():
        a = True
        pass
    else:
        messagebox.showerror(title = "ERROR", message = "First and Last names cannot contain any numerical values. ")

    if e5 == '':
        messagebox.showerror(title = "ERROR", message = "Please enter a valid Wing ")
        a = False
        return
    else:
        a = True

    try:
        e6 = int(s.flat.get())
    except:
        messagebox.showerror(title = "ERROR", message = "Please enter a valid Flat Number ")
        a = False
        return
    else:
        a = True


    return a





#A function to check weather the entered data is correct for Employee Registration
def check_registration():
    e1 = s.e_f_name.get()
    e2 = s.e_l_name.get()



    #Checking for errors in name
    if e1=='' or e2=='':
        messagebox.showerror(title="ERROR",message="First and Last names cannot be empty. ")
        return
    elif e1.isalpha() and e2.isalpha():
        a=True
        pass
    else:
        messagebox.showerror(title="ERROR",message="First and Last names cannot contain any numerical values or any special characters")

    #Checking for errors in Mobile Number
    try:
        e4 = int(s.e_mob.get())
        if (len(str(e4)) != 10):
            messagebox.showerror(title = "ERROR", message = "Mobile number must contain 10 digits...")
            a = False
            return
    except:
        messagebox.showerror(title = "ERROR", message = "Please enter a valid mobile number")
        a = False
        return
    else:
        a = True

    #Checking if passwords match
    if (s.passwd.get() == s.rpasswd.get()):
        a = True
    else:
        messagebox.showerror(title = "ERROR", message = "Password does not match")
        a = False
        return
    

    return a







def check_credentials():
    db = mysql.connector.connect(host = "localhost", port = 3306, user ="root", passwd = "ark18", db = "society_visitors")
    
    a = False
    
    usr = (s.emp_code.get(), )
    passwd = s.emp_pass.get()
    cq = db.cursor()
    
    # This block of code checks whether the actual employee code/ password is correct     
    Q = "SELECT passwd FROM employee WHERE employee_code = %s "
    cq.execute(Q, usr)
    records = cq.fetchall()
    for record in records:
        for i in record:
            if i == passwd:
                a = True

    if a is False:
        messagebox.showerror(title = "ERROR", message = "The employee code or password entered is incorrect ")
        s.ent_ecode.delete(0, END)
        s.ent_pass.delete(0, END)
        db.close()
        return a

    #This block of code stops the user from checking-in/out twice in a row(It doesnt really work)
    Q = "SELECT sr_no FROM employee_attendence_records WHERE employee_code = %s ORDER BY sr_no DESC LIMIT 1"
    cq.execute(Q, usr)
    records = cq.fetchall()
    for record in records:
        sr_no = record[0]    
    
    if records == [] and s.r.get() == 2:
        messagebox.showerror(title = "ERROR", message = "You cannot check out without checking in !! ")
        a = False
    elif records == [] and s.r.get() == 1:
        a = True
    else:
        Q = "SELECT e_cin_date FROM employee_attendence_records WHERE sr_no = %s "
        val = (sr_no, )
        cq.execute(Q, val)
        datein = cq.fetchall()
        
        Q = "SELECT e_cout_date FROM employee_attendence_records WHERE sr_no = %s "
        val = (sr_no, )
        cq.execute(Q, val)
        dateout = cq.fetchall()
        
        # If the check-in date is NULL, that means the user has not checked in before
        if datein[0][0] != 'NULL' and s.r.get() == 1 and dateout[0][0] == 'NULL' : 
            messagebox.showerror(title = "ERROR", message = "You cannot check in twice in a row!! ")
            a = False
            return a


        # If the check-out date is NULL, that means the user has not checked in before
        if dateout[0][0] == 'NULL' and datein[0][0] != 'NULL' or s.r.get() == 1 : 
            a = True
        else:
            messagebox.showerror(title = "ERROR", message = "You cannot check out without checking IN !! ")
            a = False
        
    return a