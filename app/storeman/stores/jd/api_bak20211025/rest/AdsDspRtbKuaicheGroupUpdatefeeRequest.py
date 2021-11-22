from app.main.stores.jd.api.base import RestApi

class AdsDspRtbKuaicheGroupUpdatefeeRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None
			self.mobilePriceCoef = None
			self.inSearchFee = None
			self.recommendFee = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.group.updatefee'

			





