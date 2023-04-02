import sqlite3 as sql

class Database:
    def __init__(self):
        self.conn = sql.connect("workorders.db") #hard coded this in instead of passing as a parameter because project scope is smol
        self.createTable()
    
    def createTable(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS work_orders
                            (id INTEGER PRIMARY KEY, submission_date TEXT, 
                            member TEXT, unit INT, issue TEXT, comments TEXT, )''') #subDate, member,unit,issue,comments
        self.conn.commit()