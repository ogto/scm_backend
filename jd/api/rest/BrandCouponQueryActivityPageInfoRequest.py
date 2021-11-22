from jd.api.base import RestApi

class BrandCouponQueryActivityPageInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.endDate = None
			self.activityName = None
			self.pageSize = None
			self.currentPage = None
			self.startDate = None

		def getapiname(self):
			return 'jingdong.brand.coupon.queryActivityPageInfo'

			





