from app.main.stores.jd.api.base import RestApi

class ZxjCodGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.province_id = None
			self.city_id = None
			self.county_id = None
			self.town_id = None

		def getapiname(self):
			return 'jingdong.zxj.cod.get'

			





