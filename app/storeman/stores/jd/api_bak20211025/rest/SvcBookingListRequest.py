from app.main.stores.jd.api.base import RestApi

class SvcBookingListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appId = None
			self.verificationStatus = None
			self.storeName = None
			self.lcnNo = None
			self.mobile = None
			self.submitTimeStart = None
			self.submitTimeEnd = None
			self.pageSize = None
			self.pageIndex = None

		def getapiname(self):
			return 'jingdong.svc.booking.list'

			





