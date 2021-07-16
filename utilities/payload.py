from utilities.configuration import *

def addpayload(gquery):
    row= getquery(gquery)
    bookin = {}
    bookin['name'] = row[0]
    bookin['isbn'] = row[1]
    bookin['aisle'] = row[2]
    bookin['author'] = row[3]
    return bookin

def delpayload(id):
    body = {
        "ID":id
    }
    return body