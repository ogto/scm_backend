from jd.api.base import RestApi

class UeNewSaaSOrderSyncEngineerVaccineRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderCode = None
			self.isVaccination = None
			self.appId = None
			self.temperature = None
			self.identityCard = None
			self.vaccineFile = None
			self.vaccinationDate = None

		def getapiname(self):
			return 'jingdong.ue.newSaaSOrder.syncEngineerVaccine'

			





