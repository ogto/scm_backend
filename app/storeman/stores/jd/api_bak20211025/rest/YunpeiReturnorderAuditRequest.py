from app.main.stores.jd.api.base import RestApi

class YunpeiReturnorderAuditRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.return_bill_sn = None
			self.is_agree = None
			self.opinion = None

		def getapiname(self):
			return 'jingdong.yunpei.returnorder.audit'

			





