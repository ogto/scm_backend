from app.main.stores.jd.api.base import RestApi

class ErsFangSynHouseResourceImgRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelId = None
			self.imgUrl = None
			self.imgType = None
			self.cityCode = None
			self.sourceId = None
			self.pSourceId = None

		def getapiname(self):
			return 'jingdong.ers.fang.synHouseResourceImg'

			





