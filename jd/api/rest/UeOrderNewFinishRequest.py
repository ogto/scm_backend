from jd.api.base import RestApi

class UeOrderNewFinishRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.barcode2 = None
			self.barcode1 = None
			self.failureReason = None
			self.siteName = None
			self.failureName = None
			self.pic1 = None
			self.venderCode = None
			self.pic2 = None
			self.pic3 = None
			self.dealRemark = None
			self.pic4 = None
			self.fixMethod = None
			self.createBy = None
			self.appid = None
			self.dealResult = None
			self.settleCode = None
			self.inSkuSn = None
			self.outSkuSn = None
			self.orderNo = None
			self.detecDetail = None
			self.detecResult = None
			self.detecPic = None
			self.installSituation = None
			self.invoiceSituation = None
			self.warrantyCard = None
			self.outRepair = None
			self.chargeAmount = None

		def getapiname(self):
			return 'jingdong.ue.order.new.finish'

			





