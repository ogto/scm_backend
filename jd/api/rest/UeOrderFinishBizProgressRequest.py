from jd.api.base import RestApi

class UeOrderFinishBizProgressRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appId = None
			self.barcode2 = None
			self.pic10 = None
			self.barcode1 = None
			self.failureReason = None
			self.dealRemark = None
			self.createBy = None
			self.pic1 = None
			self.failureName = None
			self.operateDate = None
			self.orderNo = None
			self.fixMethod = None
			self.pic9 = None
			self.pic8 = None
			self.pic7 = None
			self.pic6 = None
			self.dealResult = None
			self.pic5 = None
			self.pic4 = None
			self.usedMaterial = None
			self.pic3 = None
			self.pic2 = None

		def getapiname(self):
			return 'jingdong.ue.order.finishBizProgress'

			





