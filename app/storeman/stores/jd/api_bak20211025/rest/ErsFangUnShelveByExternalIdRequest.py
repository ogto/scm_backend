from app.main.stores.jd.api.base import RestApi

class ErsFangUnShelveByExternalIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cityCode = None
			self.sourceId = None

		def getapiname(self):
			return 'jingdong.ers.fang.unShelveByExternalId'

			





