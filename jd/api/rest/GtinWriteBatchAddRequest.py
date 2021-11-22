from jd.api.base import RestApi

class GtinWriteBatchAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.batchAddVo = None

		def getapiname(self):
			return 'jingdong.gtin.write.batchAdd'

			
	

class GtinVo(object):
		def __init__(self):
			"""
			"""
			self.importer = None
			self.gtin = None
			self.brandName = None
			self.certificateCode = None
			self.address = None
			self.origin = None
			self.specification = None
			self.serialNo = None
			self.productDesc = None
			self.productImageUrls = None
			self.tcCode = None
			self.firmName = None
			self.status = None
			self.baseCreateTime = None
			self.baseLastUpdated = None
			self.saleDate = None


class BatchAddVo(object):
		def __init__(self):
			"""
			"""
			self.gtinVos = None
			self.appName = None
			self.ip = None
			self.uuid = None





