from app.main.stores.jd.api.base import RestApi

class HairQueryBookRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.beginDate = None
			self.supNo = None
			self.poNo = None
			self.endDate = None
			self.whNo = None
			self.ownerNo = None
			self.pageSize = None
			self.page = None
			self.dcNo = None

		def getapiname(self):
			return 'jingdong.hair.queryBook'

			





