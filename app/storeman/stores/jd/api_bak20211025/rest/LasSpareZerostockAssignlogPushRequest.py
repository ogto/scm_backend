from app.main.stores.jd.api.base import RestApi

class LasSpareZerostockAssignlogPushRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.afs_no = None
			self.ord_no = None
			self.afs_ser_tas_no = None
			self.tra_inf = None
			self.act_t = None

		def getapiname(self):
			return 'jingdong.las.spare.zerostock.assignlog.push'

			





