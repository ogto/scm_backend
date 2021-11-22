from jd.api.base import RestApi

class HealthYjtMaintanceRecordRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appId = None
			self.appKey = None
			self.jsonArray_details = None
			self.enterpriseId = None
			self.forceRegisterFlag = None
			self.goodsType = None
			self.maintanceDate = None
			self.maintanceManId = None
			self.maintanceType = None
			self.otcType = None
			self.prescriptionDrug = None
			self.remark = None

		def getapiname(self):
			return 'jingdong.health.yjt.maintance.record'

			





