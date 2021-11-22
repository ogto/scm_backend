from jd.api.base import RestApi

class VirtualCrabCouponAppointRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.couponNumber = None
			self.merchantId = None
			self.merchantName = None
			self.appointTime = None
			self.deliveryType = None
			self.deliveryAddress = None
			self.deliveryTime = None
			self.receiverName = None
			self.receiverMobile = None
			self.appointSerialNumber = None

		def getapiname(self):
			return 'jingdong.virtual.crabCoupon.appoint'

			





