from app.main.stores.jd.api.base import RestApi

class LogisticsO2oOrderQueryAfsRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.station_no = None
			self.order_id = None
			self.customer_order_id = None
			self.customer_order_state = None
			self.customer_order_time_start = None
			self.customer_order_time_end = None
			self.customer_order_update_time_start = None
			self.customer_order_update_time_end = None
			self.current_page = None
			self.page_num = None

		def getapiname(self):
			return 'jingdong.logistics.o2o.order.queryAfs'

			





