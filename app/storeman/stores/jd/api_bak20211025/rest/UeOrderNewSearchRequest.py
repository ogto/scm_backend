from app.main.stores.jd.api.base import RestApi

class UeOrderNewSearchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderCode = None
			self.appid = None
			self.pageSize = None
			self.page = None
			self.serviceTypeId = None

		def getapiname(self):
			return 'jingdong.ue.order.new.search'

			





