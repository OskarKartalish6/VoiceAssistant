import customtkinter as ctk


class MessageWindow(ctk.CTkToplevel):

    def __init__(self, root, title, message):
        super().__init__(root)

        self.title(title)
        self.geometry("320x150")
        self.resizable(False, False)

        ctk.CTkLabel(
            self,
            text=message,
            wraplength=280
        ).pack(pady=20)

        ctk.CTkButton(
            self,
            text="OK",
            command=self.destroy
        ).pack(pady=10)