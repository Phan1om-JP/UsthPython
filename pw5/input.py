#input.py
### UI Class
import curses
import os
import pickle
import gzip
from domains.student import Student
class InputHandler:
    def __init__(self):
        self.students = []

    def add_student(self, screen):
        screen.clear()
        screen.addstr("---Add Student---\n")
        screen.addstr("Name: ")
        curses.echo()
        name = screen.getstr().decode("utf-8")
        screen.addstr("Student ID: ")
        student_id = screen.getstr().decode("utf-8")
        student = Student(name, student_id)
        self.add_marks(screen, student)
        self.students.append(student)
        
#Changing student input info to students.txt
        with open("students.txt", "a") as f:
            f.write(f"Name :{student.name}, ID : {student.student_id} \n")
        screen.addstr("\nStudent added! Press any key to continue...")
        screen.getch() #get a single key to do sth

    def add_marks(self, screen, student):
        while True:
            screen.clear()
            screen.addstr("---Add Marks---\n")
            screen.addstr("Subject (or '.' to finish): ")
            subject = screen.getstr().decode("utf-8")
            if subject == '.':
                break
            screen.addstr("Mark: ")
            mark = float(screen.getstr().decode("utf-8"))
            screen.addstr("Credit: ")
            credit = float(screen.getstr().decode("utf-8"))
            student.add_mark(subject, mark, credit)
#Changing course info to courses.txt
            with open("courses.txt", "a") as f:
                f.write(f"Subject: {subject}, Credit: {credit}\n")
#Changing mark input info to marks.txt
            with open("marks.txt", "a") as f:
                f.write(f"Student ID : {student.student_id}, Subject: {subject}, Mark : {mark}\n")
        screen.addstr("\nMarks added to the courses! Press any key to countinue ...")
        screen.getch()
        
    def save_to_dat(self):
        """Compress and save all student data into students.dat."""
        with gzip.open("students.dat", "wb") as f:
            pickle.dump(self.students, f)

    def load_from_dat(self):
        """Decompress and load all student data from students.dat."""
        if os.path.exists("students.dat"):
            with gzip.open("students.dat", "rb") as f:
                self.students = pickle.load(f)