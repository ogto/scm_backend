from jd.api.base import RestApi

class HouseHandleDsjInfo2JDForInsertRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.productInfo = None

		def getapiname(self):
			return 'jingdong.house.handleDsjInfo2JDForInsert'

			





