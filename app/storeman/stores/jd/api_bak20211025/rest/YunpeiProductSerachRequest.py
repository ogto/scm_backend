from app.main.stores.jd.api.base import RestApi

class YunpeiProductSerachRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.product_id = None
			self.oe_id = None
			self.page_no = None
			self.pop_product_sn = None

		def getapiname(self):
			return 'jingdong.yunpei.product.serach'

			





