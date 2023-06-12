import mysql.connector as connector
class UserData:
    def __init__(self):
        self.con=con=connector.connect(host='localhost',port='3306',user='root',password='8851039311',database='muj')

        
        query='create table if not exists user(Reg_no int primary key,userName varchar(200),phone varchar(200));'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
    
    #inserting data 
    def insert_user(self,userid,userName,phone):
        query1 = "insert into user(Reg_no,userName,phone) values({},'{}','{}')".format(userid,userName,phone)
        print(query1)
        cur=self.con.cursor()
        cur.execute(query1)
        self.con.commit()
        print("user saved to db successfully")
        query2=" insert into academic_record(Reg_no)Values({})".format(userid)
        query3=" insert into attendance_record(Reg_no)Values({})".format(userid)
        cur=self.con.cursor()
        cur.execute(query2)
        self.con.commit()
        cur=self.con.cursor()
        cur.execute(query3)
        self.con.commit()
    #fetch all
    def Fetch_All(self):
        querry="select * from user "
        cur=self.con.cursor()
        cur.execute(querry)
        for row in cur:
            print("Registration Number: ",row[0])
            print("Student Name: ",row[1])
            print("Studen Phone Number: ",row[2])
    def Fetch_single(self,userid):
        querry="select * from user where Reg_no={}".format(userid)
        cur=self.con.cursor()
        cur.execute(querry)
        for row in cur:
            print("Registration Number: ",row[0])
            print("Student Name: ",row[1])
            print("Studen Phone Number: ",row[2])

    def Delete_user(self,userid):
        querry="delete from user where Reg_no={}".format(userid)
        cur=self.con.cursor()
        cur.execute(querry)
        self.con.commit()
        print("User deleted successfully")
    def Edit_user_Phone(self,phone,userid):
        querry="update user set phone={} where Reg_no={}".format(phone,userid)
        cur=self.con.cursor()
        cur.execute(querry)
        self.con.commit()
        print("User info updated successfully")