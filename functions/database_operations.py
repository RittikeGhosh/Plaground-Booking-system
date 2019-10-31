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
        search_data.append(i[1])
        # if i[4] not in search_data:
        #     search_data.append(i[4])
        # if i[7] not in search_data:
        #     search_data.append(i[7])
    return search_data
