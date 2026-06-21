'''
Main File to start the tasks
'''

#Add Student function
def add_student(studentid, name, email, phone, age):
    with open("students.txt", "a") as file:

        file.write(f"{studentid}, {name}, {email}, {phone}, {age}\n")
        print("New Record added successfully")

while True:
    print("1. Add Student")
    print("2. Edit Student")
    print("3. Delete Student")
    print("4. Students List")
    print("5. Student Details")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        sid     = str(input("Enter student id:"))
        name    = str(input("Enter name:"))
        email   = str(input("Enter email:"))
        phone   = int(input("Enter phone:"))
        age     = int(input("Enter age:"))

        #Add Student function call
        add_student(sid, name, email, phone, age)

        break

    elif choice == 2:
        print("Edit Student:")
        break

    elif choice == 3:
        print("Delete Student:")
        break

    elif choice == 4:
        print("Students List:")
        break
    
    elif choice == 5:
        print("Student Details:")
        break

    elif choice == 6:
        print("Wrong choice entered, Please enter the valid choice")
        exit


