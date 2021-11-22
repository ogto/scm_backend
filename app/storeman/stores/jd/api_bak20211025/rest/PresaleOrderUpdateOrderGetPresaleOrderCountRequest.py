from app.main.stores.jd.api.base import RestApi

class PresaleOrderUpdateOrderGetPresaleOrderCountRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.userPin = None
			self.orderId = None
			self.orderStatusItem = None
			self.startTime = None
			self.endTime = None
			self.skuID = None
			self.open_id_buyer = None

		def getapiname(self):
			return 'jingdong.presale.order.updateOrder.getPresaleOrderCount'

			





