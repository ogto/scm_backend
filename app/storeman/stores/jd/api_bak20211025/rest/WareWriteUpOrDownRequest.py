from app.main.stores.jd.api.base import RestApi

class WareWriteUpOrDownRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.note = None
			self.wareId = None
			self.opType = None

		def getapiname(self):
			return 'jingdong.ware.write.upOrDown'

			





