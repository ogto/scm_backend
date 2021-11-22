from app.main.stores.jd.api.base import RestApi

class SkuWriteSaveWareSkusRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.skus = None

		def getapiname(self):
			return 'jingdong.sku.write.saveWareSkus'

			
	

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
			self.values = None
			self.key = None


class Sku(object):
		def __init__(self):
			"""
			"""
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





