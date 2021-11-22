from app.main.stores.jd.api.base import RestApi

class B2bPoPoMidProviderQueryPurOrdersRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.userName = None
			self.companyName = None
			self.issueInvoice = None
			self.submitPoTimeFrom = None
			self.submitPoTimeTo = None
			self.pageSize = None
			self.pageIndex = None
			self.consProvinceId = None
			self.consCityId = None
			self.consCountyId = None
			self.consTownId = None
			self.consName = None
			self.thirdOrderIds = None
			self.thirdPoIds = None
			self.skuIndustryIds = None
			self.poValidStates = None
			self.pins = None
			self.sortTypes = None
			self.skuIndustryTypes = None
			self.popVenderIds = None
			self.paymentTypes = None
			self.poChannels = None
			self.poIds = None
			self.poTiers = None
			self.b2bVenderIds = None
			self.jdOrderIds = None
			self.skuIds = None
			self.poStatuses = None

		def getapiname(self):
			return 'jingdong.b2b.po.PoMidProvider.queryPurOrders'

			





