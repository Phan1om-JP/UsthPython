# create a class of Student(name, id, dob) 
# display it to add the values
# add marks (subject, condition to exit, invalid input)
# display all of them with marks

class Student :
    def __init__(self, name, student_id, dob):
        self.name = name
        self.student_id = student_id
        self.dob = dob
        self.marks = {} # Make it empty to add it latter
    # def describe(self) :
    #     print(f"Name: {self.name}")
    #     print(f"ID:  {self.student_id}")
    #     print(f"Dob: {self.dob}")
    def score(self) :
        print("\n Enter mark for subject (. to exit at adding Subject state) : ")
        while True :
            subject = input("Subject: ")
            if subject.lower() == '.':
                break
            try : 
                mark = float(input(f"Enter marks for {subject}: "))
                self.marks[subject] = mark
            except ValueError :
                print("Enter invalid marks")
    def full_describe(self) :
        print("\n--- Student Information ---")
        print(f"Name: {self.name}")
        print(f"ID:  {self.student_id}")
        print(f"Dob: {self.dob}")
        print(" --- MARKS --- ")
        for subject, mark in self.marks.items() :
            print(f"{subject} : {mark}")

print("Student information")
name = input("Name : ")
student_id = input("ID : ")
dob = input("Date of Birth : ")
print("Student Information")
student = Student(name, student_id, dob)
# student.describe()
student.score()
student.full_describe()

