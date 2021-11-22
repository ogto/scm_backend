from app.main.stores.jd.api.base import RestApi

class EclpSerialQueryPageSerialByBillNoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.billNo = None
			self.billType = None
			self.pageNo = None
			self.pageSize = None
			self.queryType = None

		def getapiname(self):
			return 'jingdong.eclp.serial.queryPageSerialByBillNo'

			





