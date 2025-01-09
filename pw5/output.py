#output.py
import curses

class OutputHandler:
    def __init__(self, students):
        self.students = students
    def display_students(self, screen):
        screen.clear()
        screen.addstr("---Student List---\n")
        for student in self.students:
            screen.addstr(student.describe() + "\n")
        screen.addstr("\nPress any key to continue...")
        screen.getch()

    def sort_students_by_gpa(self, screen):
        self.students.sort(key=lambda student: student.calculate_gpa(), reverse=True)
        screen.clear()
        screen.addstr("Students sorted by GPA : \n")
        for student in self.students :
            screen.addstr(student.describe() + "\n")
        screen.addstr("\nPress any key to continue...")
        screen.getch()

    def curses_menu(self, screen, input_handler):
        curses.curs_set(1) #enable cursor
        curses.echo()   #enable user input
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
                input_handler.add_student(screen)
            elif choice == "2":
                self.display_students(screen)
            elif choice == "3":
                self.sort_students_by_gpa(screen)
                screen.addstr("Students sorted by GPA. Press any key to continue...")
                screen.getch()
            elif choice == "4":
                input_handler.save_to_dat() #save data to file
                break
            else:
                screen.addstr("Invalid choice! Press any key to continue...")
                screen.getch()
