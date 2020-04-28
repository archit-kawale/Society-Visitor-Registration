create table emp_pass
(
    employee_code bigint(10) primary key not null auto_increment,
    e_password varchar(25) not null,
    foreign key (employee_code) references employee (employee_code)
);