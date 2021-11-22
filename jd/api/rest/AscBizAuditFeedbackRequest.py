from jd.api.base import RestApi

class AscBizAuditFeedbackRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.waitCustomerFeedbackCmd = None

		def getapiname(self):
			return 'jingdong.asc.biz.audit.feedback'

			
	

class PickVasInfo(object):
		def __init__(self):
			"""
			"""
			self.primaryParam = None
			self.secondaryParam = None
			self.type = None
			self.otherParams = None


class WareDetailInfo(object):
		def __init__(self):
			"""
			"""
			self.wareId = None
			self.wareNum = None
			self.wareName = None
			self.afsApplyDetailId = None
			self.wareType = None
			self.pickWareVASList = None


class OperatorInfoReq(object):
		def __init__(self):
			"""
			"""
			self.operatorPin = None
			self.operatorNick = None
			self.operatorRemark = None
			self.operatorDate = None
			self.platformSrc = None


class QuestionInfo(object):
		def __init__(self):
			"""
			"""
			self.questionReason1 = None
			self.questionReason2 = None
			self.basisId = None
			self.qualitativeId = None


class WaitCustomerFeedbackCmd(object):
		def __init__(self):
			"""
			"""
			self.sysVersion = None
			self.buId = None
			self.callDate = None
			self.reserveDateEnd = None
			self.approveNotes = None
			self.afsServiceId = None
			self.transferFeedbackReason = None
			self.reserveDateBegin = None
			self.customerExpect = None
			self.waitFeedbackLevelOne = None
			self.smsContext = None
			self.customerPhone = None
			self.sendSmsFlag = None
			self.promiseDay = None
			self.sendType = None
			self.wareDetailInfoList = None
			self.operatorInfoReq = None
			self.questionInfo = None





