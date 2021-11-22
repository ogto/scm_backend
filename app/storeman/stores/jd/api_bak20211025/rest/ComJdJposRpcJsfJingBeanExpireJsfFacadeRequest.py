from app.main.stores.jd.api.base import RestApi

class ComJdJposRpcJsfJingBeanExpireJsfFacadeRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pin = None

		def getapiname(self):
			return 'jingdong.com.jd.jpos.rpc.jsf.JingBeanExpireJsfFacade'

			





