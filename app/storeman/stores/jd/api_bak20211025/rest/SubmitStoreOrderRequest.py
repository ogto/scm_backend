from app.main.stores.jd.api.base import RestApi

class SubmitStoreOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pin = None
			self.code = None
			self.address = None
			self.provinceId = None
			self.cityId = None
			self.countryId = None
			self.townId = None
			self.receiver = None
			self.mobile = None
			self.email = None
			self.phone = None
			self.totalPrice = None
			self.salesPin = None
			self.storeId = None
			self.remark = None
			self.deliveryType = None
			self.categoryId1 = None
			self.categoryId2 = None
			self.categoryId3 = None
			self.skuId = None
			self.skuName = None
			self.purchaseNum = None
			self.skuPrice = None

		def getapiname(self):
			return 'jingdong.submitStoreOrder'

			





