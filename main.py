#Harlan Ferguson 101133838
from Controller import Controller
from model.Database import Database
from view.GUI import GUI
if __name__ == "__main__":
    db = Database()
    controller = Controller(db)
    gui = GUI(controller)
    controller.run()
    gui.mainloop()
    