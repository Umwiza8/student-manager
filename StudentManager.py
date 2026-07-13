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


students=load_students()

while True:
    print("\n1. Add SStudent")
    print("2. View Student")
    print("3. Search student")
    print("4.Update Student")
    print("5. Delete Student")
    print("6. Total of all Students")
    print("7. Exit")

    choice=input("Please Choose:")

    if choice=="1":
        name=input("Please enter your name: ")
        country=input("Please enter your country: ")
        age=int(input("Please enter your age: "))
        student={
            "Name":name,
            "Country":country,
            "Age": age
        }
        students.append(student)
        save_students()
        print("Student added successfully!")

    elif choice=="2":
        for student in students:
            print(f"Name: {student['Name']},"
                  f"Country: {student['Country']},"
                  f"Age: {student['Age']}")
    
    elif choice=="3":
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
    
    elif choice=="4":
        update_name=input("Enter name of the student to update: ")
        found= False

        for student in students:
            if student["Name"]== update_name:
                found=True
                print("Student found.Leave blank if u don't want to change a field.")

                new_name=input("New name: ")
                new_country= input("New country: ")
                new_age= input("New age: ")

                if new_name:
                    student["Name"]= new_name
                if new_country:
                    student["Country"]= new_country
                if new_age:
                    student["Age"]=int(new_age)

                save_students()
                print("Student updated successfully!")
        if not found:
            print("Student not found")
            


    elif choice=="5":
        delete_name=input("Please enter name of student you want to delete: ")
        found=False
        for student in students:
            if delete_name==student['Name']:
                found=True
                students.remove(student)
                save_students()
                print("Student deleted successfully!")
        if not found:
            print("Students not found")

    elif choice=="6":
        Total_students=len(students)
        print(f"The total of all students is: {Total_students}")

    elif choice=="7":
        break





