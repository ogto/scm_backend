from app.main.stores.jd.api.base import RestApi

class UpdateSkuSymbolBindRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.request = None

		def getapiname(self):
			return 'jingdong.updateSkuSymbolBind'

			
	

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
			self.symbolList = None
			self.itemSecondCateCd = None
			self.itemThirdCateCd = None
			self.spuId = None
			self.itemFirstCateCd = None
			self.skuId = None
			self.itemFourthCateCd = None


class Request(object):
		def __init__(self):
			"""
			"""
			self.submitTime = None
			self.ownerName = None
			self.skuBindSymbolList = None





