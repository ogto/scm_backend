from app.main.stores.jd.api.base import RestApi

class CrmMemberScanRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pin = None
			self.grade = None
			self.min_last_trade_time = None
			self.max_last_trade_time = None
			self.min_trade_count = None
			self.max_trade_count = None
			self.avg_price = None
			self.min_trade_amount = None
			self.page_size = None
			self.scroll_id = None
			self.open_id_buyer = None

		def getapiname(self):
			return 'jingdong.crm.member.scan'

			





