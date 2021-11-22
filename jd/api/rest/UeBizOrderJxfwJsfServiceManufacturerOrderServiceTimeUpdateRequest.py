from jd.api.base import RestApi

class UeBizOrderJxfwJsfServiceManufacturerOrderServiceTimeUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNo = None
			self.bookStartTime = None
			self.bookEndTime = None
			self.appId = None
			self.bookOperateDate = None
			self.remark = None
			self.bookBy = None
			self.type = None

		def getapiname(self):
			return 'jingdong.ue.bizOrderJxfwJsfService.manufacturerOrderServiceTimeUpdate'

			





