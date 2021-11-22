from jd.api.base import RestApi

class YunpeiOrderShippingRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_sn = None
			self.company_name = None
			self.delivery_bill_id = None
			self.gtm_delivery = None
			self.remark = None

		def getapiname(self):
			return 'jingdong.yunpei.order.shipping'

			





