import tkinter as tk
from view.MainMenuFrame import MainMenuFrame
from view.WorkorderFrame import WorkorderFrame

class GUI(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Workorder Management System")
        self.geometry("600x400")

        self.main_menu_frame = MainMenuFrame(self)
        self.workorder_frame = WorkorderFrame(self)

        self.show_main_menu()

    def show_main_menu(self):
        self.workorder_frame.pack_forget()
        self.main_menu_frame.pack()

    def show_workorder_frame(self):
        self.main_menu_frame.pack_forget()
        self.workorder_frame.pack()
