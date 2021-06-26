import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_table(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5433'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO store VALUES('%s','%s,'%s')" % (item,quantity,price)) // prevent injection, dont use this
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",  (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_table(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update_table(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close()

create_table()
#view()
update_table(11,6,"water glass")
insert_table("water glass",10,10)
#delete_table("water glass")
print(view())