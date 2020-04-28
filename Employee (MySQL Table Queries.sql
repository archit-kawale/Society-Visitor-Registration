create table employee
(
employee_code bigint(10) primary key not null auto_increment,
e_firstname varchar(25) not null,
e_lastname varchar(25) not null,
e_address varchar(100) not null,
e_mobile bigint(20) not null,
e_birthday varchar(20) not null,
e_joindate varchar(20) not null,
e_designation varchar(20) not null
);