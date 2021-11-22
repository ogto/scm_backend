from app.main.stores.jd.api.base import RestApi

class UeOrderNewSettleReconsiderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNo = None
			self.endDate = None
			self.pageSize = None
			self.dealType = None
			self.settleNo = None
			self.deliverType = None
			self.beginDate = None
			self.createBy = None
			self.venderCode = None
			self.appid = None
			self.page = None
			self.invoiceNo = None
			self.dealRemark = None
			self.settleType = None

		def getapiname(self):
			return 'jingdong.ue.order.new.settleReconsider'

			





