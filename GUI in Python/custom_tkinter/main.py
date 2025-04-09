import customtkinter as ctk

# Create a window (it inherits from the tkinter window, so I have all
# the default arguments)
window = ctk.CTk()
window.geometry('600x400')
window.title('MyApp')

# Create widgets
label = ctk.CTkLabel(window, text='A ctk label')
label.pack()


def main() -> None:
    window.mainloop()


if __name__ == '__main__':
    main()
