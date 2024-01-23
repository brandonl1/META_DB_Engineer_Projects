
#Brandon Luy
#Meta Database Engineer Final Project
#Little Lemon Database Project

#Establish connection between MYSQL Connector and Python, using my own username and password
#Note: Clear User Creditentials before uplaoding to GIT
# Import MySQL Connector/Python
import mysql.connector as connector
connection=connector.connect(user="root",password="Rondonash!1")


#Create Cursor to communicate with SQL
cursor = connection.cursor()


# Check if the database exists and create it if it doesn't
cursor.execute("SHOW DATABASES")
if 'little_lemon_db' not in [db[0] for db in cursor]:
    cursor.execute("CREATE DATABASE little_lemon_db")

# Use the database
cursor.execute("USE little_lemon_db")

#Create Tables for Database (MenuItems, Menu, Bookings, Orders, Employee)

#MenuItems
# Create Tables
create_menuitem_table = """CREATE TABLE IF NOT EXISTS MenuItems (
    ItemID INT AUTO_INCREMENT,
    Name VARCHAR(200),
    Type VARCHAR(100),
    Price INT,
    PRIMARY KEY (ItemID)
);"""

#Menu
create_menu_table = """CREATE TABLE IF NOT EXISTS Menus (
    MenuID INT,
    ItemID INT,
    Cuisine VARCHAR(100),
    PRIMARY KEY (MenuID,ItemID)
);"""

#Bookings
create_booking_table = """CREATE TABLE IF NOT EXISTS Bookings (
    BookingID INT AUTO_INCREMENT,
    TableNo INT,
    GuestFirstName VARCHAR(100) NOT NULL,
    GuestLastName VARCHAR(100) NOT NULL,
    BookingSlot TIME NOT NULL,
    EmployeeID INT,
    PRIMARY KEY (BookingID)
);"""

#Orders
create_orders_table = """CREATE TABLE IF NOT EXISTS Orders (
    OrderID INT,
    TableNo INT,
    MenuID INT,
    BookingID INT,
    BillAmount INT,
    Quantity INT,
    PRIMARY KEY (OrderID,TableNo)
);"""

#Employees
create_employees_table = """CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR (255),
    Role VARCHAR (100),
    Address VARCHAR (255),
    Contact_Number INT,
    Email VARCHAR (255),
    Annual_Salary VARCHAR (100)
);"""

# Function to check if a table exists and create it if it doesn't
def create_table_if_not_exists(cursor, create_table_sql, table_name):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    result = cursor.fetchone()
    if not result:
        cursor.execute(create_table_sql)

# Create MenuItems table if not exists
create_table_if_not_exists(cursor, create_menuitem_table, 'MenuItems')

# Create Menus table if not exists
create_table_if_not_exists(cursor, create_menu_table, 'Menus')

# Create Bookings table if not exists
create_table_if_not_exists(cursor, create_booking_table, 'Bookings')

# Create Orders table if not exists
create_table_if_not_exists(cursor, create_orders_table, 'Orders')

# Create Employees table if not exists
create_table_if_not_exists(cursor, create_employees_table, 'Employees')


#*******************************************************#
# Insert query to populate "MenuItems" table:
#*******************************************************#
insert_menuitems = """
INSERT INTO MenuItems (Name, Type, Price)
VALUES
('Olives', 'Starters', 5),
('Flatbread', 'Starters', 5),
('Minestrone', 'Starters', 8),
('Tomato bread', 'Starters', 8),
('Falafel', 'Starters', 7),
('Hummus', 'Starters', 5),
('Greek salad', 'Main Courses', 15),
('Bean soup', 'Main Courses', 12),
('Pizza', 'Main Courses', 15),
('Greek yoghurt', 'Desserts', 7),
('Ice cream', 'Desserts', 6),
('Cheesecake', 'Desserts', 4),
('Athens White wine', 'Drinks', 25),
('Corfu Red Wine', 'Drinks', 30),
('Turkish Coffee', 'Drinks', 10),
('Turkish Coffee', 'Drinks', 10),
('Kabasa', 'Main Courses', 17);
"""


