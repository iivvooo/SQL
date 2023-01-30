import sqlite3
import csv

global conn
global cur

def DB():
    cur.execute('CREATE TABLE IF NOT EXISTS postnummer (\
    Postnummer     INTEGER PRIMARY KEY,\
    Poststed       TEXT,\
    kommunenummer  TEXT,\
    kommunenavn    TEXT,\
    kategori       TEXT\
    );')

    cur.execute('CREATE TABLE IF NOT EXISTS kunder (\
    kundenummer INTEGER PRIMARY KEY AUTOINCREMENT,\
    fname       TEXT,\
    lname       TEXT,\
    email       TEXT,\
    phone       INTEGER,\
    postnummer  INTEGER REFERENCES postnummer (postnummer));')



def siht():
    with open('Postnummerregister.csv', 'r') as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute('INSERT INTO postnummer VALUES (?, ?, ?, ?, ?)', row)
        conn.commit()
    print('suu')

    with open('randoms.csv', 'r') as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute('INSERT INTO kunder (fname, lname, email, phone, postnummer) VALUES (?, ?, ?, ?, ?)', row)
        conn.commit()
    print('suu')


def main():
    global conn
    global cur
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    DB()
    siht()

if __name__ == '__main__':
    main()