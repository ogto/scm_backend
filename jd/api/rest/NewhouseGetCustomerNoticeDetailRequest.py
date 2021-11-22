from jd.api.base import RestApi

class NewhouseGetCustomerNoticeDetailRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelId = None
			self.clueId = None

		def getapiname(self):
			return 'jingdong.newhouse.getCustomerNoticeDetail'

			





