from app.main.stores.jd.api.base import RestApi

class DspAdunitAreaUpdateRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None
			self.areaId = None

		def getapiname(self):
			return 'jingdong.dsp.adunit.area.update'

			





