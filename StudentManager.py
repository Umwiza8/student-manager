import json 

def load_students():
    try:
        with open("student.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_students():
    with open ("student.json","w") as file:
        json.dump(students, file, indent=4)

def display_menu():
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Search student")
    print("4.Update Student")
    print("5. Delete Student")
    print("6. Total of all Students")
    print("7. Exit")

def add_student():
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
    save_students()
    print("Student added successfully!")    
    
def view_students():
     if not students:
         print("No students available")
         return
     for student in students:
            print(f"Name: {student['Name']},"
                  f"Country: {student['Country']},"
                  f"Age: {student['Age']}")

def search_student():
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

def update_student():
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
            save_students()
            print("Student updated successfully!")
    if not found:
        print("Student not found")

def delete_student():
    delete_name=input("Please enter name of student you want to delete: ")
    found=False
    for student in students:
        if delete_name==student['Name']:
            found=True
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return
    if not found:
         print("Students not found")

def get_total_students():
    return len(students)
                
students=load_students()
while True:
    display_menu()
    choice=input("Please Choose:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        update_student()
    elif choice=="5":
        delete_student()
    elif choice=="6":
        total=get_total_students()
        print(total)
    elif choice=="7":
        break
    else:
        print("Invalid option. Please choose between 1 and 7.")
    
