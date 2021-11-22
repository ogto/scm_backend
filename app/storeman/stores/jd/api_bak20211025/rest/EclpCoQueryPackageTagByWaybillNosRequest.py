from app.main.stores.jd.api.base import RestApi

class EclpCoQueryPackageTagByWaybillNosRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.lwbNos = None

		def getapiname(self):
			return 'jingdong.eclp.co.queryPackageTagByWaybillNos'

			





