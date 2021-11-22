from jd.api.base import RestApi

class JingyiyueVenderapiUpdateappointtimeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sourceKey = None
			self.appointStartTime = None
			self.appointOrderId = None
			self.venderOrderId = None
			self.appointEndTime = None

		def getapiname(self):
			return 'jingdong.jingyiyue.venderapi.updateappointtime'

			





