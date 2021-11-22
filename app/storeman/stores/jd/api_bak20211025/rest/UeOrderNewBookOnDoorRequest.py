from app.main.stores.jd.api.base import RestApi

class UeOrderNewBookOnDoorRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNo = None
			self.bookOperateDate = None
			self.bookDate = None
			self.bookTimes = None
			self.createBy = None
			self.appid = None
			self.venderCode = None
			self.bookingStartDate = None
			self.bookingEndDate = None
			self.remark = None

		def getapiname(self):
			return 'jingdong.ue.order.new.bookOnDoor'

			





