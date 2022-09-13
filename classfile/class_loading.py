import pandas as pd
import sqlite3

class class_loading:
    def __init__(self):
        print("Creating Connection with sqlite db")
        self.conn = sqlite3.connect(":memory:")
        self.cur = self.conn.cursor()
        self.sql="Create table if not exists password_check(password text NOT NULL,strength text NOT NULL)"
        self.cur.execute(self.sql) 
        self.passwords = [("Password", "Medium"),("calvin", "Poor"),("Password@123", "Strong"),("123", "Poor"),("@##@@", "Poor")]
        self.insertsql = ''' INSERT INTO password_check(password,strength)  VALUES(?,?) '''
        self.cur.executemany(self.insertsql,self.passwords)
        self.conn.commit()
    def run(self):
        print("Loading the data ")
        self.selectsql='select  password,strength from password_check'
        df = pd.read_sql_query("select  password,strength from password_check", self.conn)
        #print(df)
        return df
    def __del__(self):
        print("Closing  connection for sqlite db")
        self.conn.close()
