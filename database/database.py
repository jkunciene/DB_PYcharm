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
    try:
        connection = sqlite3.connect("employee.db")
        connection_cursor = connection.cursor()
        connection_cursor.execute(
            """INSERT  INTO employees (first_name, last_name, pay_roll) VALUES (?, ?, ?) ('Jonas', 'Aitis', 21)""")
        connection.commit()
        connection.close()


    except:
        print(sqlite3.Error)
    finally:
        connection.close()


def select_employee():
    try:
        connection = sqlite3.connect("employee.db")
        connection_cursor = connection.cursor()
        connection_cursor.execute("""SELECT * FROM employees""")

        connection.commit()

        rows = []
        for row in connection_cursor.execute("""SELECT * FROM employees"""):
            rows.append(row)

        print(rows)

        connection.close()
        return rows

    except:
        print(sqlite3.Error)

    finally:
        connection.close()


def get_employees_for_admin():
    all = select_employee()
    print(all)

get_employees_for_admin()


def update_employee():
    connection = sqlite3.connect("employee.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE employees SET pay_roll = 30 WHERE id=3""")
    connection.commit()
    connection.close()


def delete_employee():
    connection = sqlite3.connect("employee.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""DELETE FROM employees WHERE id=7""")
    connection.commit()
    connection.close()


create_employee()
update_employee()
delete_employee()
select_employee()
