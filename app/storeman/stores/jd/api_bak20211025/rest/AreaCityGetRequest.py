from app.main.stores.jd.api.base import RestApi

class AreaCityGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.parent_id = None

		def getapiname(self):
			return 'jingdong.area.city.get'

			





