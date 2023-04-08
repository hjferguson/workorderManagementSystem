import tkinter as tk
from tkinter import messagebox

class WorkorderListFrame(tk.Frame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()
        self.load_workorders()
 
    def create_widgets(self):
        
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=0, column=0, rowspan=6, sticky="nsew")
        
        self.view_button = tk.Button(self, text="View All", command=self.view_workorders)
        self.view_button.grid(row=0, column=1, padx=5)

        self.search_button = tk.Button(self, text="Search", command=self.display_search_workorders)
        self.search_button.grid(row=1, column=1, padx=5)

        self.edit_button = tk.Button(self, text="Edit", command=self.edit_workorder)
        self.edit_button.grid(row=2, column=1, padx=5)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_workorder)
        self.delete_button.grid(row=3, column=1, padx=5)

        self.back_button = tk.Button(self, text="Back", command=self.master.show_main_menu)
        self.back_button.grid(row=4, column=1, padx=5)


    def load_workorders(self):
        self.listbox.delete(0, tk.END)
        workorders = self.master.controller.db.get_last_five_workorders()
        for workorder in workorders:
            self.listbox.insert(tk.END, f"{workorder[0]} - {workorder[2]} - {workorder[4]}") #0,2,4 = id,name,issue

    def view_workorders(self):
        self.listbox.delete(0, tk.END) #clears the listbox
        workorders = self.master.controller.db.get_all_workorders()
        self.listbox.insert(tk.END, f"ID - Submission Date - Member - Unit - Issue - Comments")
        for workorder in workorders:
            self.listbox.insert(tk.END, f"{workorder[0]} - {workorder[1]} - {workorder[2]} - {workorder[3]} - {workorder[4]} - {workorder[5]}")

    def display_search_workorders(self):
        self.member_label = tk.Label(self, text="Search by Member:")
        self.member_label.grid(row=5, column=0, pady=5, sticky="w")
        self.member_entry = tk.Entry(self)
        self.member_entry.grid(row=5, column=1, pady=5)

        self.unit_label = tk.Label(self, text="Search by Unit:")
        self.unit_label.grid(row=6, column=0, pady=5, sticky="w")
        self.unit_entry = tk.Entry(self)
        self.unit_entry.grid(row=6, column=1, pady=5)

        self.search_button = tk.Button(self, text="Search", command=self.search_workorders)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=5)

    
    def search_workorders(self):
        member = self.member_entry.get()
        unit = self.unit_entry.get()
        if(member != ""):
            self.listbox.delete(0, tk.END)
            workorders = self.master.controller.db.searchWorkorderMember(member)
            self.listbox.insert(tk.END, f"ID - Submission Date - Member - Unit - Issue - Comments")
            for workorder in workorders:
                self.listbox.insert(tk.END, f"{workorder[0]} - {workorder[1]} - {workorder[2]} - {workorder[3]} - {workorder[4]} - {workorder[5]}")
        elif(unit != ""):
            self.listbox.delete(0, tk.END)
            workorders = self.master.controller.db.searchWorkorderUnit(unit)
            self.listbox.insert(tk.END, f"ID - Submission Date - Member - Unit - Issue - Comments")
            for workorder in workorders:
                self.listbox.insert(tk.END, f"{workorder[0]} - {workorder[1]} - {workorder[2]} - {workorder[3]} - {workorder[4]} - {workorder[5]}")
        else:
            messagebox.showerror("Error", "Please enter a member or unit to search for.")
            self.load_workorders()

    
    def edit_workorder(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No workorder selected.")
            return

        workorder_id = int(self.listbox.get(selected).split()[0])
        
        self.master.show_edit_workorder_frame(workorder_id)

        self.grid_remove()  # Hide the WorkorderListFrame


    def delete_workorder(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No workorder selected.")
            return

        workorder_id = int(self.listbox.get(selected).split()[0])

        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected work order?")
        if confirm:
            self.controller.db.deleteWorkorder(workorder_id)
            self.listbox.delete(selected)