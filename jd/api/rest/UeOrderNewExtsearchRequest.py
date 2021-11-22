from jd.api.base import RestApi

class UeOrderNewExtsearchRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pageSize = None
			self.venderCode = None
			self.appid = None
			self.page = None

		def getapiname(self):
			return 'jingdong.ue.order.new.extsearch'

			





