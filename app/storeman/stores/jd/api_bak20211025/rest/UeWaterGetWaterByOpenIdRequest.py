from app.main.stores.jd.api.base import RestApi

class UeWaterGetWaterByOpenIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pin = None
			self.open_id_buyer = None

		def getapiname(self):
			return 'jingdong.ue.water.getWaterByOpenId'

			





