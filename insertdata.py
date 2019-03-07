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

    def homepage_movie_data(self):
        sql_now = "select moviename,type,thumbnail,trailer \
                from movie \
                where status = 1 "
        sql_next = "select moviename,type,thumbnail,trailer \
                from movie \
                where status = 2 "
        self.cur.execute(sql_now)
        query_result_now = self.cur.fetchall()
        self.cur.execute(sql_next)
        query_result_next = self.cur.fetchall()
        self.close_connection()
        list_now = []
        for i in query_result_now:
            dict_now = {'movie_name':i[0],'type':i[1],'thumbnail':i[2],'trailer':i[3]}
            list_now.append(dict_now)
        list_next = []
        for i in query_result_next:
            dict_next = {'movie_name':i[0],'type':i[1],'thumbnail':i[2],'trailer':i[3]}
            list_next.append(dict_next)
        return {'movie_now':list_now,'movie_next':list_next}


    def close_connection(self):
        self.cur.close()
        self.conn.close()








