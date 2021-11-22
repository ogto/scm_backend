from app.main.stores.jd.api.base import RestApi

class PopOtoLocorderinfosEngetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.time_type = None
			self.start_date = None
			self.end_date = None
			self.code_status = None
			self.code_type = None
			self.page_index = None
			self.page_size = None

		def getapiname(self):
			return 'jingdong.pop.oto.locorderinfos.enget'

			





