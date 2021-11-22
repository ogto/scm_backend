from jd.api.base import RestApi

class OmnichannelOrderLocateinfoSearchRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderIdListJsonStr = None

		def getapiname(self):
			return 'jingdong.omnichannel.order.locateinfo.search'

			





