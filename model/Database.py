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
    
    #using cursor here because fetchall is a method of cursor class
    def searchWorkorderUnit(self, unit):
        cursor = self.conn.execute("SELECT * FROM work_orders WHERE unit = ?", (unit,))
        rows = cursor.fetchall()
        return rows

    def searchWorkorderMember(self, member):
            cursor = self.conn.execute("SELECT * FROM work_orders WHERE member = ?", (member,))
            rows = cursor.fetchall()
            return rows

    
    #after searching and finding workorder, edit it
    def update_workorder(self, workorder_id, sub_date, member, unit, issue, comments):
        self.conn.execute('''UPDATE work_orders SET submission_date = ?, member = ?, unit = ?, issue = ?, comments = ? WHERE id = ?''', (sub_date, member, unit, issue, comments, workorder_id))
        self.conn.commit()
        

    
    #after searching and finding workorder, delete it
    def deleteWorkorder(self, id):
        self.conn.execute("DELETE FROM work_orders WHERE id = ?", (id,))
        self.conn.commit()

    def get_all_workorders(self):
        cursor = self.conn.execute("SELECT * FROM work_orders")
        rows = cursor.fetchall()
        return rows

    def get_last_five_workorders(self):
        cursor = self.conn.execute("SELECT * FROM work_orders ORDER BY id DESC LIMIT 5")
        rows = cursor.fetchall()
        return rows
    
    def get_workorder_by_id(self, id):
        cursor = self.conn.execute("SELECT * FROM work_orders WHERE id = ?", (id,))
        rows = cursor.fetchall()
        return rows #returns a list of tuples

