from jd.api.base import RestApi

class GetStagepayBusinessExtInfoByCouponCodeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.CouponCode = None

		def getapiname(self):
			return 'jingdong.getStagepayBusinessExtInfoByCouponCode'

			





