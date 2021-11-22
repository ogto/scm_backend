from jd.api.base import RestApi

class SkuWriteUpdateSkusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.skus = None

		def getapiname(self):
			return 'jingdong.sku.write.updateSkus'

			
	

class Prop(object):
		def __init__(self):
			"""
			"""
			self.attrValueAlias = None
			self.attrId = None
			self.attrValues = None


class Feature(object):
		def __init__(self):
			"""
			"""
			self.cn = None
			self.value = None
			self.key = None


class Sku(object):
		def __init__(self):
			"""
			"""
			self.wareId = None
			self.skuId = None
			self.saleAttrs = None
			self.features = None
			self.jdPrice = None
			self.outerId = None
			self.stockNum = None
			self.barCode = None
			self.props = None
			self.multiCateProps = None
			self.capacity = None





