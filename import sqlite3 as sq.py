import sqlite3 as sq
import pandas as pn

def main():

    conn = sq.connect('Kunder.db')

    c = conn.cursor()

    data = pn.read_csv('randoms.csv')

    data.to_sql('kunder', conn, if_exists="replace", index = False)
    
    conn.commit()

    print(c.fetchall())

    conn.close()

main()