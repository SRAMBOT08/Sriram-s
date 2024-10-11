import sqlite3
conn=sqlite3.connect('logdb1.db')
con=conn.cursor()
def create():
    con.execute('CREATE TABLE IF NOT EXISTS logdet(username TEXT,password TEXT)')
    conn.commit()
def registeruser(username,password):
    con.execute('INSERT INTO logdet VALUES(?,?)',(username,password))
    conn.commit()
def verifyuser(username,password):
    con.execute('SELECT*FROM logdet WHERE username=? AND password=?',(username,password))
    result=con.fetchone()
    return result
def cre():
    con.execute('CREATE TABLE IF NOT EXISTS PTBL(sno INTEGER PRIMARY KEY AUTOINCREMENT,date TEXT,hsn INTEGER,product TEXT,size TEXT,quantity INTEGER,gsm TEXT,rate REAL )')
    conn.commit()
def addnew(date,hsn,product,size,quantity,gsm):
    con.execute('INSERT INTO PTBL (date,hsn,product,size,quantity,gsm)VALUES (?,?,?,?,?,?)',(date,hsn,product,size,quantity,gsm))
    conn.commit()
def fetch():
    con.execute('SELECT * FROM PTBL')
    records = con.fetchall()
    return records
def fetchone(product, hsn):
    con.execute('SELECT * FROM PTBL WHERE product=? AND hsn=?', (product, hsn))
    record = con.fetchall()
    return record

def updt(hsn, date=None, product=None, size=None, quantity=None, gsm=None, rate=None):
    query = "UPDATE PTBL SET "
    params = []
    if date:
        query += "date=?, "
        params.append(date)
    if product:
        query += "product=?, "
        params.append(product)
    if size:
        query += "size=?, "
        params.append(size)
    if quantity:
        query += "quantity=?, "
        params.append(quantity)
    if gsm:
        query += "gsm=?, "
        params.append(gsm)
    if rate:
        query += "rate=?, "
        params.append(rate)
    query = query.rstrip(', ') + " WHERE hsn=?"
    params.append(hsn)
    con.execute(query,params)
    conn.commit()
def deleteproduct(hsn, product=None, size=None, gsm=None):
    query = "DELETE FROM PTBL WHERE hsn=?"
    params = [hsn]
    if product:
        query += " AND product=?"
        params.append(product)
    if size:
        query += " AND size=?"
        params.append(size)
    if gsm:
        query += " AND gsm=?"
        params.append(gsm)
    con.execute(query,params)
    conn.commit()


create()  
cre()
conn.close
