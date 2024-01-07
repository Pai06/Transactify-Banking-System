create database BankManager;
use BankManager;
create table Customer(CID varchar(15) NOT NULL primary key, Cname varchar(20), Address varchar(30), Email varchar(25));
create table Bank(ID varchar(15) NOT NULL primary key, Bname varchar(20), Location varchar(30));
create table Branch(BID varchar(15) NOT NULL primary key, BranchName varchar(20), Blocation varchar(30));create table Customer(CID varchar(15) NOT NULL primary key, Cname varchar(20), Address varchar(30), Email varchar(25));
create table Mobiles(CID varchar(15), MobileNumber varchar(15), foreign key(CID) references Customer(CID));
create table Accounts(ANO varchar(20) NOT NULL primary key, A_Type varchar(30), Balance integer, CID varchar(15), BID varchar(15), foreign key(CID) references Customer(CID), foreign key(BID) references Branch(BID));
create table Employee(EID varchar(15) NOT NULL primary key, DateofJoin date, DateofLeave date, Ename varchar(20), Phone varchar(15), Eaddress varchar(30), Salary integer, BID varchar(15), foreign key(BID) references Branch(BID));
create table Transactions(TID varchar(15) NOT NULL primary key, Amount integer, ANO varchar(15), foreign key(ANO) references Accounts(ANO), T_Type varchar(10) check (T_Type IN ('REM', 'INS')));
create table Loan(LID varchar(15) NOT NULL primary key, L_Type varchar(20), Amount integer, CID varchar(15), foreign key(CID) references Customer(CID));
create table PaymentPeriod(LID varchar(15), Period varchar(20), foreign key(LID) references Loan(LID));

INSERT INTO Customer (CID, Cname, Address, Email) VALUES ('1', 'John Doe', '123 Main St', 'john@example.com');
INSERT INTO Customer (CID, Cname, Address, Email) VALUES ('2', 'Jane Smith', '456 Elm St', 'jane@example.com');
INSERT INTO Customer (CID, Cname, Address, Email) VALUES ('3', 'Alice Johnson', '789 Oak St', 'alice@example.com');
INSERT INTO Customer (CID, Cname, Address, Email) VALUES ('4', 'Bob Williams', '101 Pine St', 'bob@example.com');
INSERT INTO Customer (CID, Cname, Address, Email) VALUES ('5', 'Eve Davis', '202 Cedar St', 'eve@example.com');

INSERT INTO Mobiles (CID, MobileNumber) VALUES ('1', '123-456-7890');
INSERT INTO Mobiles (CID, MobileNumber) VALUES ('1', '987-654-3210');
INSERT INTO Mobiles (CID, MobileNumber) VALUES ('2', '555-123-4567');
INSERT INTO Mobiles (CID, MobileNumber) VALUES ('3', '777-888-9999');
INSERT INTO Mobiles (CID, MobileNumber) VALUES ('4', '333-444-5555');
INSERT INTO Mobiles (CID, MobileNumber) VALUES ('4', '777-777-7777');
INSERT INTO Mobiles (CID, MobileNumber) VALUES ('5', '888-888-8888');
INSERT INTO Mobiles (CID, MobileNumber) VALUES ('5', '999-999-9999');

INSERT INTO Branch (BID, BranchName, Blocation) VALUES ('101', 'Downtown Branch', 'City Center');
INSERT INTO Branch (BID, BranchName, Blocation) VALUES ('102', 'Suburb Branch', 'Green Valley');
INSERT INTO Branch (BID, BranchName, Blocation) VALUES ('103', 'Westside Branch', 'Sunny Hills');
INSERT INTO Branch (BID, BranchName, Blocation) VALUES ('104', 'East End Branch', 'Riverfront');
INSERT INTO Branch (BID, BranchName, Blocation) VALUES ('105', 'Northside Branch', 'Mountain View');

INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES ('A101', 'Savings', 1000, '1', '101');
INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES ('A102', 'Checking', 500, '2', '102');
INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES ('A103', 'Savings', 2500, '3', '103');
INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES ('A104', 'Checking', 800, '4', '104');
INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES ('A105', 'Savings', 3500, '5', '105');
INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES ('A106', 'Checking', 1200, '1', '101');
INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES ('A107', 'Savings', 2200, '2', '102');
INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES ('A108', 'Checking', 1600, '3', '103');
INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES ('A109', 'Savings', 4200, '4', '104');
INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES ('A110', 'Checking', 1800, '5', '105');

INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES ('E101', '2022-01-15', NULL, 'John Smith', '123-456-7890', '123 Main St', 50000, '101');
INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES ('E102', '2021-03-20', NULL, 'Jane Doe', '987-654-3210', '456 Elm St', 60000, '102');
INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES ('E103', '2022-05-10', NULL, 'Alice Johnson', '555-123-4567', '789 Oak St', 55000, '103');
INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES ('E104', '2020-12-05', NULL, 'Bob Williams', '777-888-9999', '101 Pine St', 70000, '104');
INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES ('E105', '2023-02-18', NULL, 'Eve Davis', '333-444-5555', '202 Cedar St', 52000, '105');

INSERT INTO Transactions (TID, Amount, ANO, T_Type) VALUES ('T101', 500, 'A101', 'REM');
INSERT INTO Transactions (TID, Amount, ANO, T_Type) VALUES ('T102', 1000, 'A102', 'INS');
INSERT INTO Transactions (TID, Amount, ANO, T_Type) VALUES ('T103', 750, 'A103', 'REM');
INSERT INTO Transactions (TID, Amount, ANO, T_Type) VALUES ('T104', 300, 'A104', 'INS');
INSERT INTO Transactions (TID, Amount, ANO, T_Type) VALUES ('T105', 1200, 'A105', 'REM');

INSERT INTO Loan (LID, L_Type, Amount, CID) VALUES ('L101', 'Personal Loan', 10000, '1');
INSERT INTO Loan (LID, L_Type, Amount, CID) VALUES ('L102', 'Home Loan', 50000, '2');
INSERT INTO Loan (LID, L_Type, Amount, CID) VALUES ('L103', 'Auto Loan', 20000, '3');

INSERT INTO PaymentPeriod (LID, Period) VALUES ('L101', 'Monthly');
INSERT INTO PaymentPeriod (LID, Period) VALUES ('L102', 'Quarterly');
INSERT INTO PaymentPeriod (LID, Period) VALUES ('L103', 'Monthly');

select * from Transactions;
select * from accounts;

delimiter //
create function find_total_balance(customer_id int) returns decimal(10, 2) deterministic reads sql data 
begin
    declare total_balance decimal(10, 2);
    select sum(balance) into total_balance
    from accounts
    where cid = customer_id;
    return total_balance;
end;
end //
delimiter ;

select find_total_balance(5) AS total_balance;



CREATE TABLE IF NOT EXISTS BankManagerLog (
         LogID INT AUTO_INCREMENT PRIMARY KEY,
         TableName VARCHAR(20),
         Action VARCHAR(10),
         Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
delimiter $$
create trigger after_customer_update
after update on Customer
for each row
begin
    insert into BankManagerLog (TableName, Action) values ('Customer', 'Update');
end $$
delimiter ;

select * from Customer;

update Customer set Cname="Williamson" where CID=5;
select * from Customer;


select * from bankmanagerlog;


select * from transactions;

DELIMITER //
CREATE PROCEDURE ongoing_loans()
BEGIN 
	SELECT * from loan
    WHERE Amount > 10000;
END //
DELIMITER ;
CALL ongoing_loans();

SELECT *
FROM Customer
WHERE CID IN (
    SELECT CID
    FROM Loan
    WHERE Amount > 10000
);

-- Example of a correlated subquery to find customers with ongoing loans
SELECT *
FROM Customer c
WHERE EXISTS (
    SELECT 1 FROM Loan l
    WHERE l.CID = c.CID
    AND l.Amount > 10000
);

select * from Customer;



