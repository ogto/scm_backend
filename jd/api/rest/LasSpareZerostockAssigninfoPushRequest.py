from jd.api.base import RestApi

class LasSpareZerostockAssigninfoPushRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.afs_no = None
			self.ord_no = None
			self.afs_ser_tas_no = None
			self.sit_no = None
			self.sit_n = None
			self.sit_tel = None
			self.act_t = None

		def getapiname(self):
			return 'jingdong.las.spare.zerostock.assigninfo.push'

			





