import customtkinter as ctk


class BaseWindow:

    def __init__(self, title: str, width=450, height=350):

        self.window = ctk.CTk()

        self.window.title(title)

        self.window.geometry(f"{width}x{height}")

        self.window.resizable(False, False)

    def show(self):
        self.window.mainloop()