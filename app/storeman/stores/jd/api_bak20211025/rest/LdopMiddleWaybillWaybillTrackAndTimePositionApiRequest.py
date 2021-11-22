from app.main.stores.jd.api.base import RestApi

class LdopMiddleWaybillWaybillTrackAndTimePositionApiRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.waybillCode = None
			self.gpsTime = None
			self.customerCode = None

		def getapiname(self):
			return 'jingdong.ldop.middle.waybill.WaybillTrackAndTimePositionApi'

			





