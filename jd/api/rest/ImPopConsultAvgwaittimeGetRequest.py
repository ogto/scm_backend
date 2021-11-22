from jd.api.base import RestApi

class ImPopConsultAvgwaittimeGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.waiter = None
			self.date = None

		def getapiname(self):
			return 'jingdong.im.pop.consult.avgwaittime.get'

			





