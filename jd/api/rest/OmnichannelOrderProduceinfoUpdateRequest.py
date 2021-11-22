from jd.api.base import RestApi

class OmnichannelOrderProduceinfoUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.status = None
			self.storeType = None
			self.storeId = None
			self.operateName = None
			self.operateTime = None

		def getapiname(self):
			return 'jingdong.omnichannel.order.produceinfo.update'

			





