
import mysql.connector
#con1=mysql.connector.connect(host="localhost",user="root",password="root")

class Database():
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",user="root",password="root",database="employee")
        self.cur=self.con.cursor()
        sql="""
        Create table if not exists employees(
            id integer primary key,
            name text,
            doj text,
            email text,
            gender text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    #insert function
    def insert(self,id,name,doj,email,gender,address):
        sql = "insert into employees (id,name,doj,email,gender,address) values (%s,%s,%s,%s,%s,%s)"
        user = (id,name,doj,email,gender,address)
        self.cur.execute(sql,user)
        self.con.commit()

    #Fetch all data from db

    def fetch(self):
        self.cur.execute("select * from employees")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    #delete a record in db
    def delete(self,id):
        sql = "delete from employees where id=%s"
        user = (id,)
        self.cur.execute(sql, user)
        self.con.commit()

    #update a record in db
    def update(self,id,name,doj,email,gender,address):
        sql = "update employees set name=%s,doj=%s,email=%s,gender=%s,address=%s where id = %s"
        user = (name, doj, email, gender, address,id)
        self.cur.execute(sql, user)
        self.con.commit()



#o = Database()
#o.delete("3")
#o.insert("3","fgham","12-09-2020","sam@gmail.com","male","cbe")
#o.fetch()
#o.update("2","samkumar","12-12-2020","samkumar@gmail.com","male","mdu")
