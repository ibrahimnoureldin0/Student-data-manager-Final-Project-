students = []

def add(id):
    name = str(input("Enter name: "))
    age = int(input("Enter age: "))
    department = str(input("Enter department: "))
    student = (name, age, department, id)
    students.append(student)
    print("="*50)
    print("Student added successfully")
    print("="*50)

def delete():
    id = int(input("Enter ID of student to be deleted: "))
    student_index = 0 # Track index of tuple to delete it
    for student in students:
        if id == student[3]:
            del students[student_index]
            print("="*50)
            print("Student deleted successfully")
            print("="*50)
            break
        
        if student_index == len(students)-1: # Check if we are at the end of the list
            print("="*50)
            print("Student is not found")
            print("="*50)
            break

        student_index+=1

def view():
    if students == []: # Check if the list has no values
        print("="*50)
        print("No students in the list")
        print("="*50)
    else:
        for student in students:
            print("Name:", student[0])
            print("Age:", student[1])
            print("Department:", student[2])
            print("ID:", student[3])
            print("="*50)


id = 1 # Initial ID for the first student

while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. View All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add(id)
        id += 1 # Increment Id for the next student
    elif choice == '2':
        delete()
    elif choice == '3':
        view()
    elif choice == '4':
        break
    else:
        print("="*50)
        print("Try option from 1 to 4")
        print("="*50)
