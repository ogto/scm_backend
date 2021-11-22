from app.main.stores.jd.api.base import RestApi

class HouseDataPublishSaasAddRentHouseActivityRelateIdsRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.relateInfo = None

		def getapiname(self):
			return 'jingdong.house.data.publish.saas.addRentHouseActivityRelateIds'

			





