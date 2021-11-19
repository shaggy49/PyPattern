import sqlite3
from sqlite3 import Error
import datetime
import sys

DBNAME = 'pattern.db'

'''
aiuto: sqlite3, connect,cursor,execute,executemany, commit,close

classe vuota, tupla,dizionario, setattr()
'''

#conn = sqlite3.connect(DBNAME)

#conn.close()
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DBNAME)
    except Error as e:
        print(e)
    finally:
        if conn: 
            conn.close
    return conn

def init():
    conn = create_connection()
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE  if not exists pattern
                 (name TEXT, tag TEXT,matrix text)''')
    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    #conn.close()

def insert(name, tag, pattern):
    conn = create_connection()
    c = conn.cursor()

    # Insert a row of data
    c.execute("INSERT INTO pattern VALUES (?,?,?)", (name,tag,pattern))
    # c.execute("INSERT INTO pattern VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()

def clear():

    conn = sqlite3.connect(DBNAME)
    c = conn.cursor()

    # Drop table
    c.execute('''DROP TABLE pattern''')

    # Save (commit) the changes
    conn.commit()
    conn.close()

def search_pattern(rotations,tag):
    conn = sqlite3.connect(DBNAME)
    conn.row_factory = sqlite3.Row  

    c = conn.cursor()
    #TODO gestione eccezioni
    for row in c.execute("SELECT * FROM pattern WHERE tag = '%s'" % tag):
        print(row["name"])
    conn.close()

class riga():
    pass

def convert(rs):
    for val in rs:
        ret = riga()
        ret.date = val[0]
        ret.trans = val[1]
        ret.symbol = val[2]
        ret.qty = val[3]
        ret.price = val[4]
        yield ret

def convertStr(rs, attrnames):
    # ovviamente occorre mettere tutti gli attributi per allineamento fino
    # all'indice richiesto
    # generatore che restituyisce un oggetto di classe riga
    # con nomi attributi definiti tramite "setattr"
    for val in rs:
        ret = riga()
        for index in range (0,len(attrnames)):
            setattr(ret,attrnames[index],val[index])
        yield ret

def convertDict(rs, attrs):
    # generatore che restituyisce un dizionario ,
    # nome colonna -> valore
    for val in rs:
        ret = dict()
        for anum in attrs.keys():
            ret[attrs[anum]] = val[anum]
        yield ret


"""
if True:
    insert()
    #search()
else:
    clear()
"""