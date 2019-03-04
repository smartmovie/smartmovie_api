import psycopg2
#postgres://egvknxuh:vOI9l6Yjcc9alsCIDIO3v1F_7aDyQRBM@manny.db.elephantsql.com:5432/egvknxuh
def connect_database():
    try:
        conn = psycopg2.connect("dbname='egvknxuh' user='egvknxuh' host='manny.db.elephantsql.com' password='vOI9l6Yjcc9alsCIDIO3v1F_7aDyQRBM'")
    except:
        print("I am unable to connect to the database")
    cur = conn.cursor()
    return cur,conn


def insert_movie(name,thumb,trailer):
    cur,conn = connect_database()
    sql = "insert into movie (moviename,thumbnail,trailer) values ("+"'"+name+"'"+","+"'"+thumb+"'"+","+"'"+trailer+"'"+")"
    cur.execute(sql)
    conn.commit()
    return "success"

def insert_user()
