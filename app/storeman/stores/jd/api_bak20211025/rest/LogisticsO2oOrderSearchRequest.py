from app.main.stores.jd.api.base import RestApi

class LogisticsO2oOrderSearchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.station_no = None
			self.order_id = None
			self.order_state = None
			self.order_time_start = None
			self.order_time_end = None
			self.order_update_time_start = None
			self.order_update_time_end = None
			self.current_page = None

		def getapiname(self):
			return 'jingdong.logistics.o2o.order.search'

			





