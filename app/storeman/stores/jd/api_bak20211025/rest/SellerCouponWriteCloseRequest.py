from app.main.stores.jd.api.base import RestApi

class SellerCouponWriteCloseRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ip = None
			self.port = None
			self.couponId = None

		def getapiname(self):
			return 'jingdong.seller.coupon.write.close'

			





