#output.py
    def display_students(self, screen):
        screen.clear()
        screen.addstr("---Student List---\n")
        for student in self.students:
            screen.addstr(student.describe() + "\n")
        screen.addstr("\nPress any key to continue...")
        screen.getch()

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.calculate_gpa(), reverse=True)

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
