import sqlite3
from books_publishers.book import book
from books_publishers.publisher import publisher


def open_connection():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()


def query_data_base(query, params):
    try:
        connection, cursor = open_connection()
        cursor.execute(query, params)
        connection.commit()
        data = cursor.fetchall()
        print(data)

    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        connection.close()


def create_books_table():
    try:
        connection, cursor = open_connection()
        query = """CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_title TEXT UNIQUE,
                    author TEXT,
                    selling_price REAL)
                """

        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)


def create_publisher_table():
    try:
        connection, cursor = open_connection()
        query = """CREATE TABLE IF NOT EXISTS publishers (
                    publisher_id integer PRIMARY KEY AUTOINCREMENT,
                    publisher_name text UNIQUE,
                    book_title text UNIQUE,
                    author text,
                    printing_quantiy integer,
                    printing_price integer)
                """

        cursor.execute(query)
    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)


create_books_table()
create_publisher_table()


def create_book(book):
    query = "INSERT INTO books VALUES (? ,?, ?, ?)"
    params = (book.book_id, book.book_title, book.author, book.selling_price)
    query_data_base(query, params)


book1 = book(None, "Tu gali", "Josef Murphy", 25.05)

create_book(book1)


def get_book(book):
    query = "SELECT * FROM books WHERE book_id = (?) OR book_title = (?) OR author = (?) OR selling_price = (?)"
    params = (book.book_id, book.book_title, book.author, book.selling_price)
    query_data_base(query, params)


get_book(book1)


def update_book(book):
    query = "UPDATE books SET book_title = 'Belekas' WHERE book_title = (?) OR book_id = (?) OR author = (?) OR selling_price = (?)"
    params = (book.book_title, book.book_id, book.author, book.selling_price)
    query_data_base(query, params)


update_book(book1)
get_book(book1)


def delete_book(book):
    query = "DELETE FROM books WHERE book_title = (?) OR book_id = (?) OR author = (?) OR selling_price = (?)"
    params = (book.book_title, book.book_id, book.author, book.selling_price)
    query_data_base(query, params)


# delete_book(book1)
# get_book(book1)


def create_publisher(publisher):
    query = "INSERT INTO publishers VALUES (?,?,?,?,?,?)"
    params = (publisher.publisher_id, publisher.publisher_name, publisher.book_title,
              publisher.author, publisher.printing_quantity, publisher.printing_price)
    query_data_base(query, params)


publisher1 = publisher(None, "Baltos_lankos", "Tu_gali", "Josef_Murphy", 5000, 8)

create_publisher(publisher1)


def get_publisher(publisher):
    query = """SELECT * FROM publishers WHERE publisher_id = (?) OR publisher_name = (?) OR book_title = (?) OR author = (?) OR
                    printing_quantiy = (?) OR printing_price = (?)"""
    params = (publisher.publisher_id, publisher.publisher_name, publisher.book_title,
              publisher.author, publisher.printing_quantity, publisher.printing_price)
    query_data_base(query, params)


get_publisher(publisher1)


def update_publisher(publisher):
    query = """UPDATE publishers set publisher_name = 'zalios_lankos' WHERE publisher_id = (?) OR 
                    publisher_name = (?) OR book_title = (?) OR author = (?) OR
                    printing_quantiy = (?) OR printing_price = (?) """
    params = (publisher.publisher_id, publisher.publisher_name, publisher.book_title,
              publisher.author, publisher.printing_quantity, publisher.printing_price)
    query_data_base(query, params)


#update_publisher(publisher1)
#get_publisher(publisher1)


def delete_publisher(publisher):
    query = """DELETE FROM publishers WHERE publisher_id = (?) OR 
                    publisher_name = (?) OR book_title = (?) OR author = (?) OR
                    printing_quantiy = (?) OR printing_price = (?) """
    params = (publisher.publisher_id, publisher.publisher_name, publisher.book_title,
              publisher.author, publisher.printing_quantity, publisher.printing_price)
    query_data_base(query, params)

# delete_publisher(publisher1)
# get_publisher(publisher1)
