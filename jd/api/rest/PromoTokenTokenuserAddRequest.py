from jd.api.base import RestApi

class PromoTokenTokenuserAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.tokenId = None
			self.userPin = None
			self.timeStart = None
			self.timeEnd = None
			self.open_id_buyer = None
			self.xid_buyer = None
			self.existUpdate = None
			self.secretKey = None
			self.appCode = None
			self.authKey = None

		def getapiname(self):
			return 'jingdong.promo.token.tokenuser.add'

			





