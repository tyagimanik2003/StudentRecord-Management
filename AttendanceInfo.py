import mysql.connector as connector

class StudentAttendance:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='8851039311',database='StudentRecord')

        
        query='create table if not exists attendance_record(RegistrationNumber int primary key,Present int,Absent int);'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
        
    def Execute(self,query):
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
