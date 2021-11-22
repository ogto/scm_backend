from jd.api.base import RestApi

class YunpeiOfferSubmitRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.demand_sn = None
			self.shipping_type = None
			self.shipping_pay_way = None
			self.other_fee = None
			self.offer_detail_params = None
			self.operate_name = None

		def getapiname(self):
			return 'jingdong.yunpei.offer.submit'

			





