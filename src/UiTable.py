from tkinter import *
import customtkinter as ctk

def TableResults(lst):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    
    class Table:
        def __init__(self, root):
            for i in range(total_rows):
                for j in range(total_columns):
                    if lst[i][j] in ["Date",'Time','Action',"ERD", "Expected Data", "Data", "Data to Write", "Result", "Expected vs Data"]:
                        self.Entry = ctk.CTkEntry(root, width=214, height=23, corner_radius=2,
                                    font=('Lato',13, "bold"), bg_color="black", fg_color="#1E1E1E",
                                    border_color="#3E3E3E", border_width=1, text_color="white", justify="center")
                    elif lst[i][j] == "PASS":
                        self.Entry = ctk.CTkEntry(root, width=214, height=23, corner_radius=2,
                                    font=('Lato',13,'bold'), bg_color="black", fg_color="#1E1E1E",
                                    border_color="#3E3E3E", border_width=1, text_color="#2DF60D", justify="center")
                    elif lst[i][j] == "FAIL":
                        self.Entry = ctk.CTkEntry(root, width=214, height=23, corner_radius=2,
                                    font=('Lato',13,'bold'), bg_color="black", fg_color="#1E1E1E",
                                    border_color="#3E3E3E", border_width=1, text_color="red", justify="center")
                    else:
                        self.Entry = ctk.CTkEntry(root, width=214, height=23, corner_radius=2,
                                    font=('Lato',13), bg_color="black", fg_color="#1E1E1E",
                                    border_color="#3E3E3E", border_width=1, text_color="white", justify="center")
                    self.Entry.grid(row=i, column=j)
                    self.Entry.insert(END, lst[i][j])
                    self.Entry.configure(state="readonly")
    
    total_rows = len(lst)
    total_columns = len(lst[0])
    root = ctk.CTk()
    root.title("Ticket Results")
    t = Table(root)
    root.mainloop()