import os
import json

def read_backup():
    file_path = "backup.json"
    if(os.path.exists(file_path)):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        return {}


def write_backup(data):
    file_path = "backup.json"
    with open(file_path, 'w') as f:
        json.dump(data, f)

class DiSred:
    def __init__(self, nama_database: str):
        self.dbname = nama_database
        backup = read_backup()
        if nama_database in backup:
            self.data = backup[nama_database]
        else:
            self.data = {}

    def get_keys(self):
        return list(self.data)

    def delete(self, key: str):
        if key in self.data:
            del self.data[key]

            dbname = self.dbname
            backup = read_backup()
            backup[dbname] = self.data
            write_backup(backup)
            return "OK"
        else:
            return "OK"

    def get_all(self):
        return self.data
        
    def get(self, key: str):
        if key in self.data:
            return self.data[key]
        else:
            return None
    
    def insert(self, key: str, value: str):
        self.data[key] = value
        
        dbname = self.dbname
        backup = read_backup()
        backup[dbname] = self.data
        write_backup(backup)
        return "OK"
    
    def flush(self):
        self.data = {}
        
        dbname = self.dbname
        backup = read_backup()
        backup[dbname] = self.data
        write_backup(backup)
        return "OK"