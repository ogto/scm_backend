from app.main.stores.jd.api.base import RestApi

class OtsOrderbankExportRestOrderResourceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderType = None
			self.sendPay = None
			self.orderId = None
			self.totalPrice = None
			self.discount = None
			self.yun = None
			self.orderTime = None
			self.payDiscount = None
			self.merchantId = None
			self.parentOrderId = None
			self.appId = None
			self.systemNo = None
			self.orderPrice = None
			self.currency = None
			self.skuId = None
			self.delivery = None
			self.ver = None
			self.payMode = None
			self.appToken = None
			self.otherMoney = None
			self.productCode = None
			self.notePub = None
			self.payEnum = None
			self.payOrderId = None
			self.payTime = None
			self.businessNo = None
			self.payType = None
			self.payMoney = None
			self.payCurrencyName = None
			self.payMerchantId = None
			self.payParentOrderId = None
			self.payAppId = None
			self.paySystemNo = None
			self.payCurrency = None
			self.ext2 = None
			self.ext1 = None
			self.payVer = None
			self.payAppToken = None
			self.dataType = None
			self.noteInner = None
			self.updateTime = None
			self.orderBankNo = None
			self.eventType = None
			self.payTypeName = None
			self.currencyPrice = None
			self.payCreateTime = None
			self.rfIdType = None
			self.morePay = None
			self.payId = None
			self.businessType = None
			self.paidIn = None
			self.orderCode = None
			self.tuotouTime = None
			self.receivableTypeName = None
			self.receAmount = None
			self.receivableId = None
			self.receivableType = None
			self.receCurrencyName = None
			self.receCreateTime = None
			self.receAppToken = None
			self.receAppId = None
			self.receSystemNo = None
			self.receCurrency = None

		def getapiname(self):
			return 'jingdong.ots.orderbank.export.rest.OrderResource'

			





