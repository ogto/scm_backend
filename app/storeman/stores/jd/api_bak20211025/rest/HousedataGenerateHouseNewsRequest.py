from app.main.stores.jd.api.base import RestApi

class HousedataGenerateHouseNewsRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.articleParam = None

		def getapiname(self):
			return 'jingdong.housedata.generateHouseNews'

			





