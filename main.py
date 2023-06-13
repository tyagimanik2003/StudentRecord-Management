from StudentInfo import StudentData
from MarksInfo import StudentMarks       
#main coding

Basic_Data=StudentData()
Student_Marks=StudentMarks()

print("To edit Student information: Press 1")
print("To edit Student Marks: Press 2")
print("To edit Student Attendance: Press 3")

#taking input
choice=int(input("Enter your choice:"))
if choice==1:
    print("To Delete a Student's Information: Press 1")
    print("To Display a single Student's Information: Press 2")
    print("To Display all the Student's Information: Press 3")
    print("To insert a Student's data: Press 4")
    print("To edit a Student's PhoneNumber_number: Press 5")
    input_1=int(input("Enter your choice: "))
    if input_1==1:
        x=int(input("Enter the Student_ID"))
        Basic_Data.Delete_user(x)
    elif input_1==2:
        x=int(input("Enter the Student_ID"))
        Basic_Data.Fetch_single(x)
    elif input_1==3:
        Basic_Data.Fetch_All()
    elif input_1==4:
        userid=int(input("Enter the Student id: "))
        StudentName=input("Enter the Name of the Student: ")
        PhoneNumber=int(input("Enter the PhoneNumber number of the Student: "))
        Basic_Data.insert_user(userid, StudentName, PhoneNumber)
    elif input_1==5:
        PhoneNumber=int(input())
        userid=int(input())
        Basic_Data.Edit_user_PhoneNumber(PhoneNumber, userid)
elif choice==2:
    
    print("To Insert marks of a Student: Press 1")
    print("To Show marks of a Student: Press 2")
    print("To Display Marks of all the Student's: Press 3")
    print("To Edit marks of a student: Press 4")
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