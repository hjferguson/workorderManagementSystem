#
from WorkorderManager import WorkorderManager
from Database import Database
if __name__ == "__main__":
    WM = WorkorderManager()
    DB = Database()
    WM.addWorkorder("2023-03-30","Harlan","224","Slow bathtub drain", "It takes a long time for the bathtub to drain. Can someone please come and take a look?")

    print("This is a test")
    WM.printAll()
    print("-----------")
    WM.printSelected("224")