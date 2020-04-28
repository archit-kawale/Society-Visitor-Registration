from tkinter import *
from tkinter import ttk as t
from share import SharedClass as s
from tkinter import messagebox
import mysql.connector



class watchman:
    def __init__(self, watch_code): 
    #Here, the argument root refers to the root of the data_access module, haven't yet decided whether it is useful or not    
        self.master = Tk()

        self.master.title('Watchman Console')

        self.display = t.Treeview(self.master)

        watch_search = ('first_name', 'mobile')
    
        self.button = Button(self.master, text = 'Search' , command = lambda: self.search(watch_search))
        self.button.grid(row = 5, column = 3)
        
        w = 'Employee Code \n' + str(*watch_code)
        self.desig = Label(self.master, text = 'Designation \nWatchman')
        self.lab = Label(self.master, text = w)
        
        self.desig.grid(row = 0, column = 2)
        self.lab.grid(row = 0, column = 4)


        try:
            self.db = mysql.connector.connect(host = "localhost", port = 3306, user ="root", passwd = "ark18", db = "society_visitors")
            self.cq = self.db.cursor()
            self.cq.execute('SELECT sr_no, first_name, last_name, flat, wing FROM visitors')
            data = self.selection(self.cq.fetchall())
        except ImportError as e:
            print(e)


        s.droot.destroy()

        self.master.mainloop()

    
    def selection(self, data):

        self.display['columns'] = ('fname', 'lname','flat', 'wing')
        self.display.heading('#0', text='Visitor Code', anchor='center')
        self.display.column('#0', anchor='center', width = 100)
        self.display.heading('fname', text='First Name')
        self.display.column('fname', anchor='center', width=100)
        self.display.heading('lname', text='Last Name')
        self.display.column('lname', anchor='center', width=100)
        self.display.heading('flat', text='Flat')
        self.display.column('flat', anchor='center', width=100)
        self.display.heading('wing', text='Wing')
        self.display.column('wing', anchor='center', width=100)
        self.display.grid(row = 2, column = 2, columnspan = 3)


        for row in data:
            self.display.insert('', 'end', text = str(row[0]), values = (row[1], row[2], row[3], row[4]))


    def search(self, column):
        self.searchmaster = Tk()
        self.searchmaster.title("Watchman's Search")

        self.s = StringVar(self.searchmaster)
        self.ser = StringVar(self.searchmaster)

        search_lab = Label(self.searchmaster, text = "Enter the data you want to : ")
        search_lab.grid(row = 0, column = 3)

        ent_find = Entry(self.searchmaster, textvariable = self.s)
        ent_find.grid(row = 1, column = 3)

        
        search_opt = OptionMenu(self.searchmaster, self.ser, *column)
        self.ser.set('--Select a field to search from--')
        search_opt.grid(row = 2, column = 3, pady = 10)


        searchb = Button(self.searchmaster, text = 'Search', command = lambda: self.get_data(self.ser.get(), self.s.get()))
        searchb.grid(row = 3, column = 3)


    def get_data(self, column, data):
        try:
            Q = "SELECT sr_no, first_name, last_name, flat, wing FROM visitors WHERE " + str(column) + " = (%s)"
            val = (data, )
            self.cq.execute(Q, val)
        except ImportError as e:
            print(e)
        else:
            self.display.delete(*self.display.get_children())
            
        self.selection(self.cq.fetchall())

    
    


