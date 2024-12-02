create database customer;

use customer;

create table tb_customer(
	id integer auto_increment primary key,
    name varchar(50),
    age integer
);

insert into tb_customer (name, age) values 
('John Smith',30),
('Susan Warren',25)
;

select * from tb_customer;

update  tb_customer set name = "Harry Smith", age = "24" where id = 6;