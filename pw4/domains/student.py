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
