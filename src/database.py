
# database.py
import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def main():
    database = "../db/inventory.db"

    sql_create_inventory_table = """CREATE TABLE IF NOT EXISTS Inventory (
                                        ProductID INTEGER PRIMARY KEY,
                                        ProductName TEXT NOT NULL,
                                        InStockUnit REAL NOT NULL,
                                        PricePerUnit REAL NOT NULL
                                    );"""

    sql_create_customerinfo_table = """CREATE TABLE IF NOT EXISTS CustomerInfo (
                                           CustomerID INTEGER PRIMARY KEY,
                                           FirstName TEXT NOT NULL,
                                           LastName TEXT NOT NULL,
                                           PhoneNumber TEXT NOT NULL,
                                           CreditCardNumber TEXT NOT NULL
                                       );"""

    sql_create_orderhistory_table = """CREATE TABLE IF NOT EXISTS OrderHistory (
                                           OrderID INTEGER PRIMARY KEY,
                                           CustomerID INTEGER,
                                           TotalPrice REAL NOT NULL,
                                           PurchaseDate DATETIME NOT NULL,
                                           FOREIGN KEY (CustomerID) REFERENCES CustomerInfo(CustomerID)
                                       );"""

    # Connect to the database
    conn = create_connection(database)

    # Create tables
    if conn is not None:
        create_table(conn, sql_create_inventory_table)
        create_table(conn, sql_create_customerinfo_table)
        create_table(conn, sql_create_orderhistory_table)
        conn.commit()
    else:
        print("Error! Cannot create the database connection.")

    # Close the connection
    if conn:
        conn.close()

if __name__ == '__main__':
    main()

