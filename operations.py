from storage import save_students
def display_menu():
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Search student")
    print("4.Update Student")
    print("5. Delete Student")
    print("6. Total of all Students")
    print("7. Exit")

def add_student(students):
    name=input("Please enter your name: ")
    country=input("Please enter your country: ")
    try:
        age=int(input("Please enter your age: "))
    except ValueError:
        print("Put in a valid number") 
        return   
    student={
            "Name":name,
            "Country":country,
            "Age": age
            }
    students.append(student)
    save_students(students)
    print("Student added successfully!")    
    
def view_students(students):
     if not students:
         print("No students available")
         return
     for student in students:
            print(f"Name: {student['Name']},"
                  f"Country: {student['Country']},"
                  f"Age: {student['Age']}")

def search_student(students):
    search_name=input("Please enter name of student you are looking for: ")
    found=False
    for student in students:
        if search_name==student['Name']:
            found=True
            print(f"Name: {student['Name']},"
                  f"Country: {student['Country']},"
                  f"Age: {student['Age']}")
    if not found:
         print("student not found")

def update_student(students):
    update_name=input("Enter name of the student to update: ")
    found= False

    for student in students:
        if student["Name"]== update_name:
            found=True
            print("Student found.Leave blank if u don't want to change a field.")
            new_name=input("New name: ")
            new_country= input("New country: ")
            new_age=input("New age: ")
            if new_name:
              student["Name"]= new_name
            if new_country:
              student["Country"]= new_country
            if new_age:
                try:
                    student["Age"]=int(new_age)
                except ValueError:
                    print("Enter a valid number")
                    return
            save_students(students)
            print("Student updated successfully!")
    if not found:
        print("Student not found")

def delete_student(students):
    delete_name=input("Please enter name of student you want to delete: ")
    found=False
    for student in students:
        if delete_name==student['Name']:
            found=True
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return
    if not found:
         print("Students not found")

def get_total_students(students):
    return len(students)