from jd.api.base import RestApi

class LasSpareZerostockConfirmRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.afs_no = None
			self.ven_cod = None
			self.war_det = None

		def getapiname(self):
			return 'jingdong.las.spare.zerostock.confirm'

			





