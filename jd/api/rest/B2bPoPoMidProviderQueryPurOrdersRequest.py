from jd.api.base import RestApi

class B2bPoPoMidProviderQueryPurOrdersRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
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
			self.OrederId = None
			self.id = None
			self.OrederId1 = None
			self.OrederId2 = None
			self.OrederId3 = None
			self.OrederId4 = None
			self.OrederId5 = None
			self.OrederId6 = None
			self.OrederId7 = None
			self.OrederId8 = None
			self.OrederId9 = None
			self.OrederId10 = None
			self.OrederId11 = None
			self.OrederId12 = None
			self.OrederId13 = None
			self.OrederId14 = None

		def getapiname(self):
			return 'jingdong.b2b.po.PoMidProvider.queryPurOrders'

			





