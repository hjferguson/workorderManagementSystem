import tkinter as tk
class MainMenuFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        # Add your menu buttons here, aligned vertically down the center.
        # Set the command for each button to switch to the appropriate frame.
        self.menu_button_nw = tk.Button(self, text="Add Workorder", relief="raised",bg="green", command=self.master.show_workorder_frame)
        self.menu_button_nw.pack(pady=20) #unfortunately it is not pady, but padding - y axis...
        self.menu_button_s = tk.Button(self, text="View Workorders", relief="raised",bg="green", command=self.master.show_workorder_list_frame)
        self.menu_button_s.pack(pady=20)
        #initial design has edit in main menu, but makes more sense to integrate it into search
        # self.menu_button_e = tk.Menubutton(self, text="Edit Workorder", relief="raised",bg="green")
        # self.menu_button_e.pack()
        self.menu_button_exit = tk.Button(self, text="Exit", relief="raised",bg="red", command=self.quit)
        self.menu_button_exit.pack(pady=20)

