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
