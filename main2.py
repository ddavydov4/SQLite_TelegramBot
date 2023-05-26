import sqlite3 as db

# Задание 1
conn = db.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
conn.commit()


# Задание 2
def insert(id, name, email):
    c = conn.cursor()
    c.execute("""INSERT INTO users(id, name, email) VALUES (%, %, %)""", (id, name, email))
    conn.commit()


# Задание 3
def select():
    c = conn.cursor()
    c.execute("""SELECT * FROM users""")
    print(c.fetchall())


# Задание 4
def select_user(id):
    c = conn.cursor()
    c.execute("""SELECT * FROM users WHERE id=:id""", {"id": id})
    print(c.fetchall())


# Задание 5
def delete_user(id):
    c = conn.cursor()
    c.execute("""DELETE * FROM users WHERE id=:id""", {"id": id})
    conn.commit()


def delete_on_name(name):
    c = conn.cursor()
    c.execute("""DELETE * FROM users WHERE name=:name""", {"name": name})
    print(c.fetchall())
    conn.commit()


# Раздел II

# Задание 1

def main():
    print("asd")
    insert(1, 'Dmitriy', 'davydov@gmail.com')
    insert(2, 'Oleg', 'dsgfjhl@gmail.com')
    insert(3, 'Sergey', 'kljhsdf@gmail.com')
    select()
    select_user(1)
    delete_user(1)
    delete_on_name(1)
    select()

if __name__ == '__main__':
    main()
