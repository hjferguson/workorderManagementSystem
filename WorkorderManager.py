from Workorder import Workorder
class WorkorderManager:
    def __init__(self):
        self.workOrders = []
        self.id = 0
    
    def addWorkorder(self,subDate, member,unit,issue,comments):
        temp = Workorder(subDate, member,unit,issue,comments)
        temp.id = self.id
        self.workOrders.append(temp)
        self.id += 1

    def printAll(self):
        for workorder in self.workOrders:
            workorder.printAll()

    def printSelected(self,unit):
        for workorder in self.workOrders:
            if(workorder.unit == unit):
                workorder.printAll()
    
