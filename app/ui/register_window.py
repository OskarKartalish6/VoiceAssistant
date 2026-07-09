import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from app.ui.messege_window import MessageWindow

class RegisterWindow:

    def __init__(self, root, auth):

        self.auth = auth

        self.window = ctk.CTkToplevel(root)
        self.window.title("Регистрация")
        self.window.geometry("350x280")
        self.window.resizable(False, False)


        ctk.CTkLabel(
            self.window,
            text="Имя пользователя",
            font=("Arial", 16)
        ).pack(pady=(20, 5))

        self.username = ctk.CTkEntry(
            self.window,
            width=220,
            placeholder_text="Введите имя"
        )
        self.username.pack()

        ctk.CTkLabel(
            self.window,
            text="Пароль",
            font=("Arial", 16)
        ).pack(pady=(20, 5))

        self.password = ctk.CTkEntry(
            self.window,
            width=220,
            show="*",
            placeholder_text="Введите пароль"
        )
        self.password.pack()

        ctk.CTkButton(
            self.window,
            text="Создать аккаунт",
            command=self.register
        ).pack(pady=25)

    def register(self):
        username = self.username.get().strip()
        password = self.password.get()

        self.window.grab_set()

        if not username or not password.strip():
            MessageWindow(
                self.window,
                "Ошибка",
                "Все поля должны быть заполнены!"
            )
            return
        result = self.auth.register(username, password)
        print(result)

        if "успешно" in result.lower():
            CTkMessagebox(
                title="Успешно",
                message=result,
                icon="check"
            )
            self.window.destroy()
            return

        MessageWindow(
            self.window,
            "Ошибка",
            result
        )