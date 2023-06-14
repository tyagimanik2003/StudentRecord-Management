from StudentInfo import StudentData
from MarksInfo import StudentMarks   
import tabulate    
#main coding


Basic_Data=StudentData()
Student_Marks=StudentMarks()

def Level1():

    print("To edit Student information: Press 1")
    print("To edit Student Marks: Press 2")
    print("To edit Student Attendance: Press 3")
    print("Exit: Press 6")

def Level2():
    print("To Delete a Student's Information: Press 1")
    print("To Display a Student's Information: Press 2")
    print("To Display all the Student's Information: Press 3")
    print("To insert a Student's data: Press 4")
    print("To edit a Student's Information: Press 5")
    print("Exit: Press 6")

def Level3():
    print("To Show marks of a Student: Press 2")
    print("To Display Marks of all the Student's: Press 3")
    print("To Edit marks of a student: Press 4")
    print("Exit: Press 6")
 
choice=0
Level1

while choice!=6:
    Level1
    choice=int(input("Enter your choice:"))
    if choice==1:
        input_1=0
        Level2()

        while input_1!=6:
            input_1=int(input("Enter your choice: "))
            if input_1==1:
                RegistrationNumber=int(input("Enter the Student RegistrationNumber"))
                Basic_Data.Delete_user(RegistrationNumber)
            elif input_1==2:
                RegistrationNumber=int(input("Enter the Student RegistrationNumber"))
                Basic_Data.Fetch_single(RegistrationNumber)
            elif input_1==3:
                Basic_Data.Fetch_All()
            elif input_1==4:
                while input_1!= 6:
                    RegistrationNumber=int(input("Enter the Student RegistrationNumber: "))
                    StudentName=input("Enter the Name of the Student: ")
                    PhoneNumber=int(input("Enter the PhoneNumber number of the Student: "))
                    Basic_Data.insert_user(RegistrationNumber, StudentName, PhoneNumber)
            elif input_1==5:
                PhoneNumber=int(input())
                userid=int(input())
                Basic_Data.Edit_user_PhoneNumber(PhoneNumber, userid)
        
    elif choice==2:
        input_2=0
        Level3
        while input_2!=6:
            input_2=int(input("Enter your choice: "))
            if input_2==1:
                Student_ID=int(input("Enter the Student_ID: "))
                Maths=int(input("Enter the Maths Marks: "))
                Chemistry=int(input("Enter the Chemistry Marks: "))
                Physics=int(input("Enter the Physics Marks: "))
                English=int(input("Enter the English Marks: "))
                Student_Marks.insert_user_marks(Student_ID, Maths, Chemistry, Physics, English)

            elif input_2==2:
                x=int(input("Enter the User_ID"))
                Student_Marks.display_user_marks(x)
            elif input_2==3:
                Student_Marks.Fetch_All()
            elif input_2==4:
                input_3=int(input("Enter the StudentID: "))
                print()
                print("Maths Marks: Press 1")
                print("Chemistry Marks: Press 2")
                print("Physics Marks: Press 3")
                print("English Marks: Press 4")
                print()
                input_4=int(input("Enter the Choice: "))
                input_5=int(input("Enter the Marks: "))
                if input_4==1:
                    Student_Marks.update_maths_marks(input_5, input_3)
                elif input_4==2:
                    Student_Marks.update_chemistry_marks(input_5, input_3)
                elif input_4==3:
                    Student_Marks.update_physics_marks(input_5, input_3)
                elif input_4==4:
                    Student_Marks.update_english_marks(input_5, input_3)


        # userid=int(input("Enter the user id: "))
        # StudentName=input("Enter the Name of the user: ")
        # PhoneNumber=int(input("Enter the PhoneNumber number of the user: "))
        # Basic_Data.insert_user(userid, StudentName, PhoneNumber)