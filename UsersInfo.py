import mysql.connector as connector
class StudentData:
    def __init__(self):
        self.con=con=connector.connect(host='localhost',port='3306',user='root',password='8851039311',database='StudentRecord')

        
        query='create table if not exists StudentTable(RegistrationNumber INT AUTO_INCREMENT PRIMARY KEY,SudentName varchar(200),PhoneNumber varchar(200));'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")

    def Execute(self,query):
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    #inserting data 
    def insert_user(self,StudentName,PhoneNumber):
        query1 = "insert into StudentTable(StudentName,PhoneNumber) values('{}','{}')".format(StudentName,PhoneNumber)
        self.Execute(query1)
        print("Student Details saved to Database successfully")
        query2 = "SELECT LAST_INSERT_ID() AS RegistrationNumber"
        cur = self.Execute(query2)
        result = cur.fetchone()
        RegistrationNumber = result['RegistrationNumber']
        query3=" insert into AcademicRecord(RegistrationNumber)Values({})".format(RegistrationNumber)
        query4=" insert into AttendanceRecord(RegistrationNumber)Values({})".format(RegistrationNumber)
        self.Execute(query3)
        self.Execute(query4)
    #fetch all
    def Fetch_All(self):
        querry="select * from user "
        cur=self.con.cursor()
        cur.execute(querry)
        for row in cur:
            print("Registration Number: ",row[0])
            print("Student Name: ",row[1])
            print("Studen PhoneNumber Number: ",row[2])
    def Fetch_single(self,userid):
        querry="select * from user where RegistrationNumber={}".format(userid)
        cur=self.con.cursor()
        cur.execute(querry)
        for row in cur:
            print("Registration Number: ",row[0])
            print("Student Name: ",row[1])
            print("Studen PhoneNumber Number: ",row[2])

    def Delete_user(self,userid):
        querry="delete from user where RegistrationNumber={}".format(userid)
        cur=self.con.cursor()
        cur.execute(querry)
        self.con.commit()
        print("User deleted successfully")
    def Edit_user_PhoneNumber(self,PhoneNumber,userid):
        querry="update user set PhoneNumber={} where RegistrationNumber={}".format(PhoneNumber,userid)
        cur=self.con.cursor()
        cur.execute(querry)
        self.con.commit()
        print("User info updated successfully")