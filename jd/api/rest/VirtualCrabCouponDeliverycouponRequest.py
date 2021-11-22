from jd.api.base import RestApi

class VirtualCrabCouponDeliverycouponRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.couponNumber = None
			self.merchantName = None
			self.merchantId = None
			self.trackingName = None
			self.trackingNumber = None
			self.trackingCode = None
			self.deliveryAddress = None
			self.deliveryTime = None
			self.receiverName = None
			self.receiverMobile = None
			self.deliveryStatus = None
			self.deliverySerialNumber = None

		def getapiname(self):
			return 'jingdong.virtual.crabCoupon.deliverycoupon'

			





