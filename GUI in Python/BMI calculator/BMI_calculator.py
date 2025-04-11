import customtkinter as ctk
from settings import *


class App(ctk.CTk):
    def __init__(self):

        # Window setup
        super().__init__(fg_color=GREEN)
        self.title('')
        self.geometry('400x400')
        self.resizable(False, False)


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()

