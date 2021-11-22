from app.main.stores.jd.api.base import RestApi

class UpdateSpuSymbolBindRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.request = None

		def getapiname(self):
			return 'jingdong.updateSpuSymbolBind'

			
	

class BdsSymbol(object):
		def __init__(self):
			"""
			"""
			self.secondClassifyId = None
			self.qualifyUrlList = None
			self.qualifyEndDate = None
			self.name = None
			self.id = None


class BdsSkuBindSymbol(object):
		def __init__(self):
			"""
			"""
			self.relationId = None
			self.skuId = None
			self.spuId = None
			self.isSku = None
			self.itemFirstCateCd = None
			self.itemSecondCateCd = None
			self.itemThirdCateCd = None
			self.symbolList = None
			self.itemFourthCateCd = None


class Request(object):
		def __init__(self):
			"""
			"""
			self.relationId = None
			self.submitTime = None
			self.ownerName = None
			self.spuId = None
			self.skuBindSymbolList = None





