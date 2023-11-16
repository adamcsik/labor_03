import sqlite3

kapcsolat = None
ab = None

def ab_lerehoz():
    global kapcsolat, ab
    kapcsolat = sqlite3.connect("dolgozok.db")
    ab = kapcsolat.cursor()
    ab.execute('CREATE TABLE IF NOT EXISTS dolgozok (email TEXT, jelszo TEXT)')

def ab_rogzites(email, jelszo):
    ab.execute('INSERT INTO dolgozok VALUES (?, ?)', (email, jelszo))
    kapcsolat.commit()

def ab_jelszokeres(email):
    jelszo = ""
    ab.execute('SELECT * FROM dolgozok')
    dolgozok = ab.fetchall()
    for rekord in dolgozok:
        if rekord[0] == email:
            jelszo = rekord[1]
    return jelszo

def ab_lezar():
    global kapcsolat, ab
    ab.close()
    kapcsolat.close()
