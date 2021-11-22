from app.main.stores.jd.api.base import RestApi

class VirtualCrabCouponInvalidRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.merchantId = None
			self.merchantName = None
			self.couponNumber = None
			self.remark = None
			self.invalidTime = None
			self.invalidSerialNumber = None

		def getapiname(self):
			return 'jingdong.virtual.crabCoupon.invalid'

			





