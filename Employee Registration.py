import tkinter
from tkinter import *
from tkinter import messagebox
import tkcalendar
from tkcalendar import DateEntry
import share
from share import SharedClass as s
import datetime
from datetime import *
import check
import mysql.connector

root = Tk()
root.title("Registration")

#Clearing values
def cleardata():
    ent_fname.delete(0, END)
    ent_lname.delete(0, END)
    ent_add.delete(0, END)
    ent_mob.delete(0, END)
    ent_pass.delete(0, END)
    ent_rpass.delete(0, END)



#SQL Connection
def mysql_connection():
    if check.check_registration():
        db = mysql.connector.connect(host = "localhost", port = 3306, user ="root", passwd = "ark18", db = "society_visitors")
        cq = db.cursor()

        e1 = s.e_f_name.get()
        e2 = s.e_l_name.get()
        e3 = s.e_add.get()
        e4 = int(s.e_mob.get())
        e5 = s.passwd.get()
        e6 = s.e_birthdate.get()
        e7 = s.e_joindate.get()
        e8 = s.des.get()

        try:
            Q = "INSERT INTO employee (e_firstname, e_lastname, e_address, e_mobile, passwd, e_birthday, e_joindate, e_designation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (e1, e2, e3, e4, e5, e6, e7, e8)
            cq.execute(Q, val)
            db.commit()
        #except:
        except ImportError as e:
            print(e)
            #messagebox.showerror(title = "ERROR",message = "Please check whether you have entered the proper data")
        else:
            Q = "SELECT employee_code FROM employee ORDER BY employee_code DESC LIMIT 1"
            cq.execute(Q)
            records=cq.fetchall()
            for record in records:
                employee_code = record[0]
            thanks_msg = "Welcome, aboard!! \nYour employee code is " + str(employee_code)
            db.close()
            messagebox.showinfo(title = "Welcome!!", message = thanks_msg)
            cleardata()



#Variable Declaration
s.e_f_name = StringVar()
s.e_l_name = StringVar()
s.e_birthdate = StringVar()
s.e_add = StringVar()
s.e_mob = StringVar()
s.passwd = StringVar()
s.rpasswd = StringVar()
s.des = StringVar()


#Title
Label(root, text = "Employee Registration").grid(row = 1, column = 3)


#Data Entry
lab_fname = Label(root, text = "First Name")
lab_fname.grid(row = 2, column = 2)
ent_fname = Entry(root, textvariable = s.e_f_name)
ent_fname.grid(row = 3, column = 2)
lab_lname = Label(root, text = "Last Name")
lab_lname.grid(row = 2, column = 4)
ent_lname = Entry(root, textvariable = s.e_l_name)
ent_lname.grid(row = 3, column = 4)

lab_add = Label(root, text = "Address")
lab_add.grid(row = 4, column = 2)
ent_add = Entry(root, textvariable = s.e_add)
ent_add.grid(row = 5, column = 2)

lab_mob = Label(root, text = "Mobile")
lab_mob.grid(row = 4, column = 4)
ent_mob = Entry(root, textvariable = s.e_mob)
ent_mob.grid(row = 5, column = 4)

#Password
lab_pass = Label(root, text = "Enter Password")
lab_pass.grid(row = 6, column = 2)
ent_pass = Entry(root, textvariable = s.passwd, show = '•')
ent_pass.grid(row = 7, column = 2)

lab_rpass = Label(root, text = "Re-enter Password")
lab_rpass.grid(row = 6, column = 4)
ent_rpass = Entry(root, textvariable = s.rpasswd, show = '•')
ent_rpass.grid(row = 7, column = 4)

#Birthdate
Label(root, text = "Birthdate").grid(row = 8, column = 3)
ent_bdate = DateEntry(root, textvariable = s.e_birthdate, background = 'dark blue', foreground = 'white', date_pattern = "dd/mm/yyyy").grid(row = 9, column = 3)


#Designation
lab_des = Label(root, text = "Designation")
lab_des.grid(row = 10, column = 3)
drp_des = OptionMenu(root, s.des, "Watchman", "Security Supervisor", "Cleaning Service", "Cleaning Supervisor", "Maintainence Staff","Property Manager")
s.des.set("--Select a designation--")
drp_des.grid(row = 11, column = 3)

#Join Date
d_1 = datetime.now()
d = d_1.strftime("%d/%m/%Y")
s.e_joindate = StringVar(root, value = d)

#Button
Button(root, text = "Register", command = mysql_connection).grid(row = 15, column = 3)



root.mainloop()



#Employee Salary to be added
# RIP