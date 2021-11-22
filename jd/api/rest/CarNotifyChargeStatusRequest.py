from jd.api.base import RestApi

class CarNotifyChargeStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.Data = None

		def getapiname(self):
			return 'jingdong.car.notifyChargeStatus'

			
	

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
			self.SeviceMoney = None
			self.EndTime = None
			self.SumPeriod = None
			self.Soc = None
			self.ConnectorStatus = None
			self.StartTime = None
			self.CurrentC = None
			self.ChargeDetails = None
			self.CurrentA = None
			self.CurrentB = None
			self.VoltageB = None
			self.TotalPower = None
			self.StartChargeSeq = None
			self.VoltageC = None
			self.StartChargeSeqStat = None
			self.VoltageA = None
			self.TotalMoney = None
			self.ElecMoney = None
			self.ConnectorID = None





