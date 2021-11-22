from app.main.stores.jd.api.base import RestApi

class PopIllegalApiServiceVenderJingcreditApiServiceWriteBackPrivilegeRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.gainInfoId = None
			self.privilegeType = None
			self.summaryYearMonth = None
			self.info = None

		def getapiname(self):
			return 'jingdong.pop.illegal.storeman.service.VenderJingcreditApiService.writeBackPrivilege'

			





