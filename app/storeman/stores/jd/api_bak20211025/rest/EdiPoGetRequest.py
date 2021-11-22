from app.main.stores.jd.api.base import RestApi

class EdiPoGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderStatus = None
			self.createTimeStart = None
			self.createTimeEnd = None
			self.pageNum = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.edi.po.get'

			





