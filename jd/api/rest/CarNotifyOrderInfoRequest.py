from jd.api.base import RestApi

class CarNotifyOrderInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.Data = None

		def getapiname(self):
			return 'jingdong.car.notifyOrderInfo'

			
	

class Detail(object):
		def __init__(self):
			"""
			"""
			self.DetailEndTime = None
			self.DetailSeviceMoney = None
			self.DetailStartTime = None
			self.ElecPrice = None
			self.DetailPower = None
			self.SevicePrice = None
			self.DetailElecMoney = None


class Data(object):
		def __init__(self):
			"""
			"""
			self.TotalPower = None
			self.StartChargeSeq = None
			self.EndTime = None
			self.TotalSeviceMoney = None
			self.SumPeriod = None
			self.StartTime = None
			self.TotalElecMoney = None
			self.TotalMoney = None
			self.ChargeDetails = None
			self.StopReason = None
			self.ConnectorID = None
			self.TotalOriginalElecMoney = None
			self.TotalOriginalSeviceMoney = None
			self.TotalOriginalMoney = None





