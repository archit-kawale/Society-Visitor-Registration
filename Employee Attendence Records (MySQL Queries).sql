create table employee_attendence_records
(
    sr_no int primary key not null auto_increment,
    employee_code bigint(10) not null,
    e_cin_date varchar(12) not null,
    e_cin_time varchar(12) not null,
    e_cout_date varchar(12) default 'NULL',
    e_cout_time varchar(12) default 'NULL'
);

alter table employee auto_increment = 4000;