class sec_supervisor:
    def __init__(self, cursor, sup_code):
        
        self.data = cursor
        self.master = Tk()

        self.master.title('Security Supervisor Console')

        self.display = t.Treeview(self.master)

        self.selectvar = IntVar()

        w = 'Employee Code \n' + str(*sup_code)
        self.desig = Label(self.master, text = 'Designation \nSecurity Supervisor')
        self.lab = Label(self.master, text = w)
        
        self.desig.grid(row = 0, column = 2)
        self.lab.grid(row = 0, column = 4)

        self.rad = Radiobutton(self.master, text = 'Attendance Data', variable = self.selectvar, value = 1 ,tristatevalue = 0, command = lambda: self.selectvar.set(1) )
        self.rad.grid(row = 5, column = 2, pady = 10)
        self.rad.deselect()

        self.rad1 = Radiobutton(self.master, text = 'Employee Data', variable = self.selectvar, value = 2, tristatevalue = 0, command = lambda: self.selectvar.set(2) )
        self.rad1.grid(row = 5, column = 4, pady = 10)
        self.rad1.deselect()

        self.sel = Button(self.master, text = "Select", command = lambda: self.select())
        self.sel.grid(row = 6, column = 3)

        s.droot.destroy()

        self.master.mainloop()


    def emp_att_access(self):
        try:
            self.db = mysql.connector.connect(host = "localhost", port = 3306, user ="root", passwd = "ark18", db = "society_visitors")
            self.cq = self.db.cursor()

            self.cq.execute('DESC employee_attendence_records')
            self.columns = self.cq.fetchall()
        except:
            messagebox.showerror(title = "ERROR", message = "Database Connectivity Error")
        else:
            self.display.delete(*self.display.get_children())

        self.var = []
        
        for i in self.columns:
            if i[0] == 'sr_no':
                continue
            self.var.append(i[0])

        root = Tk()

        self.display_data(root, self.var, self.get_data(0, self.var, 0, 1, 'employee_attendence_records'), 'employee_attendence_records')


        
        


    def emp_data_access(self):
        self.emp = Tk()
        self.emp.title('Select Data')

        try:
            self.db = mysql.connector.connect(host = "localhost", port = 3306, user ="root", passwd = "ark18", db = "society_visitors")
            self.cq = self.db.cursor()

            self.cq.execute('DESC employee')
            self.columns = self.cq.fetchall()
        except:
            messagebox.showerror(title = "ERROR", message = "Database Connectivity Error")
        else:
            self.display.delete(*self.display.get_children())

        
        
        self.cb, self.var = [],[]

        for i in range(len(self.columns)-1):
            a = StringVar(self.emp)
            self.var.append(a)

        i = 0

        for column in self.columns:
            if column[0] == 'employee_code':
                continue
            self.cb.append(Checkbutton(self.emp, text = column[0], onvalue = column[0], variable = self.var[i], offvalue = 'None',anchor = E))
            self.cb[i].grid(row = i, column = 3)
            self.cb[i].deselect()
            i+=1
        
        c_select = IntVar()
        
        sel_all = Radiobutton(self.emp, text = "Select All", variable = c_select, value = 1, tristatevalue = 0, command = lambda: self.check_select(self.cb, 1))
        sel_all.grid(row = 10, column = 2)
        dsel_all = Radiobutton(self.emp, text = "Deselect All", variable = c_select, value = 2, tristatevalue = 0, command = lambda: self.check_select(self.cb, 2))
        dsel_all.grid(row = 10, column = 4)
        sel_all.deselect()
        dsel_all.deselect()

        
        select = Button(self.emp, command = lambda: self.display_data(self.emp ,self.get_column(self.var), 0, 'employee') , text = 'Select')
        select.grid(row = 12, column = 2, padx = 10, pady = 10)

        back_button = Button(self.emp, text = 'Back', command = lambda: self.emp.destroy())
        back_button.grid(row = 12, column = 4, padx = 10, pady = 10)

    def check_select(self, button, opt):
        if opt == 1:
            for i in button:
                i.select()
        elif opt == 2:
            for i in button:
                i.deselect()



    def display_data(self, root, columns, sdata, table): #Add a few buttons for after the data has been displayed

        root.destroy()
        if sdata == 0:
            data = self.get_data(0, columns, 0, 1, 'employee')
        else:
            data = sdata
        
        self.display['columns'] = columns
        self.display.heading('#0', text='Sr. No', anchor='center')
        self.display.column('#0', anchor='center', width = 100)
        
        for col in columns:
            self.display.heading(col, text = col, anchor = 'center')
            self.display.column(col, anchor ='center', width = 100)
        
        sr = 1
        for row in data:
            x = []
            for i in range(len(columns)):
                x.append(row[i])
            self.display.insert('', 'end', text = str(sr), values = tuple(x) )
            sr += 1


        self.display.grid(row = 1, column = 3, pady = 5)

        modify = Button(self.master, text = "Modify", command = lambda: self.select())
        modify.grid(row = 3, column = 2)

        search = Button(self.master, text = "Search", command = lambda: self.search(columns, table))
        search.grid(row = 3, column = 4)

        
    def search(self, columns, table):
        self.searchmaster = Tk()
        self.searchmaster.title('Search')

        self.s = StringVar(self.searchmaster)
        self.ser = StringVar(self.searchmaster)

        search_lab = Label(self.searchmaster, text = "Enter the data you want to search: ")
        search_lab.grid(row = 0, column = 3)

        ent_find = Entry(self.searchmaster, textvariable = self.s)
        ent_find.grid(row = 1, column = 3)

        col = []
        for i in self.columns:
            col.append(i[0])

        search_opt = OptionMenu(self.searchmaster, self.ser, *col)
        self.ser.set('--Select a field to search from--')
        search_opt.grid(row = 2, column = 3, pady = 10)


        searchb = Button(self.searchmaster, text = 'Search', command = lambda: self.get_data(self.ser.get(), columns, self.s.get(), 2, str(table)))
        searchb.grid(row = 3, column = 3)


    def get_data(self, column, columns, data, opt, table):

        if opt == 1:
            try:
                Q = 'SELECT ' + ', '.join(columns) + ' FROM ' + str(table)
                self.cq.execute(Q)
            except ImportError as e:
                print(e)
            else:
                return self.cq.fetchall()

        elif opt == 2:
            try:
                Q = 'SELECT  ' + ', '.join(columns) + ' FROM ' + table +  ' WHERE '  + column +'= (%s)'
                val = (data, )
                self.cq.execute(Q, val)
            except ImportError as e:
                messagebox.showerror(title = "ERROR", message = "Please check whether you have entered the proper data ")
                print(e)
            else:
                self.display.delete(*self.display.get_children())
                self.display_data(self.searchmaster, columns, self.cq.fetchall(), table )


    def get_column(self, columns):

        
        
        col = []
        col.append('employee_code')
        for i in columns:
            if i.get() == 'None':
                continue
            else:
                col.append(i.get())

        return tuple(col)


    def select(self):
        self.rad.destroy()
        self.rad1.destroy()
        self.sel.destroy()
        
        if self.selectvar.get() == 1:
            self.emp_att_access()
            return 1
        elif self.selectvar.get() == 2:
            self.emp_data_access()
            return 2


class manager:
    def __init__(selfroot, cursor, watch_code):
        self.data = cursor
        self.master = Tk()

        self.display = t.Treeview(self.master)
    
        self.displaybutton = Button(self.master, text = 'Display Data' , command = lambda: self.display_data(cursor))
        self.displaybutton.grid(row = 5, column = 2)

        self.sel_button = Button(self.master, text = 'Customize Display' , command = lambda: self.customize(cursor))
        self.sel_button.grid(row = 5, column = 2)
        
        w = 'Employee Code \n' + str(*manager_code)
        self.desig = Label(self.master, text = 'Designation \nProperty Manager')
        self.lab = Label(self.master, text = w)
        
        self.desig.grid(row = 0, column = 2)
        self.lab.grid(row = 0, column = 4)
    
    def customize(self):
        self.root = Tk()