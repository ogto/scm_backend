from app.main.stores.jd.api.base import RestApi

class DspMaterialQueryListByParamRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.effective = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.material.queryListByParam'

			





