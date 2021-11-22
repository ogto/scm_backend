from jd.api.base import RestApi

class QueryMetaAttrStoreQualificationListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.param = None

		def getapiname(self):
			return 'jingdong.queryMetaAttrStoreQualificationList'

			





