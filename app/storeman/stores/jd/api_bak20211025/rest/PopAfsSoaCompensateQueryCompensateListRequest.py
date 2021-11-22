from app.main.stores.jd.api.base import RestApi

class PopAfsSoaCompensateQueryCompensateListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.compensateId = None
			self.id = None
			self.refId = None
			self.refType = None
			self.modifiedStartTime = None
			self.modifiedEndTime = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.pop.afs.soa.compensate.queryCompensateList'

			





