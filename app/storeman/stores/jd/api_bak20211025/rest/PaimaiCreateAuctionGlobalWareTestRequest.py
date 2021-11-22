from app.main.stores.jd.api.base import RestApi

class PaimaiCreateAuctionGlobalWareTestRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.categoryId = None
			self.bail = None
			self.initialPrice = None
			self.customsBelong = None
			self.commissionRatio = None
			self.name = None
			self.location = None
			self.auctionType = None
			self.auctionWareType = None
			self.sortWeight = None
			self.deliveryType = None
			self.auctionTimes = None
			self.auctionForm = None
			self.consultant = None
			self.consultTel = None
			self.limitPurchase = None
			self.loanSupport = None
			self.mobileDesc = None
			self.PCDesc = None
			self.reservedPrice = None
			self.incrType = None
			self.incrRangeStart = None
			self.incrRangeEnd = None
			self.delayPeriod = None
			self.reservedPriceRequired = None
			self.is7ToReturn = None
			self.isCertificate = None
			self.isAuthorize = None
			self.isOfflinePreviewCheck = None
			self.stockNum = None
			self.notes = None
			self.wareImgs = None
			self.exteriorId = None
			self.evalPrice = None
			self.entrustStartTime = None
			self.entrustEndTime = None
			self.entrustLocation = None
			self.propStr = None
			self.tailOrderPayMode = None
			self.extendParam = None

		def getapiname(self):
			return 'jingdong.paimai.createAuctionGlobalWareTest'

			





