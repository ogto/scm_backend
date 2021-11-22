from jd.api.base import RestApi

class LasImHfsArrivalPushRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ord_no = None
			self.ope_n = None
			self.ser_pro_no = None
			self.ope_t = None
			self.pro_no = None
			self.pro_n = None
			self.cit_no = None
			self.cit_n = None
			self.cou_no = None
			self.cou_n = None
			self.add = None
			self.poi_n = None
			self.con_tel = None
			self.con_n = None
			self.col_cod = None
			self.ser_nos = None

		def getapiname(self):
			return 'jingdong.las.im.hfs.arrival.push'

			





