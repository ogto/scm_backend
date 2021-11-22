from app.main.stores.jd.api.base import RestApi

class LasSpareZerostockDetectionPushRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ord_no = None
			self.afs_no = None
			self.afs_ser_tas_no = None
			self.eng_no = None
			self.eng_n = None
			self.eng_mp = None
			self.goo_sku = None
			self.act_t = None
			self.goo_n = None
			self.det_rs = None
			self.is_inv = None
			self.goo_sn = None
			self.not_ref_rea = None
			self.ref_rea = None
			self.dea_typ = None
			self.goo_pac_n = None
			self.goo_ext_n = None
			self.goo_fun_n = None
			self.att_desc = None
			self.is_bro_scr = None

		def getapiname(self):
			return 'jingdong.las.spare.zerostock.detection.push'

			





