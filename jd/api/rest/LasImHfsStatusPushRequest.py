from jd.api.base import RestApi

class LasImHfsStatusPushRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ord_no = None
			self.ope_n = None
			self.ser_pro_no = None
			self.ope_t = None
			self.rem = None
			self.det = None
			self.loc = None

		def getapiname(self):
			return 'jingdong.las.im.hfs.status.push'

			





