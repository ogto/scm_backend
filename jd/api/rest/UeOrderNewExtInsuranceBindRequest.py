from jd.api.base import RestApi

class UeOrderNewExtInsuranceBindRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.bindStat = None
			self.appid = None
			self.venderCode = None
			self.remark = None
			self.orderNos = None

		def getapiname(self):
			return 'jingdong.ue.order.new.extInsuranceBind'

			





