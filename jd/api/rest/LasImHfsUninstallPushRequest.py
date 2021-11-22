from jd.api.base import RestApi

class LasImHfsUninstallPushRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ord_no = None
			self.ser_pro_no = None
			self.ope_t = None
			self.ope_n = None
			self.ope_tel = None
			self.uni_det = None

		def getapiname(self):
			return 'jingdong.las.im.hfs.uninstall.push'

			





