import mysql.connector as connector

class StudentMarks:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='8851039311',database='StudentRecord')

        
        query='create table if not exists academic_record(RegistrationNumber int primary key,Maths_marks int,Chemistry_marks int,Physics_marks int,English_marks int);'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
    
    def Execute(self,query):
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    #inserting data 
    def insert_user_marks(self,RegistrationNumber,Maths,Chemistry,Physics,English):
        query = "insert into academic_record(RegistrationNumber,Maths_marks,Chemistry_marks,Physics_marks,English_marks) values({},{},{},{},{})".format(RegistrationNumber,Maths,Chemistry,Physics,English)
        self.Execute(query)
        print("Student Marks saved to Database successfully")

    def display_user_marks(self,RegistrationNumber):
        querry="select * from academic_record where RegistrationNumber={}".format(RegistrationNumber)
        cur=self.con.cursor()
        cur.execute(querry)
        for row in cur:
            print("RegistrationNumber: ",row[0])
            print("Maths_Marks: ",row[1])
            print("Chemistry_Marks: ",row[2])
            print("Physics_Marks: ",row[3])
            print("English_Marks: ",row[4])

    def Fetch_All(self):
        query = "SELECT * FROM academic_record"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

        headers = ["RegistrationNumber", "Maths_marks", "Chemistry_marks", "Physics_marks", "English_marks"]
        table_data = []
        for row in rows:
            table_data.append(row)

        print(tabulate(table_data, headers, tablefmt="grid"))

    def update_MathsMarks(self,RegistrationNumber,marks):
        query="Update academic_record set Maths_marks={} where RegistrationNumber={}".format(marks,RegistrationNumber)
        self.Execute(query)
        print("Student Marks updated")

    def update_ChemistryMarks(self,RegistrationNumber,marks):
        query="Update academic_record set Chemistry_marks={} where RegistrationNumber={}".format(marks,RegistrationNumber)
        self.Execute(query)
        print("Student Marks updated")

    def update_PhysicsMarks(self,RegistrationNumber,marks):
        query="Update academic_record set Physics_marks={} where RegistrationNumber={}".format(marks,RegistrationNumber)
        self.Execute(query)
        print("Student Marks updated")

    def update_EnglishMarks(self,RegistrationNumber,marks):
        query="Update academic_record set English_marks={} where RegistrationNumber={}".format(marks,RegistrationNumber)
        self.Execute(query)
        print("Student Marks updated")