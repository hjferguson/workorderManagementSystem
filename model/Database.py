import sqlite3 as sql

class Database:
    def __init__(self):
        self.conn = sql.connect("workorders.db") #hard coded this in instead of passing as a parameter because project scope is smol
        self.createTable()
    
    #For the methods, I researched and found that you don't need to make a cursor object, this is done automatically with sqlite3 when
    #execute is used on a connection object.

    def createTable(self): #added autoincrement to id to make unique
        self.conn.execute('''CREATE TABLE IF NOT EXISTS work_orders
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, submission_date TEXT,
                            member TEXT, unit INT, issue TEXT, comments TEXT)''')
        self.conn.commit()

    def addWorkorder(self,subDate, member,unit,issue,comments):
        self.conn.execute("INSERT INTO work_orders (submission_date, member, unit, issue, comments) VALUES (?,?,?,?,?)", (subDate, member,unit,issue,comments))
        self.conn.commit()
    
    def searchWorkorderUnit(self,unit):
        self.conn.execute("SELECT * FROM work_orders WHERE unit = ?", (unit,))
        self.conn.commit()
    
    def searchWorkorderMember(self,member):
        self.conn.execute("SELECT * FROM work_orders WHERE member = ?", (member,))
        self.conn.commit()
    
    #after searching and finding workorder, edit it
    def editWorkorder(self,subDate, member,unit,issue,comments):
        self.conn.execute("UPDATE work_orders SET submission_date = ?, member = ?, unit = ?, issue = ?, comments = ? WHERE id = ?", (subDate, member,unit,issue,comments))
        self.conn.commit()
    
    #after searching and finding workorder, delete it
    def deleteWorkorder(self,subDate, member,unit,issue,comments):
        self.conn.execute("DELETE FROM work_orders WHERE id = ?", (id,))
        self.conn.commit()