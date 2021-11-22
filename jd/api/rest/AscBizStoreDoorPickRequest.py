from jd.api.base import RestApi

class AscBizStoreDoorPickRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.StoreDoorPickApplyCmd = None

		def getapiname(self):
			return 'jingdong.asc.biz.storeDoorPick'

			
	

class WareDetailInfo(object):
		def __init__(self):
			"""
			"""
			self.wareId = None
			self.wareNum = None
			self.wareName = None
			self.afsApplyDetailId = None
			self.wareType = None


class OperatorInfoReq(object):
		def __init__(self):
			"""
			"""
			self.operatorPin = None
			self.platformSrc = None
			self.operatorNick = None
			self.operatorRemark = None
			self.operatorDate = None


class AddressInfo(object):
		def __init__(self):
			"""
			"""
			self.province = None
			self.city = None
			self.county = None
			self.village = None
			self.detailAddress = None
			self.lng = None
			self.lat = None
			self.returnAddressType = None


class PickWareContactInfo(object):
		def __init__(self):
			"""
			"""
			self.contactsName = None
			self.contactsTel = None
			self.contactsZipCode = None
			self.addressInfo = None


class AuditAddInfo(object):
		def __init__(self):
			"""
			"""
			self.pickwareType = None
			self.approveNotes = None
			self.pickWareNotes = None
			self.companyId = None
			self.auditType = None
			self.pickwareMethod = None
			self.afterServiceType = None
			self.customizedSmsType = None
			self.customerExpect = None


class AppointmentInfo(object):
		def __init__(self):
			"""
			"""
			self.appointDateBegin = None
			self.appointDateEnd = None
			self.appointDateStr = None
			self.appointDateType = None
			self.reserveDate = None
			self.reserveType = None
			self.appointRenewDate = None
			self.appointRenewRange = None


class AddressInfo1(object):
		def __init__(self):
			"""
			"""
			self.province1 = None
			self.city1 = None
			self.county1 = None
			self.village1 = None
			self.detailAddress1 = None
			self.lng1 = None
			self.lat1 = None
			self.returnAddressType1 = None


class ShopContactInfo(object):
		def __init__(self):
			"""
			"""
			self.contactsName1 = None
			self.contactsTel1 = None
			self.contactsZipCode1 = None
			self.addressInfo1 = None


class StoreDoorPickApplyCmd(object):
		def __init__(self):
			"""
			"""
			self.buId = None
			self.afsServiceId = None
			self.returnWareDetailInfo = None
			self.operatorInfoReq = None
			self.pickWareContactInfo = None
			self.auditAddInfo = None
			self.appointmentInfo = None
			self.shopContactInfo = None





