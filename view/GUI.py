import tkinter as tk
from view.MainMenuFrame import MainMenuFrame
from view.WorkorderFrame import WorkorderFrame
from view.WorkorderListFrame import WorkorderListFrame
from view.EditWorkorderFrame import EditWorkorderFrame

class GUI(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Workorder Management System")
        self.geometry("600x400")
        #Gui has instances of the different frames. The packs/unpacks depending on button selected
        self.main_menu_frame = MainMenuFrame(self,controller)
        self.workorder_frame = WorkorderFrame(self,controller)
        self.workorder_list_frame = WorkorderListFrame(self,controller)
        self.edit_workorder_frame = EditWorkorderFrame(self,controller=self.controller)

        self.show_main_menu()

    def show_main_menu(self):
        self.workorder_frame.pack_forget()
        self.workorder_list_frame.pack_forget()
        self.edit_workorder_frame.pack_forget()
        self.main_menu_frame.pack()

    def show_workorder_frame(self):
        self.main_menu_frame.pack_forget()
        self.workorder_list_frame.pack_forget()
        self.edit_workorder_frame.pack_forget()
        self.workorder_frame.pack()

    def show_workorder_list_frame(self):
        self.main_menu_frame.pack_forget()
        self.workorder_frame.pack_forget()
        self.edit_workorder_frame.pack_forget()
        self.workorder_list_frame.load_workorders() #before adding this, the listbox would update after relaunching the program
        self.workorder_list_frame.pack(fill=tk.BOTH, expand=True) #dynamic resizing of the display
    
    def show_edit_workorder_frame(self, workorder_id):
        self.main_menu_frame.pack_forget()
        self.workorder_list_frame.pack_forget()
        self.workorder_frame.pack_forget()
        self.edit_workorder_frame.workorder_id = workorder_id
        self.edit_workorder_frame.load_workorder(workorder_id)
        self.edit_workorder_frame.pack()

