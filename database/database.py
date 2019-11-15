import sqlite3


def create_employee_table():
    connection = sqlite3.connect("employee.db")

    connection_cursor = connection.cursor()
    connection_cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                                                id integer PRIMARY KEY,
                                                first_name text,
                                                last_name text,
                                                pay_roll integer
                                                )""")
    connection_cursor.execute("""INSERT  INTO employees (first_name, last_name, pay_roll) VALUES (Jonas, Aitis, 21)""")
    connection.commit()
    connection.close()


create_employee_table()


def create_employee():
    connection = sqlite3.connect("employee.db")
    connection.execute("""INSERT  INTO employees (first_name, last_name, pay_roll) VALUES (Jonas, Aitis, 21)""")


def select_employee():
    connection = sqlite3.connect("employee.db")
    connection.execute("""SELECT * FROM employees""")


def update_employee():
    connection = sqlite3.connect("employee.db")
    connection.execute("""UPDATE employees SET pay_roll = '30' WHERE id=1""")


def delete_employee():
    connection = sqlite3.connect("employee.db")
    connection.execute("""DELETE FROM employees WHERE id=1 LIMIT 1""")
