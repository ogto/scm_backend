from app.main.stores.jd.api.base import RestApi

class AdsDspRtbKcAdUpdateRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.adInputVO = None
			self.paramExt = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kc.ad.update'

			
	

class AdVO(object):
		def __init__(self):
			"""
			"""
			self.id = None
			self.name = None
			self.adGroupId = None
			self.imgUrl = None
			self.customTitle = None


class AdInputVO(object):
		def __init__(self):
			"""
			"""
			self.adList = None


class ParamExt(object):
		def __init__(self):
			"""
			"""





