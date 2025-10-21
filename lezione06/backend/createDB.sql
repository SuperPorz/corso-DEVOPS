drop database if exists lezione06;
create database lezione06;
use lezione06;

create table users(
	cf varchar(16),
    nome varchar(25),
    cognome varchar(25)
);

insert into users values 
	("bttmrc", "mirco", "botti"),
    ("lrnmch", "lorenzo", "michelon");
