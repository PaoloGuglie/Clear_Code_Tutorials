import customtkinter as ctk

# Window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')

# Button
button_x = 0.5
button = ctk.CTkButton(window, text = 'toggle sidebar')
button.place(relx=button_x, rely=0.5, anchor='center')


def main() -> None:
    window.mainloop()


if __name__ == '__main__':
    main()
