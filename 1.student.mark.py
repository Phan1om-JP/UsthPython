def input_students():
    students = [];
    num_students = int(input("How many student in this class ? : "))

    for _ in range(num_students) : 
        #id, name, dob
        student_id = input("Student ID : ")
        student_name = input("Name : ")
        student_dob = input("Date of birth : ")
        students.append({"ID" : student_id, "Name" : student_name, "Dob" : student_dob, "Courses":{}})
    return students
def input_courses(students): 
    for student in students: 
        print(f"\nAdding course for {student['Name']}(ID:{student['ID']})")
        while True:
            course_name = input("Course name('end' to finish) :").strip()
            if course_name.lower() == "end":
                break
            mark = float(input(f"Mark for {course_name}: "))
            #adding course and mark for student
            student["Courses"][course_name] = mark 
    return students

#int main(){}

students = input_students()
students = input_courses(students)

print("\nStudent Data:")
for student in students:
    print(f"ID: {student['ID']}, Name: {student['Name']}, Course: {student['Courses']}")
    
# Student Data:
# ID: 12, Name: scotus, Course: {'Algebra': 12.4}
# ID: 14, Name: jasper, Course: {'Algebra': 16.6}