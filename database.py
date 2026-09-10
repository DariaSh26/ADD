# создать таблицу компания и пользователи

# import sqlite3
#
# with sqlite3.connect('people.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS companies (     # companies - название таблицы
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS users (       # users - название таблицы
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER,
#         company_id INTEGER,
#         FOREIGN KEY(company_id) REFERENCES companies (id) ON DELETE        # внешний ключ из (company_id) связан с таблицей companies (id)
#     """)




# Создать три таблицы


# import sqlite3
#
# with sqlite3.connect('book.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS books (     # books - название таблицы
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         count_page INTEGER NOT NULL CHECK (count_page > 0),
#         price REAL CHECK (price > 0)
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS author (       # users - название таблицы
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER CHECK (age > 16)
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS author_books (       # author_books - название таблицы
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         books_id INTEGER NOT NULL,
#         author_id INTEGER NOT NULL,
#         FOREIGN KEY (books_id) REFERENCES books (id)
#         FOREIGN KEY (author_id) REFERENCES author (id)
#     )""")





# создание 4 таблиц

# import sqlite3
#
# with sqlite3.connect('people.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS student (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         surname TEXT,
#         name TEXT,
#         patronymic TEXT,
#         age INTEGER,
#         [group] INTEGER NOT NULL,
#         FOREIGN KEY([group]) REFERENCES groups (id)
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS groups (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         group_name  TEXT
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS association (
#         lesson_id INTEGER NOT NULL,
#         group_id INTEGER NOT NULL,
#         FOREIGN KEY(lesson_id) REFERENCES lessons (id)
#         FOREIGN KEY(group_id) REFERENCES groups (id)
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS lessons (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         lesson_title TEXT
#     )""")