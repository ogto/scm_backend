from jd.api.base import RestApi

class EclpMasterQueryShipperRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.shipperNos = None

		def getapiname(self):
			return 'jingdong.eclp.master.queryShipper'

			





