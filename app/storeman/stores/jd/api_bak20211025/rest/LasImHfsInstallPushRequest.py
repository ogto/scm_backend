from app.main.stores.jd.api.base import RestApi

class LasImHfsInstallPushRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ord_no = None
			self.ser_pro_no = None
			self.ver_cod = None
			self.ope_t = None
			self.ope_n = None
			self.ope_tel = None
			self.ins_det = None

		def getapiname(self):
			return 'jingdong.las.im.hfs.install.push'

			





