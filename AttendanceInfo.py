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
    def Mark_present(self,RegistrationNumber,value):
        query1 = "SELECT Present FROM attendance_record WHERE RegistrationNumber = {}".format(RegistrationNumber)
        cur = self.con.cursor()
        cur.execute(query1)
        present = cur.fetchone()[0] + value

        query2 = "UPDATE attendance_record SET Present = {} WHERE RegistrationNumber = {}".format(present, RegistrationNumber)
        self.Execute(query2)

    def Mark_absent(self,RegistrationNumber,value):
        query1 = "SELECT Absent FROM attendance_record WHERE RegistrationNumber = {}".format(RegistrationNumber)
        cur = self.con.cursor()
        cur.execute(query1)
        absent = cur.fetchone()[0] + value
    
        query2 = "UPDATE attendance_record SET Absent = {} WHERE RegistrationNumber = {}".format(absent, RegistrationNumber)
        self.Execute(query2)

        
