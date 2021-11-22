from jd.api.base import RestApi

class ErsFangAddOrUpdateDescribeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelId = None
			self.content = None
			self.publishDate = None
			self.sourceUrl = None
			self.cityCode = None
			self.sourceId = None
			self.pSourceId = None

		def getapiname(self):
			return 'jingdong.ers.fang.addOrUpdateDescribe'

			





