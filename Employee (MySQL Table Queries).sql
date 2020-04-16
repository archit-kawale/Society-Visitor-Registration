create table employee
(
employee_code bigint(50) primary key not null auto_increment,
e_firstname varchar(25) not null,
e_lastname varchar(25) not null,
e_address varchar(100) not null,
e_mobile bigint(20) not null,
passwd varchar(25) not null string_to_encrypt,
e_birthday varchar(20) not null,
e_joindate varchar(20) not null,
e_designation varchar(20) not null
);

















if (s.passwd == s.rpasswd):
        a = True
    else:
        messagebox.showerror(title = "ERROR", message = "Password does not match")
        a = False
        return

    #Checking if a valid designation is entered
