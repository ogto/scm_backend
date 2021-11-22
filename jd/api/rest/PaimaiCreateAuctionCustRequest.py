from jd.api.base import RestApi

class PaimaiCreateAuctionCustRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.name = None
			self.categoryId = None
			self.summary = None
			self.thumbTopUrl = None
			self.thumbEntranceUrl = None
			self.auctionCustType = None
			self.auctionForm = None
			self.sortType = None
			self.startTime = None
			self.endTime = None
			self.auctionType = None
			self.paimaiIds = None
			self.exteriorId = None
			self.biddingPeriod = None

		def getapiname(self):
			return 'jingdong.paimai.createAuctionCust'

			





