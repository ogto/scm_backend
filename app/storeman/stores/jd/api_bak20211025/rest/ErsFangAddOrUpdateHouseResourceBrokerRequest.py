from app.main.stores.jd.api.base import RestApi

class ErsFangAddOrUpdateHouseResourceBrokerRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.brokerId = None
			self.houseResourceId = None
			self.quotedPrice = None
			self.recommend = None
			self.orderNum = None
			self.cityCode = None
			self.sourceId = None

		def getapiname(self):
			return 'jingdong.ers.fang.addOrUpdateHouseResourceBroker'

			





