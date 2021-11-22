from jd.api.base import RestApi

class UeRecoveryOutServiceAssignListJsfServiceGetSyncAssignOrderListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.code = None
			self.appid = None

		def getapiname(self):
			return 'jingdong.ue.recovery.out.service.AssignListJsfService.getSyncAssignOrderList'

			