#*******************************************************#
# Insert query to populate "Menu" table:
#*******************************************************#
insert_menu="""
INSERT INTO Menus (MenuID,ItemID,Cuisine)
VALUES
(1, 1, 'Greek'),
(1, 7, 'Greek'),
(1, 10, 'Greek'),
(1, 13, 'Greek'),
(2, 3, 'Italian'),
(2, 9, 'Italian'),
(2, 12, 'Italian'),
(2, 15, 'Italian'),
(3, 5, 'Turkish'),
(3, 17, 'Turkish'),
(3, 11, 'Turkish'),
(3, 16, 'Turkish');"""

#*******************************************************#
# Insert query to populate "Bookings" table:
#*******************************************************#
insert_bookings="""
INSERT INTO Bookings (BookingID, TableNo, GuestFirstName, 
GuestLastName, BookingSlot, EmployeeID)
VALUES
(1, 12, 'Anna','Iversen','19:00:00',1),
(2, 12, 'Joakim', 'Iversen', '19:00:00', 1),
(3, 19, 'Vanessa', 'McCarthy', '15:00:00', 3),
(4, 15, 'Marcos', 'Romero', '17:30:00', 4),
(5, 5, 'Hiroki', 'Yamane', '18:30:00', 2),
(6, 8, 'Diana', 'Pinto', '20:00:00', 5);"""

#*******************************************************#
# Insert query to populate "Orders" table:
#*******************************************************#
insert_orders="""
INSERT INTO Orders (OrderID, TableNo, MenuID, BookingID, Quantity, BillAmount)
VALUES
(1, 12, 1, 1, 2, 86),
(2, 19, 2, 2, 1, 37),
(3, 15, 2, 3, 1, 37),
(4, 5, 3, 4, 1, 40),
(5, 8, 1, 5, 1, 43);"""

#*******************************************************#
# Insert query to populate "Employees" table:
#*******************************************************#
insert_employees = """
INSERT INTO Employees (Name, Role, Address, Contact_Number, Email, Annual_Salary)
VALUES
('Mario Gollini', 'Manager', '724, Parsley Lane, Old Town, Chicago, IL', 351258074, 'Mario.g@littlelemon.com', '$70,000'),
('Adrian Gollini', 'Assistant Manager', '334, Dill Square, Lincoln Park, Chicago, IL', 351474048, 'Adrian.g@littlelemon.com', '$65,000'),
('Giorgos Dioudis', 'Head Chef', '879 Sage Street, West Loop, Chicago, IL', 351970582, 'Giorgos.d@littlelemon.com', '$50,000'),
('Fatma Kaya', 'Assistant Chef', '132 Bay Lane, Chicago, IL', 351963569, 'Fatma.k@littlelemon.com', '$45,000'),
('Elena Salvai', 'Head Waiter', '989 Thyme Square, EdgeWater, Chicago, IL', 351074198, 'Elena.s@littlelemon.com', '$40,000'),
('John Millar', 'Receptionist', '245 Dill Square, Lincoln Park, Chicago, IL', 351584508, 'John.m@littlelemon.com', '$35,000');
"""

# Populate MenuItems table
cursor.execute(insert_menuitems)
#print rows in table to check number of
print("Total number of rows in MenuItem table: {}\n".format(cursor.rowcount))
connection.commit()

# Populate MenuItems table
cursor.execute("TRUNCATE TABLE Menus")
cursor.execute(insert_menu)
print("Total number of rows in Menu table: {}\n".format(cursor.rowcount))
connection.commit()

# Populate Bookings table
cursor.execute("TRUNCATE TABLE Bookings")
cursor.execute(insert_bookings)
print("Total number of rows in Booking table: {}\n".format(cursor.rowcount))
connection.commit()

