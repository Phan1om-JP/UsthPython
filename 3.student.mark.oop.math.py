# • Use math module to round-down student scores to 1-digit
# decimal upon input, floor()
# • Add function to calculate average GPA for a given student (use numpy)
#     Weighted sum of credits and marks
#     Sort student list by GPA descending
# • Decorate your UI with curses module

# import packages
# create class Student (client_info, marks(round down to 1 digit)) class UI (info, list, gpa, sort gpa)
# create function to calculate average GPA (mark * credit)/number of subject included
# create function to sort student list by GPA descending

import curses # Menu 
import math
import numpy as np

#domain/student.py
### Student Class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.marks = {}  # {subject: (mark, credit)}

    def add_mark(self, subject, mark, credit):
        rounded_mark = math.floor(mark * 10) / 10  #12.32 -> 123.2 -> 123 -> 12.3
        self.marks[subject] = (rounded_mark, credit)

    def calculate_gpa(self):
        if not self.marks:
            return 0
        marks = np.array([mark for mark, _ in self.marks.values()])
        credits = np.array([credit for _, credit in self.marks.values()])
        return np.sum(marks * credits) / np.sum(credits)

    def describe(self):
        return f"{self.name} (ID: {self.student_id}) - GPA: {self.calculate_gpa():.2f}"
#input.py
### UI Class
class UI:
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
#output.py
    def display_students(self, screen):
        screen.clear()
        screen.addstr("---Student List---\n")
        for student in self.students:
            screen.addstr(student.describe() + "\n")
        screen.addstr("\nPress any key to continue...")
        screen.getch()

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.calculate_gpa(), reverse=True) #lambda takes a single student in students list and reverse to change the default sort(asc) to desc

    def curses_menu(self, screen):
        curses.curs_set(1)
        curses.echo()
        screen.keypad(True) #enable keypad (up, down, left, right)

        while True:
            screen.clear()
            screen.addstr("---Menu---\n")
            screen.addstr("1. Add Student\n")
            screen.addstr("2. Display Students\n")
            screen.addstr("3. Sort Students by GPA\n")
            screen.addstr("4. Exit\n")
            screen.addstr("Choice: ")
            choice = screen.getstr().decode("utf-8")

            if choice == "1":
                self.add_student(screen)
            elif choice == "2":
                self.display_students(screen)
            elif choice == "3":
                self.sort_students_by_gpa()
                screen.addstr("Students sorted by GPA. Press any key to continue...")
                screen.getch()
            elif choice == "4":
                break
            else:
                screen.addstr("Invalid choice! Press any key to continue...")
                screen.getch()
#main.py
### Main Function
def main(stdscr):
    ui = UI()
    ui.curses_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)