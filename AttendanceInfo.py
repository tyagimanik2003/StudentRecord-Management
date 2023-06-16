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
        query1="Select Present from attendance_record where RegistrationNumber={}".format(RegistrationNumber)
        cur=self.con.cursor()
        present=cur.execute(query)+value
        
        query2="Update attendance_record set Present ={} where RegistrationNumber={}".format(Present,RegistrationNumber)
        self.Execute(query2)
    def Mark_absent(self,RegistrationNumber,value):
        query1="Select Absent from attendance_record where RegistrationNumber={}".format(RegistrationNumber)
        cur=self.con.cursor()
        Absent=cur.execute(query)+value
        
        query2="Update attendance_record set Absent ={} where RegistrationNumber={}".format(Absent,RegistrationNumber)
        self.Execute(query2)
        
