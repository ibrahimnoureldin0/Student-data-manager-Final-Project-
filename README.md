# Student-data-manager-Final-Project-
# Student Management System

This is a simple Python program that lets you manage student records. You can add, delete, and view students using a menu.

## What It Does

1. **Add a Student**:  
   - You can add a student by entering their name, age, and department.  
   - The program gives each student a unique ID automatically.

2. **Delete a Student**:  
   - You can delete a student by entering their ID.  
   - If the student is found, they are removed. If not, it tells you the student doesn't exist.

3. **View All Students**:  
   - Shows a list of all students with their details (name, age, department, and ID).  
   - If no students are added, it says the list is empty.

4. **Exit**:  
   - Stops the program.

## How to Use

1. Run the program.
2. A menu will appear with these options:
   - **1**: Add a student.
   - **2**: Delete a student.
   - **3**: View all students.
   - **4**: Exit the program.
3. Follow the instructions on the screen to add, delete, or view students.

## Example

```plaintext
1. Add Student
2. Delete Student
3. View All Students
4. Exit
Enter your choice: 1
Enter name: Omer
Enter age: 21
Enter department: Computer Engineering
==================================================
Student added successfully
==================================================
```

## Notes

- The program doesn’t save data. If you close it, all student records will be lost.
- Student IDs start at 1 and increase automatically for each new student.
