from jd.api.base import RestApi

class CreateEntityStoreRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.name = None
			self.addCode = None
			self.addName = None
			self.coordinate = None
			self.phone = None
			self.item = None
			self.customerId = None
			self.categoryName = None
			self.extendJson = None
			self.imageFile = None
			self.addCode4 = None
			self.mobile = None
			self.categoryId2 = None
			self.slogan = None
			self.qualificationId = None
			self.startingTime = None
			self.endingTime = None
			self.imgUrl = None
			self.isPermanent = None

		def getapiname(self):
			return 'jingdong.createEntityStore'

			





