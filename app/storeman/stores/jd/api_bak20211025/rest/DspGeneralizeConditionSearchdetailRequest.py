from app.main.stores.jd.api.base import RestApi

class DspGeneralizeConditionSearchdetailRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.token = None
			self.keyValue = None
			self.equipment = None
			self.page = None
			self.type = None
			self.areaValue = None

		def getapiname(self):
			return 'jingdong.dsp.generalize.condition.searchdetail'

			





