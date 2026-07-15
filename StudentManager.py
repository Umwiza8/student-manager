from storage import load_students
from operations import (
    display_menu,
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    get_total_students
)
students=load_students()
print(students)
while True:
    display_menu()
    choice=input("Please Choose:")
    if choice=="1":
        add_student(students)
    elif choice=="2":
        view_students(students)
    elif choice=="3":
        search_student(students)
    elif choice=="4":
        update_student(students)
    elif choice=="5":
        delete_student(students)
    elif choice=="6":
        total=get_total_students(students)
        print(total)
    elif choice=="7":
        break
    else:
        print("Invalid option. Please choose between 1 and 7.")
    
