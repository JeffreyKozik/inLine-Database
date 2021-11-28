CREATE TABLE Services
(
    service_name varchar(45) not null,
    business_phone_num varchar(45) not null,
    primary key (service_name, business_phone_num),
    constraint business_phone_num_fk_services
        foreign key (business_phone_num) references Businesses (phone_num)
            on update cascade on delete cascade
);
