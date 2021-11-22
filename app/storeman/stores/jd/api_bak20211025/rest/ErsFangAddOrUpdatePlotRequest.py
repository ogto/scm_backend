from app.main.stores.jd.api.base import RestApi

class ErsFangAddOrUpdatePlotRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cityCode = None
			self.areaCode = None
			self.sourceId = None
			self.brokerIds = None
			self.plotName = None
			self.plotNickname = None
			self.estateType = None
			self.buildYear = None
			self.volumeRate = None
			self.greenRate = None
			self.estateAmt = None
			self.estateCompany = None
			self.buildCompany = None
			self.tradingAreaId = None
			self.addressDes = None
			self.loopLineId = None
			self.addressLat = None
			self.addressLon = None
			self.buildType = None
			self.estateHeating = None
			self.buildingNum = None
			self.houseNum = None
			self.totalArea = None
			self.plotDes = None
			self.parkingCount = None
			self.parkingRate = None
			self.estateWater = None
			self.estateElectric = None
			self.latLonType = None
			self.extensionField = None
			self.ifUse = None

		def getapiname(self):
			return 'jingdong.ers.fang.addOrUpdatePlot'

			





