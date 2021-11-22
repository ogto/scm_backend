from app.main.stores.jd.api.base import RestApi

class HouseHandleDsjInfo2JDForUpdateRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.productInfo = None

		def getapiname(self):
			return 'jingdong.house.handleDsjInfo2JDForUpdate'

			





