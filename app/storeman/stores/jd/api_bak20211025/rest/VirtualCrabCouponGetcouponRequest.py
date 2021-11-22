from app.main.stores.jd.api.base import RestApi

class VirtualCrabCouponGetcouponRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.merchantId = None
			self.merchantName = None
			self.orderId = None
			self.channelType = None
			self.couponType = None
			self.couponNumber = None
			self.trackingName = None
			self.trackingNumber = None
			self.sendTime = None
			self.receiverName = None
			self.receiverMobile = None
			self.sendSerialNumber = None

		def getapiname(self):
			return 'jingdong.virtual.crabCoupon.getcoupon'

			





