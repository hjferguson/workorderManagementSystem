from view.GUI import GUI
from model.Database import Database

class Controller:
    def __init__(self,database):
        self.db = database
        self.gui = GUI(self)
        self.db.createTable()

    def run(self):
        self.gui.mainloop()

