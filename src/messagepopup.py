import tkinter as tk
import customtkinter as ctk

def ActionToDo(Action:str) -> str:
    def PassTest(value):
        nonlocal result
        result = value
        window.destroy()

    def FailTest(value):
        nonlocal result
        result = value
        window.destroy()

    result = None

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    window = ctk.CTk()
    window.title("Pass or Fail")
    window.geometry("350x100")

    label = ctk.CTkLabel(window, text=Action, font=("Lato", 13, "bold"))
    label.pack()

    button_pass = ctk.CTkButton(window, text="Pass", command=lambda: PassTest("PASS"))
    button_fail = ctk.CTkButton(window, text="Fail", command=lambda: FailTest("FAIL"))
    button_pass.place(relx=0.28, rely=0.75, anchor=tk.CENTER)
    button_fail.place(relx=0.72, rely=0.75, anchor=tk.CENTER)

    window.mainloop()

    return result

print(ActionToDo("Verify Led19 (HandWash) Turn ON"))