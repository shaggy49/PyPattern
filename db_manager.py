import sqlite3
from sqlite3 import Error

DBNAME = "pattern.db"

"""
aiuto: sqlite3, connect,cursor,execute,executemany, commit,close

classe vuota, tupla,dizionario, setattr()
"""


# conn = sqlite3.connect(DBNAME)

# conn.close()
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
    c.execute(
        """CREATE TABLE  if not exists pattern
                 (  name TEXT, 
                    tag TEXT,
                    matrix TEXT)"""
    )
    conn.commit()


"""[Insertion function]
### Returns:    1 inserimento effettuato con successo,
                0 matrice già presente
"""


def insert(name, tag, pattern, rotations):
    risultato = 0
    conn = create_connection()
    c = conn.cursor()
    # Insert a row of data
    if not search_pattern(rotations):
        c.execute("INSERT INTO pattern VALUES (?,?,?)", (name, tag, pattern))
        risultato = 1
        conn.commit()
    conn.close()
    return risultato


def clear():
    conn = sqlite3.connect(DBNAME)
    c = conn.cursor()

    # Drop table
    c.execute("""DROP TABLE pattern""")

    # Save (commit) the changes
    conn.commit()
    conn.close()


# valutare se spostare in un altro file
def or_generator(rotations):
    or_string = ""
    for i in range(len(rotations)):
        or_string += "matrix = '" + rotations[i] + "'"
        # mette gli or fino al penultimo elemento/ciclo
        if i < len(rotations) - 1:
            or_string += " OR "
    return or_string


def search_pattern(rotations):
    conn = sqlite3.connect(DBNAME)
    conn.row_factory = sqlite3.Row
    patternFound = None
    orList = or_generator(rotations)

    c = conn.cursor()
    for row in c.execute(f"SELECT * FROM pattern WHERE ({orList})"):
        patternFound = row["name"]
    conn.close()
    # print(patternFound)
    return patternFound
