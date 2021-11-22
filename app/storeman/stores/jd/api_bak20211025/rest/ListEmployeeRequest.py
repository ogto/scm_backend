from app.main.stores.jd.api.base import RestApi

class ListEmployeeRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.storeId = None
			self.name = None
			self.phone = None
			self.employeeId = None
			self.pageNum = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.listEmployee'

			





