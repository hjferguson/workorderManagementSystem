import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
class WorkorderFrame(tk.Frame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.sub_date_label = tk.Label(self, text="Submission Date:")
        self.sub_date_entry = DateEntry(self, date_pattern='yyyy-mm-dd', width=12, background='darkblue', foreground='white', borderwidth=2)
        
        self.member_label = tk.Label(self, text="Member:")
        self.member_entry = tk.Entry(self)

        self.unit_label = tk.Label(self, text="Unit:")
        self.unit_entry = tk.Entry(self)

        #I wanted the potential issues to be in a drop down to reduce the chance of misspelling
        #or redundancy.
        ISSUES = ['Appliance','Electrical','Plumbing','Painting','Drywall','Hardware','Other'] 
        self.issue_label = tk.Label(self, text="Issue:")
        self.issue_entry = ttk.Combobox(self, values=ISSUES)

        self.comments_label = tk.Label(self, text="Comments:")
        self.comments_entry = tk.Text(self,width=60, height=10)

        # Add a submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_workorder)

        # Add a back button
        self.back_button = tk.Button(self, text="Back", command=self.master.show_main_menu)

        #Using the grid layout manager to position the widgets
        self.sub_date_label.grid(row=0, column=0, padx=5, pady=5)
        self.sub_date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.member_label.grid(row=1, column=0, padx=5, pady=5)
        self.member_entry.grid(row=1, column=1, padx=5, pady=5)
        self.unit_label.grid(row=2, column=0, padx=5, pady=5)
        self.unit_entry.grid(row=2, column=1, padx=5, pady=5)
        self.issue_label.grid(row=3, column=0, padx=5, pady=5)
        self.issue_entry.grid(row=3, column=1, padx=5, pady=5)
        self.comments_label.grid(row=4, column=0, padx=5, pady=5)
        self.comments_entry.grid(row=4, column=1, padx=5, pady=5)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=5)
        self.back_button.grid(row=6, column=0, columnspan=2, pady=5)

    def submit_workorder(self):
        # Get the data from the input fields
        sub_date = self.sub_date_entry.get_date() # returns a datetime object
        sub_date_string = sub_date.strftime("%Y-%m-%d")    # convert to a string to work with TEXT column in db
        member = self.member_entry.get()
        unit = self.unit_entry.get()
        issue = self.issue_entry.get()
        comments = self.comments_entry.get("1.0", tk.END).strip()

       #insert into db
        self.controller.db.addWorkorder(sub_date_string, member, unit, issue, comments)

        # Clear the input fields after submitting
        self.sub_date_entry.delete(0, tk.END)
        self.member_entry.delete(0, tk.END)
        self.unit_entry.delete(0, tk.END)
        self.issue_entry.delete(0, tk.END)
        self.comments_entry.delete("1.0", tk.END)
