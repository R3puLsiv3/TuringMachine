# https://www.pythontutorial.net/tkinter/tkinter-mvc/
# https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/
import app

APP_TITLE = "Turing Machine"


def main():
    application = app.App(APP_TITLE)
    application.mainloop()

if __name__ == '__main__':
    main()
