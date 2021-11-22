from jd.api.base import RestApi

class UeOrderNewArriveRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.beginDate = None
			self.venderCode = None
			self.endDate = None
			self.appid = None
			self.pageSize = None
			self.page = None
			self.deliverType = None
			self.orderNo = None

		def getapiname(self):
			return 'jingdong.ue.order.new.arrive'

			





