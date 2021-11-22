from app.main.stores.jd.api.base import RestApi

class VcGetrequisitiondetailbywareidRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ware_id = None
			self.deliver_center_id = None

		def getapiname(self):
			return 'jingdong.vc.getrequisitiondetailbywareid'

			





