from view.GUI import GUI
from model.Database import Database

class Controller:
    def __init__(self,database):
        
        self.gui = GUI(self)
        self.database = database
        self.db.createTable()

    def run(self):
        self.gui.mainloop()
