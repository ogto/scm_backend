from app.main.stores.jd.api.base import RestApi

class EerdcActivityGatewayApiActivityexternaloperationRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.operType = None
			self.jsonData = None
			self.extStr = None

		def getapiname(self):
			return 'jingdong.eerdc.activity.gateway.storeman.activityexternaloperation'

			





