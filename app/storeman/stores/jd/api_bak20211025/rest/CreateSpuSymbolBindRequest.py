from app.main.stores.jd.api.base import RestApi

class CreateSpuSymbolBindRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.request = None

		def getapiname(self):
			return 'jingdong.createSpuSymbolBind'

			
	

class BdsSymbol(object):
		def __init__(self):
			"""
			"""
			self.secondClassifyId = None
			self.id = None
			self.name = None
			self.qualifyUrlList = None
			self.qualifyEndDate = None


class BdsSkuBindSymbol(object):
		def __init__(self):
			"""
			"""
			self.skuId = None
			self.spuId = None
			self.isSku = None
			self.itemFirstCateCd = None
			self.itemSecondCateCd = None
			self.itemThirdCateCd = None
			self.itemFourthCateCd = None
			self.symbolList = None


class Request(object):
		def __init__(self):
			"""
			"""
			self.relationId = None
			self.submitTime = None
			self.ownerName = None
			self.bussinessTypeEnum = None
			self.spuId = None
			self.skuBindSymbolList = None





