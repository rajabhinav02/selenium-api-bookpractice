from utilities.configuration import *
from utilities.resources import *
from utilities.payload import *
import utilities.custom_logging as cl
import requests

class AddDeleteBook:
    log= cl.log(logging.DEBUG)
    gquery = 'select * from Books'
    burl = getconfig()['API']['endpoint'] + Resources.areource
    durl = getconfig()['API']['endpoint'] + Resources.dresource
    uquery = 'update Books set aisle = %s where BookName = %s'

    def validatestatus(self):
        res = requests.post(self.burl,json=addpayload(self.gquery))
        #log.info(res)
        if res.status_code == 200:
            self.log.info("Status code is 200")
            return True
        else:
            self.log.error("status code is " +str(res.status_code))
            return False

    def validatemessage(self):
        res = requests.post(self.burl, json=addpayload(self.gquery))
        log.info(res)
        res_json = res.json()

        try:
            if res_json['Msg'] == 'successfully added':
                self.log.info(res_json['Msg'])
                return True
            else:
                self.log.error("no message")
                return False
        except:
            self.log.error("issue with return json for add")
            return False

    def updatedata(self):
        row = getquery(self.gquery)
        data= (int(row[2])+1, row[0])
        updatequery(self.uquery,data)
        self.log.info("Data Updated from "+ str(row[2]))

    def validatedb(self):
        row = getquery(self.gquery)
        self.updatedata()
        row2 = getquery(self.gquery)
        if row2[2] > row[2]:
            self.log.info("DB updated correctly")
            return True
        else:
            self.log.error("D not updated correctly")
            return False

    def getid(self):
        res=requests.post(self.burl,json=addpayload(self.gquery))
        res_json= res.json()
        id= res_json['ID']
        self.log.info("ID is "+id)
        return id


    def validatedelete(self):
        id = self.getid()
        resp = requests.post(self.durl, json=delpayload(id))
        self.log.info(resp)
        resp_json= resp.json()
        if resp.status_code == 200 and resp_json['msg']=='book is successfully deleted':
            self.log.info("Delete successful")
            return True
        else:
            self.log.error("Delete Failed")
            return False



