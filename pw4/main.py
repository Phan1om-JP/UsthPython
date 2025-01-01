#main.py
### Main Function
def main(stdscr):
    ui = UI()
    ui.curses_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)