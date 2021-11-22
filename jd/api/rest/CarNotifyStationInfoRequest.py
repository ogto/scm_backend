from jd.api.base import RestApi

class CarNotifyStationInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.Data = None

		def getapiname(self):
			return 'jingdong.car.notifyStationInfo'

			
	

class ChargeConnectorInfoVO(object):
		def __init__(self):
			"""
			"""
			self.VoltageLowerLimits = None
			self.ConnectorType = None
			self.VoltageUpperLimits = None
			self.NationalStandard = None
			self.ConnectorName = None
			self.ParkNo = None
			self.Current = None
			self.power = None
			self.ConnectorID = None


class ChargeEquipmentInfoVO(object):
		def __init__(self):
			"""
			"""
			self.EquipmentID = None
			self.ManufacturerID = None
			self.EquipmentLng = None
			self.ConnectorInfos = None
			self.EquipmentName = None
			self.EquipmentModel = None
			self.ProductionDate = None
			self.EquipmentType = None
			self.EquipmentLat = None
			self.Power = None


class ChargeStationsInfoVO(object):
		def __init__(self):
			"""
			"""
			self.Pictures = None
			self.StationLng = None
			self.SiteGuide = None
			self.Address = None
			self.ServiceTel = None
			self.SupportOrder = None
			self.OperatorID = None
			self.StationID = None
			self.StationRemark = None
			self.Remark = None
			self.StationName = None
			self.EquipmentRemark = None
			self.StationTel = None
			self.StationLat = None
			self.StationStatus = None
			self.CountryCode = None
			self.StationType = None
			self.EquipmentOwnerID = None
			self.Construction = None
			self.MatchCars = None
			self.ParkFee = None
			self.ParkInfo = None
			self.ServiceFee = None
			self.Payment = None
			self.ElectricityFee = None
			self.ConnectorRemark = None
			self.AreaCode = None
			self.EquipmentInfos = None
			self.ParkNums = None
			self.BusineHours = None


class Data(object):
		def __init__(self):
			"""
			"""
			self.StationInfos = None





