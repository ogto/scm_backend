from app.main.stores.jd.api.base import RestApi

class GxptDirectPayQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startCreated = None
			self.endCreated = None
			self.startModified = None
			self.endModified = None
			self.payType = None
			self.payState = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.gxpt.directPay.query'

			





