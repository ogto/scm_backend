from app.main.stores.jd.api.base import RestApi

class B2bWareQuerySkuToPoolRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.businessChannel = None
			self.mappingId = None
			self.minJdSkuId = None
			self.jdSkuId = None
			self.totalItem = None
			self.pageNo = None
			self.totalPage = None
			self.mappingType = None
			self.pageSize = None
			self.b2bSkuToPoolQueryTypeEnum = None
			self.b2bPoolId = None

		def getapiname(self):
			return 'jingdong.b2b.ware.querySkuToPool'

			





