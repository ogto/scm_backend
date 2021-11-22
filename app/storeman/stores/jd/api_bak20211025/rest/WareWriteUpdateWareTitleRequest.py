from app.main.stores.jd.api.base import RestApi

class WareWriteUpdateWareTitleRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.title = None

		def getapiname(self):
			return 'jingdong.ware.write.updateWareTitle'

			





