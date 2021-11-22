from jd.api.base import RestApi

class StationinfojosserviceGetStationInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.companyCode = None
			self.stationCode = None
			self.stationName = None
			self.stationAddress = None
			self.provinceId = None
			self.cityId = None
			self.countyId = None
			self.townId = None

		def getapiname(self):
			return 'jingdong.stationinfojosservice.getStationInfo'

			





