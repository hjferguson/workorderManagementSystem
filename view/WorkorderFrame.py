import tkinter as tk
class WorkorderFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        # Add your labels and input fields for entering workorder details
        self.sub_date_label = tk.Label(self, text="Submission Date:")
        self.sub_date_entry = tk.Entry(self)

        self.member_label = tk.Label(self, text="Member:")
        self.member_entry = tk.Entry(self)

        self.unit_label = tk.Label(self, text="Unit:")
        self.unit_entry = tk.Entry(self)

        self.issue_label = tk.Label(self, text="Issue:")
        self.issue_entry = tk.Entry(self)

        self.comments_label = tk.Label(self, text="Comments:")
        self.comments_entry = tk.Entry(self)

        # Add a submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_workorder)

        # Add a back button
        self.back_button = tk.Button(self, text="Back", command=self.master.show_main_menu)

        # Use the grid layout manager to position the widgets
        self.sub_date_label.grid(row=0, column=0)
        self.sub_date_entry.grid(row=0, column=1)
        self.member_label.grid(row=1, column=0)
        self.member_entry.grid(row=1, column=1)
        self.unit_label.grid(row=2, column=0)
        self.unit_entry.grid(row=2, column=1)
        self.issue_label.grid(row=3, column=0)
        self.issue_entry.grid(row=3, column=1)
        self.comments_label.grid(row=4, column=0)
        self.comments_entry.grid(row=4, column=1)
        self.submit_button.grid(row=5, column=0, columnspan=2)
        self.back_button.grid(row=6, column=0, columnspan=2)

    def submit_workorder(self):
        # Get the data from the input fields and call the WorkorderManager method to create a new workorder
        sub_date = self.sub_date_entry.get()
        member = self.member_entry.get()
        unit = self.unit_entry.get()
        issue = self.issue_entry.get()
        comments = self.comments_entry.get()

       
        self.master.db.insert_workorder(sub_date, member, unit, issue, comments)

        # Clear the input fields after submitting
        self.sub_date_entry.delete(0, tk.END)
        self.member_entry.delete(0, tk.END)
        self.unit_entry.delete(0, tk.END)
        self.issue_entry.delete(0, tk.END)
        self.comments_entry.delete(0, tk.END)

        # Return to the main menu
        self.master.show_main_menu()
