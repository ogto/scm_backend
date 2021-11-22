from jd.api.base import RestApi

class ErsFangAddDealAverageRecordRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cityCode = None
			self.sourceId = None
			self.pSourceId = None
			self.externalPlotName = None
			self.totalRate = None
			self.unitRate = None
			self.houseArea = None
			self.houseRoom = None
			self.houseHall = None
			self.finishTime = None
			self.externalChannelId = None
			self.externalChannelName = None
			self.externalBrokerId = None
			self.externalBrokerName = None

		def getapiname(self):
			return 'jingdong.ers.fang.addDealAverageRecord'

			





