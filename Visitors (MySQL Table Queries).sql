create table visitors
(
sr_no bigint(10) primary key not null auto_increment,
first_name varchar(25) not null,
last_name varchar(25) not null,
mobile bigint(25) not null,
address varchar(100) not null,
wing varchar(5) not null,
flat int(5) not null,
purpose varchar(50) not null,
company_name varchar(50) default 'NULL',
cin_date varchar(20) not null,
cin_time varchar(20) not null,
cout_date varchar(20) default 'NULL',
cout_time varchar(20) default 'NULL',
watchman_code int(10) not null 
);