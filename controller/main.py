# https://www.pythontutorial.net/tkinter/tkinter-mvc/
# https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/
# https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
import app

APP_TITLE = "Turing Machine"


def main():
    application = app.App(APP_TITLE)
    application.mainloop()


if __name__ == '__main__':
    main()
