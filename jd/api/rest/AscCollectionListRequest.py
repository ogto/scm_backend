from jd.api.base import RestApi

class AscCollectionListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.jdInterveneFlag = None
			self.balanceFlag = None
			self.applyTimeBegin = None
			self.applyTimeEnd = None
			self.pageNumber = None
			self.pageSize = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.collection.list'

			





