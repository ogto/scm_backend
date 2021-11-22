from app.main.stores.jd.api.base import RestApi

class NewWareVenderSkusQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.index = None

		def getapiname(self):
			return 'jingdong.new.ware.vender.skus.query'

			





