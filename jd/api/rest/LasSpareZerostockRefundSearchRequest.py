from jd.api.base import RestApi

class LasSpareZerostockRefundSearchRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.out_no = None

		def getapiname(self):
			return 'jingdong.las.spare.zerostock.refund.search'

			





