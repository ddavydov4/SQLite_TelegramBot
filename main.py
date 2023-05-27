import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users( id integer PRIMARY KEY UNIQUE, name text, email text)""")
conn.commit()


def insert(id, name, email):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO users  (id, name, email) VALUES (:id,:name,:email) """, {"id": id, "name": name, "email": email})
    conn.commit()


def select():
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users""")
    print(cursor.fetchall())


def select_user(id):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users WHERE id=:id""", {"id": id})
    print(cursor.fetchall())


def delete_user_id(id):
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM users WHERE id=:id""", {"id": id})
    print(cursor.fetchall())
    conn.commit()


def delete_user_name(name):
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM users WHERE name=:name""", {"name": name})
    print(cursor.fetchall())
    conn.commit()


def main():
    insert(1, 'Dmitriy', 'davydov@mail.ru')
    insert(2, 'Ivan', 'beketov@mail.ru')

    select()
    select_user(1)
    delete_user_id(2)
    delete_user_name('Dmitriy')
    select()

main()
conn.close()