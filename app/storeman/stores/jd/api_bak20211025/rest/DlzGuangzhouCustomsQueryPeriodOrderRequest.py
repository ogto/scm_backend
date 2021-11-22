from app.main.stores.jd.api.base import RestApi

class DlzGuangzhouCustomsQueryPeriodOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.beginDate = None
			self.endDate = None
			self.page = None
			self.type = None

		def getapiname(self):
			return 'jingdong.dlz.guangzhou.customs.queryPeriodOrder'

			





