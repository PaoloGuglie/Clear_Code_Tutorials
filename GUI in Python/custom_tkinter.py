import customtkinter as ctk


def change_theme():
    global CURRENT_THEME

    # Toggle theme
    CURRENT_THEME = "dark" if CURRENT_THEME == "light" else "light"
    ctk.set_appearance_mode(CURRENT_THEME)


# Create a window (it inherits from the tkinter window, so I have all
# the default arguments)
window = ctk.CTk()
window.geometry('600x400')
window.title('MyApp')

# Set initial theme
CURRENT_THEME = "dark"
ctk.set_appearance_mode(CURRENT_THEME)

# Create widgets
label = ctk.CTkLabel(window,
                     text='A ctk label',
                     fg_color=('black', 'white'),
                     text_color=('white', 'black'))
label.pack(pady=20)

button = ctk.CTkButton(window,
                       text='change theme',
                       fg_color=('black', 'white'),
                       text_color=('white', 'black'),
                       hover_color='yellowgreen',
                       command=change_theme)
button.pack()


def main() -> None:
    window.mainloop()


if __name__ == '__main__':
    main()
