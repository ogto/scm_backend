from app.main.stores.jd.api.base import RestApi

class PromoTokenTokenuserDelRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.tokenId = None
			self.userPin = None
			self.secretKey = None
			self.appCode = None
			self.authKey = None
			self.open_id_buyer = None

		def getapiname(self):
			return 'jingdong.promo.token.tokenuser.del'

			





