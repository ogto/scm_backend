from app.storeman.stores.jd.api.base import RestApi

class WareWriteUpdateWareRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ware = None

		def getapiname(self):
			return 'jingdong.ware.write.updateWare'

			
	

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
			self.featureKey = None
			self.featureValue = None


class Ware(object):
		def __init__(self):
			"""
			"""
			self.wareId = None
			self.title = None
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
			self.shopCategorys = None
			self.mobileDesc = None
			self.zhuangBaId = None
			self.introductionUseFlag = None
			self.mobileZhuangBaId = None
			self.mobileDescUseFlag = None
			self.introduction = None
			self.afterSales = None
			self.jdPrice = None
			self.marketPrice = None
			self.designConcept = None
			self.fitCaseHtmlApp = None
			self.fitCaseHtmlPc = None
			self.multiCateProps = None
			self.specialServices = None





