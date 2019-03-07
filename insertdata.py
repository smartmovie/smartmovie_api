import psycopg2
#postgres://egvknxuh:vOI9l6Yjcc9alsCIDIO3v1F_7aDyQRBM@manny.db.elephantsql.com:5432/egvknxuh

class InsertData:
    def __init__(self):
        self.conn = psycopg2.connect("dbname='tagitmnx' user='tagitmnx' host='manny.db.elephantsql.com' password='VTyQvPjzEtgozMnPgKKJ1Uc_czyEbXPK'")
        self.cur = self.conn.cursor()

    def insert_movie(self,name,thumb,trailer,status,type):
        sql = "insert into movie (moviename,thumbnail,trailer,status,type) values ('{}','{}','{}',{},'{}')".format(name,thumb,trailer,str(status),type)
        self.cur.execute(sql)
        self.conn.commit()
        self.close_connection()
        return "success"

    def insert_users(self,username,email,phone,password):
        sql = "insert into users (username,email,phone,password) values ("+"'"+username+"'"+","+"'"+email+"'"+","+"'"+phone+"'"+","+"'"+password+"'"")"
        self.cur.execute(sql)
        self.conn.commit()
        self.close_connection()
        return "success"

    def user_login_check(self,un,pw):
        sql = "select exists(select id from users where (username = '{}' or email = '{}' or phone = '{}') and password = '{}' )".format(un,un,un,pw)
        self.cur.execute(sql)
        query_result = self.cur.fetchall()
        self.close_connection()
        if query_result[0][0] == True:
            return 'true'
        else:
            return 'false'

    def homepage_data_now(self):
        sql = "select moviename,thumbnail from movie \
                where status = 1 "
        self.cur.execute(sql)
        query_result = self.cur.fetchall()
        self.close_connection()
        print(query_result)
        print(type(query_result))
        return "hello"


    def close_connection(self):
        self.cur.close()
        self.conn.close()








