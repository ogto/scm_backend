from app.main.stores.jd.api.base import RestApi

class EclpCoQueryB2BSWbMainRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.deptNo = None
			self.newWBType = None
			self.no = None

		def getapiname(self):
			return 'jingdong.eclp.co.queryB2BSWbMain'

			





