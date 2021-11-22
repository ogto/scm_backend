from jd.api.base import RestApi

class LasImHfsCollectPushRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ord_no = None
			self.ope_n = None
			self.ser_pro_no = None
			self.col_no = None
			self.ope_t = None
			self.rem = None
			self.dis_pho = None

		def getapiname(self):
			return 'jingdong.las.im.hfs.collect.push'

			





