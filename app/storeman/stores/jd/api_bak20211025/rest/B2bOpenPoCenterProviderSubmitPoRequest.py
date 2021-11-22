from app.main.stores.jd.api.base import RestApi

class B2bOpenPoCenterProviderSubmitPoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.op = None
			self.systemSource = None
			self.poReq = None
			self.cartReq = None

		def getapiname(self):
			return 'jingdong.b2b.open.PoCenterProvider.submitPo'

			
	

class Payment(object):
		def __init__(self):
			"""
			"""
			self.paymentType = None
			self.delayPay = None


class Shipment(object):
		def __init__(self):
			"""
			"""
			self.shipmentDate = None
			self.shipmentType = None


class Freight(object):
		def __init__(self):
			"""
			"""
			self.freight = None
			self.jdFreight = None
			self.needValidate = None


class VatInvoice(object):
		def __init__(self):
			"""
			"""
			self.companyName = None
			self.taxpayerIdentity = None
			self.registeredAddress = None
			self.registeredBank = None
			self.registeredBankAccount = None
			self.registeredPhone = None


class InvoiceConsignee(object):
		def __init__(self):
			"""
			"""
			self.name = None
			self.mobile = None
			self.regAddressId = None
			self.provinceId = None
			self.provinceName = None
			self.cityId = None
			self.cityName = None
			self.countyId = None
			self.countyName = None
			self.townId = None
			self.townName = None
			self.address = None


class ElectricInvoice(object):
		def __init__(self):
			"""
			"""
			self.title = None
			self.taxpayerIdentity = None
			self.companyName = None
			self.bookInvoiceContent = None
			self.invoiceContent = None
			self.phone = None
			self.email = None


class Invoice(object):
		def __init__(self):
			"""
			"""
			self.invoiceType = None
			self.putType = None
			self.vatInvoice = None
			self.invoiceConsignee = None
			self.electricInvoice = None


class Consignee(object):
		def __init__(self):
			"""
			"""
			self.name = None
			self.mobile = None
			self.regAddressId = None
			self.provinceId = None
			self.provinceName = None
			self.cityId = None
			self.cityName = None
			self.countyId = None
			self.countyName = None
			self.townId = None
			self.townName = None
			self.address = None
			self.email = None
			self.idCard = None


class PreOccupyRep(object):
		def __init__(self):
			"""
			"""
			self.preOccupy = None


class PoReq(object):
		def __init__(self):
			"""
			"""
			self.thirdOrderId = None
			self.remark = None
			self.payment = None
			self.shipments = None
			self.freight = None
			self.invoice = None
			self.consignee = None
			self.preOccupyRep = None


class Promotion(object):
		def __init__(self):
			"""
			"""
			self.promotionId = None
			self.promotionType = None


class SkuReq(object):
		def __init__(self):
			"""
			"""
			self.skuId = None
			self.num = None
			self.jdPrice = None
			self.price = None
			self.skuType = None
			self.promotion = None
			self.extParam = None
			self.giftItems = None


class SuiteReq(object):
		def __init__(self):
			"""
			"""
			self.suiteId = None
			self.type = None
			self.name = None
			self.num = None
			self.promotion = None
			self.skuItems = None
			self.giftItems = None


class CartReq(object):
		def __init__(self):
			"""
			"""
			self.totalAmount = None
			self.totalPurchaseAmount = None
			self.skuItems = None
			self.suiteItems = None





