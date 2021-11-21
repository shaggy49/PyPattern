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

def insert(name, tag, pattern, rotations):

    """[Insertion function]
    ### Returns:
        Integer -- 0 inserimento effettuato con successo, 1 matrice già presente
    """

    risultato = 0
    conn = create_connection()
    c = conn.cursor()
    # Insert a row of data
    if(not search_pattern(rotations,tag)):
        c.execute("INSERT INTO pattern VALUES (?,?,?)", (name,tag,pattern))
        risultato = 1
        print("Insert success")
        conn.commit()
    conn.close()
    print(risultato)
    return risultato

def clear():

    conn = sqlite3.connect(DBNAME)
    c = conn.cursor()

    # Drop table
    c.execute('''DROP TABLE pattern''')

    # Save (commit) the changes
    conn.commit()
    conn.close()

#valutare se spostare in un altro file
def orGenerator(rotations):
    or_string = ''
    for i in range(len(rotations)):
        or_string += "matrix = '" + rotations[i] + "'"
        #mette gli or fino al penultimo elemento/ciclo
        if(i<len(rotations)-1):
            or_string += " OR "
    return or_string

def search_pattern(rotations,tag):
    conn = sqlite3.connect(DBNAME)
    conn.row_factory = sqlite3.Row
    patternFound = None
    orList = orGenerator(rotations)

    c = conn.cursor()
    #TODO gestione eccezioni
    #! molto pericolosa, ma non riusciamo a farla funzionare in altri modi
    for row in c.execute(f'SELECT * FROM pattern WHERE (tag=\'{tag}\') AND ({orList})'):
        patternFound = row["name"]
    conn.close()
    print(patternFound)
    return patternFound

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