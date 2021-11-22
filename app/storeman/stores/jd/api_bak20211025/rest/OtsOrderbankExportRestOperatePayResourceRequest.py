from app.main.stores.jd.api.base import RestApi

class OtsOrderbankExportRestOperatePayResourceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.notePub = None
			self.payEnum = None
			self.orderId = None
			self.payTime = None
			self.oper = None
			self.businessNo = None
			self.payType = None
			self.payMoney = None
			self.currencyName = None
			self.merchantId = None
			self.parentOrderId = None
			self.appId = None
			self.currency = None
			self.ext2 = None
			self.ext1 = None
			self.ver = None
			self.appToken = None
			self.dataType = None
			self.noteInner = None
			self.updateTime = None
			self.eventType = None
			self.payTypeName = None
			self.currencyPrice = None
			self.createTime = None
			self.rfIdType = None
			self.payId = None
			self.businessType = None

		def getapiname(self):
			return 'jingdong.ots.orderbank.export.rest.OperatePayResource'

			





