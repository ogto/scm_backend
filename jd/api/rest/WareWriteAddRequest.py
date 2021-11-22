from jd.api.base import RestApi

class WareWriteAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ware = None
			self.skus = None

		def getapiname(self):
			return 'jingdong.ware.write.add'

			
	

class AdWords(object):
		def __init__(self):
			"""
			"""
			self.url = None
			self.urlWords = None
			self.words = None


class Prop(object):
		def __init__(self):
			"""
			"""
			self.attrId = None
			self.attrValues = None


class Feature(object):
		def __init__(self):
			"""
			"""
			self.key = None
			self.value = None


class Image(object):
		def __init__(self):
			"""
			"""
			self.colorId = None
			self.imgIndex = None
			self.imgUrl = None
			self.imgZoneId = None


class Ware(object):
		def __init__(self):
			"""
			"""
			self.title = None
			self.categoryId = None
			self.multiCategoryId = None
			self.brandId = None
			self.templateId = None
			self.transportId = None
			self.wareStatus = None
			self.outerId = None
			self.itemNum = None
			self.barCode = None
			self.wareLocation = None
			self.delivery = None
			self.promiseId = None
			self.adWords = None
			self.wrap = None
			self.packListing = None
			self.length = None
			self.width = None
			self.height = None
			self.weight = None
			self.props = None
			self.features = None
			self.images = None
			self.shopCategorys = None
			self.mobileDesc = None
			self.introduction = None
			self.afterSales = None
			self.jdPrice = None
			self.marketPrice = None
			self.zhuangBaId = None
			self.introductionUseFlag = None
			self.mobileZhuangBaId = None
			self.mobileDescUseFlag = None
			self.designConcept = None
			self.fitCaseHtmlApp = None
			self.fitCaseHtmlPc = None
			self.specialServices = None
			self.multiCateProps = None


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





