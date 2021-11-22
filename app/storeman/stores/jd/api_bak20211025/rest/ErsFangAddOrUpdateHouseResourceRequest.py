from app.main.stores.jd.api.base import RestApi

class ErsFangAddOrUpdateHouseResourceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelId = None
			self.plotId = None
			self.number = None
			self.title = None
			self.labels = None
			self.estateType = None
			self.room = None
			self.hall = None
			self.toilet = None
			self.kitchen = None
			self.downPayment = None
			self.structureArea = None
			self.usableArea = None
			self.orientation = None
			self.fitmentType = None
			self.buildYear = None
			self.totalFloor = None
			self.locationFloor = None
			self.floorLabel = None
			self.recordNumber = None
			self.housePutawayTime = None
			self.houseUpdateTime = None
			self.houseStatus = None
			self.houseTerm = None
			self.propertyYear = None
			self.tradeAffiliation = None
			self.cityCode = None
			self.sourceId = None
			self.storeId = None

		def getapiname(self):
			return 'jingdong.ers.fang.addOrUpdateHouseResource'

			





