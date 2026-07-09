import tkinter as tk

from app.auth.current_user import CurrentUser


class LogsWindow:

    def __init__(self, root, db):

        self.window = tk.Toplevel(root)

        self.window.title("Логи")
        self.window.geometry("700x500")

        textbox = tk.Text(
            self.window,
            width=80,
            height=30
        )

        textbox.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

        logs = db.get_user_logs(CurrentUser.id)

        for command, response, created in logs:

            textbox.insert(
                "end",
                f"[{created}]\n"
                f"Команда: {command}\n"
                f"Ответ: {response}\n\n"
            )

        textbox.config(state="disabled")