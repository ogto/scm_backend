from jd.api.base import RestApi

class UeNewSaaSOrderFinishBizProgressRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.warrantyCard = None
			self.detecResult = None
			self.usedMaterial = None
			self.failureName = None
			self.invoiceSituation = None
			self.pic1 = None
			self.inSkuSn = None
			self.installSituation = None
			self.appId = None
			self.pic6 = None
			self.pic7 = None
			self.pic8 = None
			self.chargeAmount = None
			self.pic9 = None
			self.pic2 = None
			self.pic3 = None
			self.dealRemark = None
			self.pic4 = None
			self.pic5 = None
			self.fixMethod = None
			self.detecDetail = None
			self.outRepair = None
			self.orderNo = None
			self.barcode2 = None
			self.barcode1 = None
			self.createBy = None
			self.pic10 = None
			self.callSource = None
			self.failureReason = None
			self.outSkuSn = None
			self.dealResult = None
			self.operateDate = None
			self.receiveBrand = None
			self.buyYear = None

		def getapiname(self):
			return 'jingdong.ue.newSaaSOrder.finishBizProgress'

			





