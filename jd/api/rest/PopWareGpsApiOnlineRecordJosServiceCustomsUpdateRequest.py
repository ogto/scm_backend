from jd.api.base import RestApi

class PopWareGpsApiOnlineRecordJosServiceCustomsUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.recordingParamToJson = None
			self.recordedParamToJson = None
			self.customsId = None
			self.serviceId = None

		def getapiname(self):
			return 'jingdong.pop.ware.gps.api.OnlineRecordJosService.customsUpdate'

			





