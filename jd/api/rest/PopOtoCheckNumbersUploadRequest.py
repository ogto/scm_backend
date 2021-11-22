from jd.api.base import RestApi

class PopOtoCheckNumbersUploadRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_id = None
			self.card_number = None
			self.pwd_number = None

		def getapiname(self):
			return 'jingdong.pop.oto.checkNumbers.upload'

			





