from app.main.stores.jd.api.base import RestApi

class TransportWriteUpdateWareTransportIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.transportId = None

		def getapiname(self):
			return 'jingdong.transport.write.updateWareTransportId'

			




