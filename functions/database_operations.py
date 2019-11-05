import sqlite3 as sl

# connecting to database
def db_connection(db_file):
    try:
        conn = sl.connect(db_file)
    except:
        print('Unable to connect to Database')
    return conn

# selecting from playground table
def select_from_playground(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM playgrounds")
    playground_data = cur.fetchall()
    conn.close()
    search_data = []
    for i in playground_data:
        x = []
        x.append(i[0])
        x.append(i[1])
        search_data.append(x)
    return search_data

def retrive_f_id(conn, s):
    cur = conn.cursor()
    cur.execute("SELECT * FROM playgrounds")
    playground_data = cur.fetchall()
    conn.close()
    for i in playground_data:
        if(i[1] == s):
            x = i[0]
            return x
