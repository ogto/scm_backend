from app.main.stores.jd.api.base import RestApi

class ClubPopCommentreplySaveRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.commentId = None
			self.content = None
			self.replyId = None

		def getapiname(self):
			return 'jingdong.club.pop.commentreply.save'

			





