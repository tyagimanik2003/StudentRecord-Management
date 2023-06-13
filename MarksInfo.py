import mysql.connector as connector
class StudentMarks:
    def __init__(self):
        self.con=con=connector.connect(host='localhost',port='3306',user='root',password='8851039311',database='StudentRecord')

        
        query='create table if not exists academic_record(userId int primary key,StudentName varchar(200),PhoneNumber varchar(200));'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")

    #inserting data 
    def insert_user_marks(self,userid,Maths,Chemistry,Physics,English):
        query = "insert into academic_record(userID,Maths_marks,Chemistry_marks,Physics_marks,English_marks) values({},{},{},{},{})".format(userid,Maths,Chemistry,Physics,English)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db successfully")
    def display_user_marks(self):
        querry="select * from academic_record where userID={}".format(x)
        cur=self.con.cursor()
        cur.execute(querry)
        for row in cur:
            print("User ID: ",row[0])
            print("User Maths_marks: ",row[1])
            print("User Chemistry_marks: ",row[2])
            print("User Physics_marks: ",row[3])
            print("User English_marks: ",row[4])
    def Fetch_All(self):
        querry="select * from academic_record "
        cur=self.con.cursor()
        cur.execute(querry)
        for row in cur:
            print("User ID: ",row[0])
            print("User Maths_marks: ",row[1])
            print("User Chemistry_marks: ",row[2])
            print("User Physics_marks: ",row[3])
            print("User English_marks: ",row[4])
    def update_maths_marks(self,marks,userid):
        querry="Update academic_record set Maths_marks={} where userID={}".format(marks,userid)
        cur=self.con.cursor()
        cur.execute(querry)
        self.con.commit()
        print("Student Marks updated")
    def update_chemistry_marks(self,marks,userid):
        querry="Update academic_record set Chemistry_marks={} where userID={}".format(marks,userid)
        cur=self.con.cursor()
        cur.execute(querry)
        self.con.commit()
        print("Student Marks updated")
    def update_physics_marks(self,marks,userid):
        querry="Update academic_record set Physics_marks={} where userID={}".format(marks,userid)
        cur=self.con.cursor()
        cur.execute(querry)
        self.con.commit()
        print("Student Marks updated")
    def update_english_marks(self,marks,userid):
        querry="Update academic_record set English_marks={} where userID={}".format(marks,userid)
        cur=self.con.cursor()
        cur.execute(querry)
        self.con.commit()
        print("Student Marks updated")
# yoyo.insert_user_marks(1, 90, 90, 94, 95)