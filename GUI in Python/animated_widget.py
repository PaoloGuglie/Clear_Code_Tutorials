import customtkinter as ctk
from random import choice


def move_button():
    global button_x
    button_x += 0.004
    sidebar_toggle_button.place(relx=button_x,
                                rely=0.5,
                                anchor='center')

    if button_x < 0.9:
        window.after(10, move_button)


# Window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')

# Sidebar toggle button
button_x = 0.5
sidebar_toggle_button = ctk.CTkButton(window,
                                      text='toggle sidebar',
                                      command=move_button)

sidebar_toggle_button.place(relx=button_x,
                            rely=0.5,
                            anchor='center')


def main() -> None:
    window.mainloop()


if __name__ == '__main__':
    main()
