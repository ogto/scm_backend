from app.main.stores.jd.api.base import RestApi

class QuestionTypeCascadeProviderGetQuestionTypeCascadeRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.parentId = None
			self.wareId = None
			self.afsApplyId = None
			self.operatorPin = None
			self.operatorNick = None
			self.operatorRemark = None
			self.operatorDate = None
			self.platformSrc = None

		def getapiname(self):
			return 'jingdong.QuestionTypeCascadeProvider.getQuestionTypeCascade'

			





