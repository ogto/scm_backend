from jd.api.base import RestApi

class EclpAfsQueryServiceItemInfoByServiceNoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.servicesNo = None

		def getapiname(self):
			return 'jingdong.eclp.afs.queryServiceItemInfoByServiceNo'

			





