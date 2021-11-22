from app.main.stores.jd.api.base import RestApi

class EclpRtwRejectorderinfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startDate = None
			self.endDate = None
			self.pageStart = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.eclp.rtw.rejectorderinfo'

			





