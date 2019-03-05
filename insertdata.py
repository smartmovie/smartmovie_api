import psycopg2
#postgres://egvknxuh:vOI9l6Yjcc9alsCIDIO3v1F_7aDyQRBM@manny.db.elephantsql.com:5432/egvknxuh

class InsertData:
    def __init__(self):
        self.conn = psycopg2.connect("dbname='tagitmnx' user='tagitmnx' host='manny.db.elephantsql.com' password='VTyQvPjzEtgozMnPgKKJ1Uc_czyEbXPK'")
        self.cur = self.conn.cursor()

    def insert_movie(self,name,thumb,trailer):
        #cur,conn = connect_database()
        sql = "insert into movie (moviename,thumbnail,trailer) values ("+"'"+name+"'"+","+"'"+thumb+"'"+","+"'"+trailer+"'"+")"
        self.cur.execute(sql)
        self.conn.commit()
        self.close_connection()
        return "success"

    def insert_users(self,username,email,phone,password):
        #cur,conn = connect_database()
        sql = "insert into users (username,email,phone,password) values ("+"'"+username+"'"+","+"'"+email+"'"+","+"'"+phone+"'"+","+"'"+password+"'"")"
        self.cur.execute(sql)
        self.conn.commit()
        self.close_connection()
        return "success"

    def close_connection(self):
        self.cur.close()
        self.conn.close()







