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
    connection.commit()
    connection.close()


create_employee_table()


def create_employee():
    connection = sqlite3.connect("employee.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute(
        """INSERT  INTO employees (first_name, last_name, pay_roll) VALUES ('Jonas', 'Aitis', 21)""")
    connection.commit()
    connection.close()


create_employee()


def select_employee():
    connection = sqlite3.connect("employee.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""SELECT * FROM employees""")
    connection.close()


select_employee()


def update_employee():
    connection = sqlite3.connect("employee.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE employees SET pay_roll = 30 WHERE id=1""")
    connection.commit()
    connection.close()


update_employee()


def delete_employee():
    connection = sqlite3.connect("employee.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""DELETE FROM employees WHERE id=1""")
    connection.commit()
    connection.close()


delete_employee()
