import sqlite3 as db
#Задание 1
conn = db.connect('users.db')
c = conn.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
conn.commit()
#Задание 2
users_to_add = [(1, 'Dmitriy', 'davydov@gmail.com')]
conn = db.connect('users.db')
def insert(id, name, email):
    c = conn.cursor()
    c.execute("""INSERT INTO users.db(id, name, email) VALUES (:id, :name, :email)""",
              {id: id, name: name, email: email})
conn.commit()
#Задание 3
def select():
    c = conn.cursor()
    c.execute("""select * from users""")
    print(c.fetchall())
#Задание 4
def select_user(id):
    c = conn.cursor()
    c.execute("""select * from users where id=:id""", {"id": id})
print(c.fetchall())
#Задание 5
def delete_user(id):
    c = conn.cursor()
    c.execute("""delete from users where id=:id""", {"id": id})
print(c.fetchall())
conn.commit()


def delete_on_name(name):
    c = conn.cursor()
    c.execute("""delete from users where name=:name""", {"name": name})
print(c.fetchall())
conn.commit()

#Раздел II

#Задание 1

def main():
    select()
    select_user(1)
    delete_user(1)
    delete_on_name(1)
    select()