from jd.api.base import RestApi

class ImPopWaiterOnlinetimeStatGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.waiter = None
			self.startTime = None
			self.endTime = None

		def getapiname(self):
			return 'jingdong.im.pop.waiter.onlinetime.stat.get'

			





