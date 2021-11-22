from app.main.stores.jd.api.base import RestApi

class PopWareGpsApiOnlineRecordJosServiceQueryListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.queryToJson = None
			self.customsId = None
			self.serviceId = None

		def getapiname(self):
			return 'jingdong.pop.ware.gps.storeman.OnlineRecordJosService.queryList'

			





