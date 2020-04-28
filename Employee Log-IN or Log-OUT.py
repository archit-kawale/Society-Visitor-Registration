from share import SharedClass as s
import check
import mysql.connector
from tkinter import messagebox 
from tkinter import *
import datetime
from datetime import *
from time import strftime

root = Tk()
root.title("Log-IN or Log-OUT")


#A function for Clearing Data
def clear_data():
    s.ent_ecode.delete(0, END)
    s.ent_pass.delete(0, END)
    rad_cin.deselect()
    rad_cout.deselect()
    s.r.set(18)

#SQL Connection
def employee_data_entry():
    if check.check_credentials():
        e1 = int(s.emp_code.get())
        e2 = cin_date.get()
        e3 = time()



        db = mysql.connector.connect(host = "localhost", port = 3306, user ="root", passwd = "ark18", db = "society_visitors")
        cq = db.cursor()
        
        a=False

        if s.r.get() == 1:
            try:
                Q = "INSERT INTO employee_attendence_records(employee_code, e_cin_date, e_cin_time) VALUES(%s,%s,%s)"
                val = (e1, e2, e3)
                cq.execute(Q, val)
                db.commit()  
            except ImportError as e:
                messagebox.showerror(title = "ERROR", message = "Please check whether you have entered the proper data ")
                print(e)
            else:
                db.close()
                messagebox.showinfo(title = "THANK YOU", message = "Have a great day!")
                clear_data()
    
        elif s.r.get() == 2:
            try:
                Q = "SELECT sr_no FROM employee_attendence_records WHERE employee_code = %s ORDER BY sr_no DESC LIMIT 1"
                val = (e1, )
                cq.execute(Q, val)
                records = cq.fetchall()
                for record in records:
                    sr_no = record[0]
        
                Q = "UPDATE employee_attendence_records SET e_cout_date = %s WHERE sr_no = %s "
                Q1 = "UPDATE employee_attendence_records SET e_cout_time = %s WHERE sr_no = %s "
                val = (e2, sr_no)
                val1 = (e3, sr_no)
                cq.execute(Q, val)
                cq.execute(Q1, val1)
                db.commit()
            except ImportError as e:
                messagebox.showerror(title = "ERROR",message = "Please check whether you have entered the proper data ")
                print(e)
            else:
                db.close()
                messagebox.showinfo(title = "THANK YOU",message = "Have a great day!")
                clear_data()
        
        else: 
            messagebox.showerror(title = "ERROR", message = "Please select an option!")

    



#Date & Time 
d_1 = datetime.now()
d = d_1.strftime("%d/%m/%Y")
cin_date = StringVar(root, value = d)

label_t1 = Label(root)
def time(): 
    Time = strftime('%H:%M:%S') 
    label_t1.config(text = Time) 
    label_t1.after(1000, time)
    return Time
time()
cin_time = StringVar(root, value= time())

#Declaring Variables
s.emp_code = StringVar()
s.emp_pass = StringVar()
s.r = IntVar()


#Data Entry
lab_ecode = Label(root, text = "Employee Code")
lab_ecode.grid(row = 2, column = 2, padx = 3)
s.ent_ecode = Entry(root, textvariable = s.emp_code)
s.ent_ecode.grid(row = 3, column = 2, padx = 3)

lab_pass = Label(root, text = "Password")
lab_pass.grid(row = 2, column = 4, padx = 3)
s.ent_pass = Entry(root, textvariable = s.emp_pass, show = '•')
s.ent_pass.grid(row = 3, column = 4, padx = 3)

#Date & Time Labels
lab_dt = Label(root, text = "Date")
lab_dt1 = Label(root, textvariable = cin_date)
lab_dt.grid(row = 4, column = 2)
lab_dt1.grid(row = 5, column = 2)

lab_t= Label(root, text= "Time")
lab_t.grid(row = 4, column = 4)
label_t1.grid(row = 5, column = 4)

#Radio Button
rad_cin = Radiobutton(root, text = "Check-IN", variable = s.r, value = 1, tristatevalue = 0, command = s.r.set(1))
rad_cin.grid(row = 7, column = 2)
rad_cin.deselect()
rad_cout = Radiobutton(root, text = "Check-OUT", variable = s.r, value = 2, tristatevalue = 0, command = s.r.set(2))
rad_cout.grid(row = 7, column = 4)
rad_cout.deselect()
#rad_inv = Radiobutton(root, text = "Invalid", variable = s.r, value = 3, tristatevalue = 0, command = s.r.set(3))

#Button
Button(root, text = "Go!!", command = lambda: employee_data_entry()).grid(row = 8, column = 3)





root.mainloop()