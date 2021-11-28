CREATE TABLE inLine
(
    service_name varchar(45) not null,
    business_phone_num varchar(45) not null,
    customer_phone_num varchar(45) not null,
    position int null,
    minutes_left int null,
    primary key (service_name, business_phone_num, customer_phone_num),
    constraint business_phone_num_fk_inline
        foreign key (business_phone_num) references Services (business_phone_num)
            on update cascade on delete cascade,
    constraint service_name_fk
        foreign key (service_name) references Services (service_name)
            on update cascade on delete cascade,
    constraint customer_phone_num_fk_inline
        foreign key (customer_phone_num) references Customers (phone_num)
            on update cascade on delete cascade
);