# Populate Orders table
cursor.execute("TRUNCATE TABLE Orders")
cursor.execute(insert_orders)
print("Total number of rows in Orders table: {}\n".format(cursor.rowcount))
connection.commit()

# Populate Employees table
cursor.execute("TRUNCATE TABLE Employees")
cursor.execute(insert_employees)
print("Total number of rows in Employees table: {}\n".format(cursor.rowcount))
connection.commit()

#close connection and return to pool

#Now we are going to create and connect a pool with 2 connections
# Import MySQLConnectionPool class
from mysql.connector.pooling import MySQLConnectionPool

# Import Error class
from mysql.connector import Error
import mysql.connector as connector
dbconfig={"database":"little_lemon_db", "user":"root", "password":"Rondonash!1"}
try:
    pool = MySQLConnectionPool(pool_name="pool_b", pool_size=2, host='localhost', **dbconfig)
    print("The connection pool is created with name:", pool.pool_name)
    print("The pool size is:", pool.pool_size)
except Error as err:
    print("Error Code:", err.errno)
    print("Error Message:", err.msg)

#if done correctly then output should be The connection pool is created with name: pool_b The pool size is: 2
print("Getting a connection from the pool.")

connection = pool.get_connection()
cursor = connection.cursor()
# Dropping the procedure if it exists
try:
    cursor.execute("DROP PROCEDURE IF EXISTS PeakHours")
except connector.Error as err:
    print("Error dropping procedure: {}".format(err))
print("'connection' object is created with a connection from the pool")

#Now create a query for "PROCEDURE" for PeakHours
#Hour for hour in BookingSlot
#Count on hour to count number of bookings
#Group By on Booking hour, Order By on Bookings in descending order
peak_hours = """
CREATE PROCEDURE PeakHours()
BEGIN
    SELECT HOUR(BookingSlot) AS BookingHour, COUNT(*) AS NumberOfBookings
    FROM Bookings
    GROUP BY BookingHour
    ORDER BY NumberOfBookings DESC;
END;
"""
#running procedure query invoding execute moduel
cursor.execute(peak_hours)

#callproc to call stored procedure
cursor.callproc('PeakHours')

res = next(cursor.stored_results())
set = res.fetchall()

#Fetch results in dataset variable, and print results
for column_id in cursor.stored_results():
    cols = [column[0] for column in column_id.description]
print(cols)
for data in set:
    print(data)
#close connections, clean up
cursor.close()
connection.close()


#TASK 3: IMPLEMENT A STORED PROCEDURE GUEST STATUS
#Creating procedure for guest status
guest_status = """
#DROP Procedure in case if it exists already, if so then drop it
DROP PROCEDURE IF EXISTS GuestStatus;
CREATE PROCEDURE GuestStatus()
BEGIN
    SELECT CONCAT(b.GuestFirstName, ' ', b.GuestLastName) AS GuestName,
           CASE e.Role
               WHEN 'Manager' THEN 'Ready to pay'
               WHEN 'Assistant Manager' THEN 'Ready to pay'
               WHEN 'Head Chef' THEN 'Ready to serve'
               WHEN 'Assistant Chef' THEN 'Preparing Order'
               WHEN 'Head Waiter' THEN 'Order served'
           END AS OrderStatus
    FROM Bookings b
    LEFT JOIN Employees e ON b.EmployeeID = e.EmployeeID;
END;
"""

import mysql.connector as connector

# Assuming you have already created a connection pool named pool
connection = pool.get_connection()
cursor = connection.cursor()

# Run the stored procedure query with multi=True, because multiple statements
try:
    cursor.execute(guest_status, multi=True)
except connector.Error as err:
    print("Error: {}".format(err))

# Invoke callproc to call the stored procedure
cursor.callproc('GuestStatus')

# Fetch the results and print
for result in cursor.stored_results():
    dataset = result.fetchall()
    columns = [column[0] for column in result.description]
    print("Column names:", columns)
    for row in dataset:
        print(row)

# Close the cursor and connection return back to pool
cursor.close()
connection.close()
