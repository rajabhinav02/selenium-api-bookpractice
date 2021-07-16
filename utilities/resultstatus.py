import logging
from utilities import custom_logging as cl

class ResultStatus:
    resultlist = []
    log = cl.log(logging.DEBUG)

    def result(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("Pass")
                    self.log.info(resultmessage + " is working fine")
                else:
                    self.resultlist.append("Fail")
                    self.log.error(resultmessage + " is not working fine")
            else:
                self.resultlist.append("Fail")
                self.log.error(resultmessage + " is not working fine")
        except:
            self.resultlist.append("Fail")
            self.log.error(resultmessage + " is not working fine")

    def marktest(self, result, resultmessage):
        self.result(result, resultmessage)

    def marktestfinal(self, result, resultmessage, tcname):
        self.result(result, resultmessage)
        if "Fail" in self.resultlist:
            self.log.error(tcname + " Failed")
            self.resultlist.clear()
            assert True==False
        else:
            self.log.info(tcname + " Passed")
            assert True == True




