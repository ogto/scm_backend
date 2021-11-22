from app.main.stores.jd.api.base import RestApi

class ImPopEvaluationstatGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.waiter = None
			self.startTime = None
			self.endTime = None

		def getapiname(self):
			return 'jingdong.im.pop.evaluationstat.get'

			





