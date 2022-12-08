import pymysql

class connectDB():
    def __init__(self, user, password):
        self.con = pymysql.connect(
            host="localhost", 
            user=user, 
            password=password, 
            db="crawling", 
            charset="utf8"
        )
        self.cur = self.con.cursor()


    def insert_sql(self, tablename, col, data): 
        query = f"INSERT INTO {tablename} ({col}) VALUES ('{data}');"
        self.cur.execute(query)
        self.con.commit()
    
    def insert_many_sql(self, query, lis):
        self.cur.executemany(query, lis)
        self.con.commit()
    
    def select_sql(self, a):
        query = a
        self.cur.execute(query)
        resDb = self.cur.fetchall()
        return resDb

    def update_sql(self, tablename, col, data):
        query = f"INSERT {tablename} SET ({col}) WHERE ('{data}');"
        self.cur.execute(query)
        self.con.commit()

    def close_db(self):
        self.con.close()
