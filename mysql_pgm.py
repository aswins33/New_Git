import pymysql

connection=pymysql.connect(user="root",password="1234",host="localhost",database="company")

cursor=connection.cursor()
def empSave():
    name=input("Enter employee name : ")
    salary=float(input("Enter employee salary : "))
    address=input("Enter employee address : ")
    cursor.execute(f'INSERT INTO EMPLOYEES (NAME, SALARY,ADDRESS) VALUES ("{name}", {salary},{"ADDRESS"});')
    connection.commit()

emp_count=int(input("How many employees you wish to add : "))
for k in range(1,emp_count+1):
    print(f"Employee {k}")
    empSave()


def empDelete():
    name=input("enter employee ID to delete :")
    cursor.execute(f'DELETE FROM EMPLOYEES WHERE ID ({ID});')
    connection.commit


while True:
    print("1. Add empoloyee")
    print("2. Delete employee")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        emp_count = int(input("How many employees you wish to add: "))
        for k in range(1,emp_count+1):
            print(f"Employee {k}")
            empSave()

    elif choice == 2:
        empDelete()

    else:
        print("invalid input")
