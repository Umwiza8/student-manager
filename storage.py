import json 

def load_students():
    try:
        with open("student.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_students(students):
    with open ("student.json","w") as file:
        json.dump(students, file, indent=4)
