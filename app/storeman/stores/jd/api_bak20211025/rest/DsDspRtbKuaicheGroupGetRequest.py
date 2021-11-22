from app.main.stores.jd.api.base import RestApi

class DsDspRtbKuaicheGroupGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None

		def getapiname(self):
			return 'jingdong.ds.dsp.rtb.kuaiche.group.get'

			





