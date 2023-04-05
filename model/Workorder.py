class Workorder:
    def __init__(self, subDate, member,unit,issue,comments):
        self.id = None
        self.subDate = subDate
        self.member = member
        self.unit = unit
        self.issue = issue
        self.comments = comments
        
    
    def printAll(self):
        print(f"ID: {self.id}")
        print(f"Submission date: {self.subDate}")
        print(f"Member: {self.member}")            
        print(f"Unit: {self.unit}")            
        print(f"Issue: {self.issue}")     
        print(f"Comments: {self.comments}")       
    
    
    