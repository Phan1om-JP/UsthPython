students = []
course = []
marks = {}

def nums_std():
    num_std = int(input("Number of student: "))
    for _ in range(num_std):
        std_name = input("Student name: ")
        std_id = input("Student id: ")
        std_DoB = input("Date of Birth: ")
        std.append((std_name, std_id, std_DoB))
    print(f"{num_std} students added!")

def nums_cours():
    num_cours = int(input("Numbr of courses: "))
    for _ in range(num_cours):
        cour_name = input("Course name: ")
        cour_id = input("Course id: ")
        cours.append((cour_name, cour_id))
        marks[cour_id] = {}
    print(f"{cour_name} cours added!")

def marks():
    cours_id = input("Course id: ")
    if cours_id not in [course[0] for cour in cours]:
        print("Course not found!")
        return
    for std_name, std_id, _ in students

