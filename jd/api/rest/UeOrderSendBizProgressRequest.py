from jd.api.base import RestApi

class UeOrderSendBizProgressRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sendDate = None
			self.appId = None
			self.engineerName = None
			self.netWorkContactMan = None
			self.engineerCode = None
			self.netWorkTel = None
			self.netWorkCode = None
			self.netWorkAddress = None
			self.sendNetWorkDate = None
			self.engineerMobile = None
			self.sendEngineeDate = None
			self.orderNo = None
			self.netWorkName = None
			self.sendBy = None
			self.type = None

		def getapiname(self):
			return 'jingdong.ue.order.sendBizProgress'

			





