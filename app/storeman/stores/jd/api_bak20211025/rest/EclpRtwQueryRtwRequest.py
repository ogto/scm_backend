from app.main.stores.jd.api.base import RestApi

class EclpRtwQueryRtwRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.eclpSoNo = None
			self.eclpRtwNo = None
			self.isvRtwNum = None
			self.warehouseNo = None
			self.reson = None
			self.orderInType = None
			self.queryBatAttrFlag = None

		def getapiname(self):
			return 'jingdong.eclp.rtw.queryRtw'

			





