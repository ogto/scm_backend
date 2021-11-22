from app.main.stores.jd.api.base import RestApi

class B2bWareSearchSkulistFxRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.req = None

		def getapiname(self):
			return 'jingdong.b2b.ware.search.skulist.fx'

			
	

class SortKeys(object):
		def __init__(self):
			"""
			"""
			self.field = None
			self.sortType = None
			self.missing = None


class Req(object):
		def __init__(self):
			"""
			"""
			self.jdSkuId = None
			self.b2bPoolId = None
			self.returnFieldList = None
			self.operatorErp = None
			self.skuName = None
			self.yn = None
			self.sortList = None
			self.auditStatus = None
			self.status = None





