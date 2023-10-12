//
create table doctor_425 (doctor_id varchar(5) PRIMARY KEY,
                    doctor_name varchar(50),
                    specilization varchar(50)
                     );
create table customer_425(customer_id varchar(30) PRIMARY KEY,
                      customer_name varchar(50),
                      doctor_id varchar(5),
                      ph_no int, 
                      addr varchar(50),
                      FOREIGN KEY(doctor_id) References doctor_425(doctor_id));
                      //
create table drug_425(drug_id varchar(10),
                drug_name varchar(30),
                stock_required int,
                customer_id varchar(30),
                FOREIGN KEY(customer_id) References customer_425(customer_id),
                FOREIGN KEY(drug_id) REFERENCES inventory_425(drug_id)
                );
           
create table inventory_425(drug_id varchar(10) PRIMARY KEY,
                        drug_name varchar(30),
                        stock_present int,
                        cost int,
                        company_name varchar(30),
                        date_of_prod date,
                        months_of_expiry int,
                        dose int
                           );
create table employee_425(employee_id varchar(5)  PRIMARY KEY,
                      emp_name varchar(50),
                      passwd varchar(25),
                      cont_info int,
                      );
create payment_info_425(transc_id varchar(20) PRIMARY KEY,
                    payment_method varchar(30)
                    total_amt int,
                    p_date datetime,
                    employee_id varchar(5),
                    customer_id varchar(5),
                    FOREIGN KEY(employee_id) REFERENCES employee_425(employee_id),
                    FOREIGN KEY(customer_id) REFERENCES drug_425(drug_id)
                    );

                    
/* insertion*/
insert into employee_425 values('E001',"Rohith",'8657',9458671235), ("E002","syed","9457",8974586213), ("E003",'Pragathi','4684',8974861237), ("E005","joel",'5789',9745862333), ("E004",'shriya','8974',8795643222);
LOAD DATA INFILE "doctor.csv" INTO TABLE doctor_425 
COLUMNS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
ESCAPED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;
/* use joins to print all the drug which are not being sold""
*/
/* 2*/
select drug_425.drug_name,sum(stock_required),sum(stock_present) from inventory_425 join drug_425 on drug_425.drug_id=inventory_425.drug_id and  stock_required>stock_present group by(drug_425.drug_name);
/*1*/
Select doctor_425.doctor_name,count(customer_425.customer_name) as count_of_customer from doctor_425 left join customer_425 on doctor_425.doctor_id=customer_425.doctor_id group by (doctor_425.doctor_id) ;
/*3*/
DELIMITER $$
CREATE FUNCTION TOTAL_AMOUNT(id varchar(30))
returns int
deterministic
begin
declare total_amount_to_paid int;
declare res longtext;
set total_amount_to_paid=(select sum(inventory_425.cost*drug_425.stock_required) from drug_425 join inventory_425 on inventory_425.drug_id=drug_425.drug_id and customer_id=id);
set res=concat("The total amount to be paid",Convert(total_amount_to_paid,char));
return res;
end $$
delimiter ;
/* procedure*/

DELIMITER $$
CREATE PROCEDURE proc3(IN customerid varchar(255), OUT message varchar(100))
BEGIN
DECLARE amt int;
set amt = (SELECT total_amt FROM payment_425 WHERE payment_425.customer_id=customerid);
IF amt>0 THEN
    set message = ('Amount has been  already updated ');
ELSE
set amt=(select sum(inventory_425.cost*drug_425.stock_required) from drug_425 join inventory_425 on inventory_425.drug_id=drug_425.drug_id and customer_id=customerid);
    update payment_425
    set p_date=CURRENT_DATE(),total_amt=amt
    WHERE payment_425.customer_id=customerid;
    set message = 'Amount has been currently updated';
END IF;
END $$
DELIMITER ;
/* trigger */
/*task1*/
DELIMITER $$
 CREATE TRIGGER insert_compartment1 BEFORE insert on compartment_425 For each row BEGIN DECLARE c int; 
DECLARE error_msg varchar(255); 
set error_msg=('CANNOT INSERT AS COMPARTMENT NUMBER EXCEEDS 4'); 
select count(Comp_no) into c from compartment_425 where Train_No=new.Train_No;
 If c>=4 then
 SIGNAL SQLSTATE '45000' set message_text=error_msg;
 End if; 
END$$
 DELIMITER ;
/* Vaild insertion:*/
Insert into compartment_425 values(“F01”,”I class”,80,8,45613);

/*Invalid insertion:*/

Insert into compartment_425 values(“G01”,”II class”,23,4,45613);


DELIMITER $$
 CREATE TRIGGER insert_drug BEFORE insert on drug_425 
 For each row 
 BEGIN 
 
 declare stockp int ;
 declare stockr int;
DECLARE error_msg varchar(255); 
set error_msg=('cant purchase , out of stock'); 
set stockr=new.stock_required;
set stockp=(select stock_present from inventory_425 where drug_id=new.drug_id);
 If stockr> stockp then
 SIGNAL SQLSTATE '45000' set message_text=error_msg;
 End if; 
END$$
 DELIMITER ;
 /* cursor*/
Create table backup(drug_id varchar(10),drug_name varchar(30),stock_required int,customer_id varchar(30));
DELIMITER $$
CREATE PROCEDURE backup()
 BEGIN
 DECLARE done INT DEFAULT 0;
 DECLARE drugid varchar(10);
 DECLARE customerid ,drugname varchar(30);
 DECLARE stockrequired int;
 DECLARE cur CURSOR FOR SELECT * FROM drug_425;
 DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
 OPEN cur;
 label: LOOP
 FETCH cur INTO drugid,drugname, stockrequired, customerid;
 INSERT INTO backup VALUES(drugid, drugname, stockrequired,customerid);
 IF done = 1 THEN LEAVE label;
 END IF; 
END LOOP;
 CLOSE cur;
 END$$
DELIMITER ; 



 