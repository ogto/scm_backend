from jd.api.base import RestApi

class PopOtoCheckNumberConsumerRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_id = None
			self.card_number = None
			self.pwd_umber = None
			self.shop_id = None
			self.shop_name = None
			self.code_type = None

		def getapiname(self):
			return 'jingdong.pop.oto.CheckNumber.consumer'

			





