from app.main.stores.jd.api.base import RestApi

class YunpeiBillStatusQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)

		def getapiname(self):
			return 'jingdong.yunpei.billStatus.query'

			





