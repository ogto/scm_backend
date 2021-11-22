from app.main.stores.jd.api.base import RestApi

class AdsDspRtbTpBatchUpdateDifferentDmpPriceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.dmpVOS = None
			self.paramExt = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.batchUpdateDifferentDmpPrice'

			
	

class DmpVO(object):
		def __init__(self):
			"""
			"""
			self.ids = None
			self.adGroupId = None
			self.adGroupPrice = None


class ParamExt(object):
		def __init__(self):
			"""
			"""





