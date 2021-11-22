from app.main.stores.jd.api.base import RestApi

class NbhouseRentBrokerstaffAddRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.brokerStaffName = None
			self.brokerStaffPhone = None
			self.brokerStaffGender = None
			self.brokerStaffImg = None
			self.brokerStaffIdCardNum = None
			self.brokerStaffIdcardfront = None
			self.brokerStaffIdcardback = None
			self.brokerName = None
			self.extensionPhone = None
			self.businessLicense = None

		def getapiname(self):
			return 'jingdong.nbhouse.rent.brokerstaff.add'

			





