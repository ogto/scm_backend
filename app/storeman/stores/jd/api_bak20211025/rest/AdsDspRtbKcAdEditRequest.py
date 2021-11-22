from app.main.stores.jd.api.base import RestApi

class AdsDspRtbKcAdEditRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.adInputVO = None
			self.paramExt = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kc.ad.edit'

			
	

class AdVO(object):
		def __init__(self):
			"""
			"""
			self.customTitle = None
			self.id = None
			self.name = None
			self.imgUrl = None
			self.skuId = None


class AdInputVO(object):
		def __init__(self):
			"""
			"""
			self.adList = None
			self.adGroupId = None
			self.showSalesWord = None
			self.url = None


class ParamExt(object):
		def __init__(self):
			"""
			"""





