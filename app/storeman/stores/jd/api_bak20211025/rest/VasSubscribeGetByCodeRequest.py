from app.main.stores.jd.api.base import RestApi

class VasSubscribeGetByCodeRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.item_code = None

		def getapiname(self):
			return 'jingdong.vas.subscribe.getByCode'

			





