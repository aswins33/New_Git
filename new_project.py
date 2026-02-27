students={}

def add_students():
    students_id=int(input("enter student id: "))
    students_name=input("enter student name: ")
    students_age=int(input("enter student age: "))

    marks={}

    all_subject=int(input("number of subject: "))
    for i in range(all_subject):
        subject_name=input("enter subject name: ")
        subject_mark=int(input("enter your mark:" ))
        marks[subject_name]=subject_mark

    details={}
    details["name"]=students_name
    details["age"]=students_age
    details["marks"]=marks

    students[students_id]=details

    print(students)

add_students()

def remove_student():
    std_id=int(input("enter the student id which is to be remove: "))
    students.pop(std_id)
    print("remove successfully")
while True:
    print("1. Add student")
    print("2. view all student")
    print("3. delete student")
    print("4. exit")

    choice=int(input("enter your choice 1/2/3/4: "))
    if choice==1:
        add_students()
    elif choice==2:
        print(students)
    elif choice==3:
        remove_student()
    elif choice==4:
        print("exiting")
        break