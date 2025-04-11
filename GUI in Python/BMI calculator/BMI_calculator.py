import customtkinter as ctk
from settings import *

try:
    from ctypes import windll, byref, sizeof, c_int
except Exception as e:
    print(e)


class App(ctk.CTk):
    def __init__(self):

        # Window setup
        super().__init__(fg_color=GREEN)
        self.title('')
        self.geometry('400x400')
        self.resizable(False, False)
        self.change_title_bar_color()

    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(HWND,
                                                DWMWA_ATTRIBUTE,
                                                byref(c_int(COLOR)),
                                                sizeof(c_int))
        except Exception as e:
            print(f"Does not work: {e}")


app = App()


def main() -> None:
    app.mainloop()


if __name__ == '__main__':
    main()

