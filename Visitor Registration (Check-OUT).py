import check
from share import SharedClass as s
from tkinter import messagebox
from tkinter import *
from time import strftime
import datetime
from datetime import *
import mysql.connector

#Declaring a function for clearing the fields
def clearout():
    ent_fn.delete(0, END)
    ent_ln.delete(0, END)
    ent_wn.delete(0, END)
    ent_fl.delete(0, END) 
    ent_vc.delete(0, END)




#Declaring Function for SQL Connection
def mysql_connection():
    if check.check_data_out():
        db = mysql.connector.connect(host = "localhost", port = 3306, user ="root", passwd = "ark18", db = "society_visitors")
        cq = db.cursor()

        e1 = s.f_name.get()
        e2 = s.l_name.get()
        e5 = s.wing.get()
        e6 = s.flat.get()
        e7 = s.vc_code.get()
        e11 = date.get()
        e12 = cout_time.get()

        try:
            Q = "UPDATE visitors SET cout_date = %s WHERE first_name = %s and last_name = %s and wing = %s and flat = %s and sr_no = %s"
            Q1 = "UPDATE visitors SET cout_time = %s WHERE first_name = %s and last_name = %s and wing = %s and flat = %s and sr_no = %s"
            val = (e11, e1, e2, e5, e6, e7)
            val1 = (e12, e1, e2, e5, e6, e7)
            cq.execute(Q, val)
            cq.execute(Q1, val1)
            db.commit()
            db.close()
        except:
            messagebox.showerror(title = "ERROR",message = "Please check whether you have entered the proper data")
        else:
            clearout()

root = Tk()
root.title("Society Visitor Check-OUT")

#Declaring datetime variables
d_1 = datetime.now()
d = d_1.strftime("%d/%m/%Y")
date = StringVar(root, value = d)
labelt=Label(root)
def time(): 
    Time = strftime('%H:%M:%S') 
    labelt.config(text = Time) 
    labelt.after(1000, time)
    return Time
time()
cout_time= StringVar(root, value= time())



#Declaring Variables for program
s.f_name = StringVar()
s.l_name = StringVar()
s.wing = StringVar()
s.flat = IntVar()
s.vc_code = StringVar()

#Basic entry details to access database
lab_fn = Label(root, text = "First Name")
lab_ln = Label(root, text = "Last Name")
ent_fn = Entry(root, textvariable = s.f_name)
ent_ln = Entry(root, textvariable = s.l_name)
lab_fn.grid(row = 2, column = 2)
ent_fn.grid(row = 3, column = 2)
lab_ln.grid(row = 2, column = 4)
ent_ln.grid(row = 3, column = 4)


lab_wn = Label(root, text = "Wing")
ent_wn = Entry(root, textvariable = s.wing)
lab_fl = Label(root, text = "Flat No.")
ent_fl = Entry(root, textvariable = s.flat)
lab_wn.grid(row = 4, column = 2)
ent_wn.grid(row = 5, column = 2)
lab_fl.grid(row = 4, column = 4)
ent_fl.grid(row = 5, column = 4)

#Using Datetime for Checkout
lab_d = Label(root, text = "Check-OUT Date")
lab_d1 = Label(root, textvariable = date)
lab_d.grid(row = 6, column = 2)
lab_d1.grid(row = 7, column = 2)
lab_t = Label(root, text = "Check-OUT Time")
lab_t.grid(row = 6, column = 4)
labelt.grid(row = 7, column = 4)

#Visiting Code
lab_vc = Label(root, text = "Visiting Code")
ent_vc = Entry(root, textvariable = s.vc_code)
lab_vc.grid(row = 10, column = 3)
ent_vc.grid(row = 11, column = 3)


#Button
but = Button(root, text = "Check-OUT", command = mysql_connection)
but.grid(row = 13, column = 3)




root.mainloop()