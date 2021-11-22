from jd.api.base import RestApi

class ImPopEvaluationlistGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.waiter = None
			self.startTime = None
			self.endTime = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.im.pop.evaluationlist.get'

			





