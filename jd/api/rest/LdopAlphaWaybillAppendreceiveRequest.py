from jd.api.base import RestApi

class LdopAlphaWaybillAppendreceiveRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.attribute1 = None
			self.parentWaybillCode = None
			self.providerCode = None
			self.signReturn = None
			self.source = None
			self.receiveTimeType = None
			self.vendorCode = None
			self.promiseCompleteTime = None
			self.payType = None
			self.needGuarantee = None
			self.pin = None
			self.appKey = None
			self.goodsName = None
			self.thirdSectionCode = None
			self.height = None
			self.expressType = None
			self.weight = None
			self.vendorName = None
			self.branchCode = None
			self.volume = None
			self.guaranteeMoney = None
			self.transType = None
			self.vendorOrderCode = None
			self.remark = None
			self.idNumber = None
			self.warehouseCode = None
			self.expressPayMethod = None
			self.waybillType = None
			self.salePlatform = None
			self.addedService = None
			self.providerId = None
			self.secondSectionCode = None
			self.length = None
			self.waybillCount = None
			self.pickUpStartTime = None
			self.promiseTimeType = None
			self.settlementCode = None
			self.shouldPayMoney = None
			self.goodsMoney = None
			self.createTime = None
			self.platformOrderNo = None
			self.coldChainType = None
			self.pickUpEndTime = None
			self.width = None
			self.fromProvinceId = None
			self.fromProvinceName = None
			self.fromCityId = None
			self.fromCityName = None
			self.fromCountryId = None
			self.fromCountryName = None
			self.fromCountrysideId = None
			self.fromCountrysideName = None
			self.fromAddressDetail = None
			self.fromContact = None
			self.fromPhone = None
			self.fromMobile = None
			self.toProvinceId = None
			self.toProvinceName = None
			self.toCityId = None
			self.toCityName = None
			self.toCountryId = None
			self.toCountryName = None
			self.toCountrysideId = None
			self.toCountrysideName = None
			self.toAddressDetail = None
			self.toContact = None
			self.toPhone = None
			self.toMobile = None

		def getapiname(self):
			return 'jingdong.ldop.alpha.waybill.appendreceive'

			





