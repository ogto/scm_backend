from app.main.stores.jd.api.base import RestApi

class AreasOverseasProvinceGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)

		def getapiname(self):
			return 'jingdong.areas.overseasProvince.get'

			





