from jd.api.base import RestApi

class WareWriteUpdateWareTitleRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.title = None

		def getapiname(self):
			return 'jingdong.ware.write.updateWareTitle'

			





