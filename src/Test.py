from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("green")

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                if lst[i][j] == "To Do":
                    self.Entry = ctk.CTkEntry(root, width=856, height=23, corner_radius=4,
                                font=('Lato',13), bg_color="black", fg_color="#1E1E1E",
                                border_color="#3E3E3E", border_width=1, text_color="white", justify="center")
                if lst[i][j] in ["Date",'Hour','Action',"ERD", "Expected Data", "Data", "Data to write", "Result", "Comments"]:
                    self.Entry = ctk.CTkEntry(root, width=214, height=23, corner_radius=4,
                                font=('Lato',13, "bold"), bg_color="black", fg_color="#1E1E1E",
                                border_color="#3E3E3E", border_width=1, text_color="white", justify="center")
                elif lst[i][j] == "PASS":
                    self.Entry = ctk.CTkEntry(root, width=214, height=23, corner_radius=4,
                                font=('Lato',13,'bold'), bg_color="black", fg_color="#1E1E1E",
                                border_color="#3E3E3E", border_width=1, text_color="green", justify="center")
                elif lst[i][j] == "FAIL":
                    self.Entry = ctk.CTkEntry(root, width=214, height=23, corner_radius=4,
                                font=('Lato',13,'bold'), bg_color="black", fg_color="#1E1E1E",
                                border_color="#3E3E3E", border_width=1, text_color="red", justify="center")
                else:
                    self.Entry = ctk.CTkEntry(root, width=214, height=23, corner_radius=4,
                                font=('Lato',13), bg_color="black", fg_color="#1E1E1E",
                                border_color="#3E3E3E", border_width=1, text_color="white", justify="center")
                self.Entry.grid(row=i, column=j)
                self.Entry.insert(END, lst[i][j])
                self.Entry.configure(state="readonly")
# take the data
lst = [["Date",'Hour','Action',"ERD", "Expected Data", "Data", "Data to write", "Result", "Comments"],
       [2,'Aaryan','To Do',"---", "Verify Led 13 Turn On", 2, 3, 4, "Hola mundo soy yo de nuevo y es diferente"],
       [3,'Vaishnavi','Mumbai',"FAIL", 1, 2, 3, 4, 5],
       [4,'Rachna','Mumbai',"PASS", 1, 2, 3, 4, 5],
       [5,'Shubham','Delhi',"FAIL", 1, 2, 3, 4, 5]]


total_rows = len(lst)
total_columns = len(lst[0])
root = ctk.CTk()
t = Table(root)
root.mainloop()
