CREATE TABLE Visits
(
    customer_phone_num varchar(45) not null,
    business_phone_num varchar(45) not null,
    primary key (customer_phone_num, business_phone_num),
    visit_date timestamp null,
    constraint customer_phone_num_fk
        foreign key (customer_phone_num) references Customers (phone_num)
            on update cascade on delete cascade,
    constraint business_phone_num_fk
        foreign key (business_phone_num) references Businesses (phone_num)
            on update cascade on delete cascade
);
