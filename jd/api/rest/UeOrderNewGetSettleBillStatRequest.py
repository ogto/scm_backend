from jd.api.base import RestApi

class UeOrderNewGetSettleBillStatRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
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
			return 'jingdong.ue.order.new.getSettleBillStat'

			





