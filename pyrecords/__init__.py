import os

class Table:
    
    def __init__(self,columns):
        self.columns = columns
        self.records = []
        self.primary = None
        self.table = []
        
    def insert(self,record):
        if len(record) == len(self.columns):
            self.records.append(record)
        else:
            print('pyRecords error: Length of record does not match number of table columns')