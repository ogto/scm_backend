from jd.api.base import RestApi

class ErsFangHouseResourceDeleteImgByHouseResourceIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cityCode = None
			self.pSourceId = None

		def getapiname(self):
			return 'jingdong.ers.fang.houseResource.deleteImgByHouseResourceId'

			





