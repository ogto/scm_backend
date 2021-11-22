from jd.api.base import RestApi

class DropshipDpsDeliveryAddressServiceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.addressId = None

		def getapiname(self):
			return 'jingdong.dropship.dps.deliveryAddressService'

			





