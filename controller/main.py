from model import Model
from view import View
from controller import Controller

# https://www.pythontutorial.net/tkinter/tkinter-mvc/
# https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/
# https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()


if __name__ == '__main__':
    main()
