import customtkinter as ctk
from random import choice


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # General attributes
        self.start_pos = start_pos + 0.01
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)

        # Animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # Layout
        self.place(relx=self.start_pos,
                   rely=0.05,
                   relwidth=self.width,
                   relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos,
                       rely=0.05,
                       relwidth=self.width,
                       relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos,
                       rely=0.05,
                       relwidth=self.width,
                       relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True


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

# Animated widged (frame)
animated_panel = SlidePanel(window, 0, -0.3)
ctk.CTkLabel(animated_panel, text='Label 1').pack(expand=True, fill='both', padx=2, pady=10)
ctk.CTkTextbox(animated_panel).pack(expand=True, fill='both', pady=10)

# Sidebar toggle button
button_x = 0.5
sidebar_toggle_button = ctk.CTkButton(window,
                                      text='toggle sidebar',
                                      command=animated_panel.animate)

sidebar_toggle_button.place(relx=button_x,
                            rely=0.5,
                            anchor='center')


def main() -> None:
    window.mainloop()


if __name__ == '__main__':
    main()
