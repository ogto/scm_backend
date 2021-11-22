from app.main.stores.jd.api.base import RestApi

class UeRecoveryOrderCompletedRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.nameplatePic = None
			self.realResiduePrice = None
			self.verifyCode = None
			self.userVerifyPic = None
			self.finishOrder = None
			self.machinePic = None
			self.finishOrderRemark = None
			self.orderNo = None
			self.code = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.completed'

			





