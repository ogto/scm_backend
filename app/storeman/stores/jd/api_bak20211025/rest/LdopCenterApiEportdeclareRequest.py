from app.main.stores.jd.api.base import RestApi

class LdopCenterApiEportdeclareRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.platformId = None
			self.platformName = None
			self.appType = None
			self.logisticsNo = None
			self.billSerialNo = None
			self.billNo = None
			self.freight = None
			self.insuredFee = None
			self.netWeight = None
			self.weight = None
			self.packNo = None
			self.worth = None
			self.goodsName = None
			self.orderNo = None
			self.shipper = None
			self.shipperAddress = None
			self.shipperTelephone = None
			self.shipperCountry = None
			self.consigneeCountry = None
			self.consigneeProvince = None
			self.consigneeCity = None
			self.consigneeDistrict = None
			self.consingee = None
			self.consigneeAddress = None
			self.consigneeTelephone = None
			self.buyerIdType = None
			self.buyerIdNumber = None
			self.customsId = None
			self.customsCode = None

		def getapiname(self):
			return 'jingdong.ldop.center.storeman.eportdeclare'

			





