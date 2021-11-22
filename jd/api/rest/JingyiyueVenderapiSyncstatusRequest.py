from jd.api.base import RestApi

class JingyiyueVenderapiSyncstatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sourceKey = None
			self.orderId = None
			self.stateDesc = None
			self.stateCode = None
			self.pushTime = None
			self.extInfo = None

		def getapiname(self):
			return 'jingdong.jingyiyue.venderapi.syncstatus'

			





