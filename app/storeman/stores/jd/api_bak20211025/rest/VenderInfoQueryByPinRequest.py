from app.main.stores.jd.api.base import RestApi

class VenderInfoQueryByPinRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ext_json_param = None

		def getapiname(self):
			return 'jingdong.vender.info.queryByPin'

			





