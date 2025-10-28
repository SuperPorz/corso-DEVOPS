drop database if exists lezione07;
create database lezione07;
use lezione07;

create table prodotti(
	idp int auto_increment primary key,
    nome varchar(25) not null,
    descrizione varchar(255),
    prezzo decimal(16,2) not null
);

insert into prodotti values 
(default, "cotoletta","bonroll aia", 4.12),
(default, "tofu","cibo merda", 9.56),
(default, "acqua","piscio liquido", 3.00),
(default, "padella","pezzo di ferraglia", 12.25);

select * from prodotti;
truncate prodotti;

create table carrello (
    idProdotto int primary key,
    quantita int not null,
    foreign key (idProdotto) references prodotti(idp) on update cascade on delete cascade
);

insert into carrello values 
(1, 10),
(2, 8);

select * from carrello;

insert into carrello values 
(1, 3);