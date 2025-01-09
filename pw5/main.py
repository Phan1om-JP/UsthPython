#main.py
### Main Function
import curses
from input import InputHandler
from output import OutputHandler

def main(stdscr):
    input_handler = InputHandler()
    input_handler.load_from_dat()  # Load data if students.dat exists
    output_handler = OutputHandler(input_handler.students)
    output_handler.curses_menu(stdscr, input_handler)

if __name__ == "__main__":
    curses.wrapper(main)