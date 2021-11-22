from jd.api.base import RestApi

class AscBizAuditRefuseRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.RefuseServiceCmd = None

		def getapiname(self):
			return 'jingdong.asc.biz.audit.refuse'

			
	

class WareDetailInfo(object):
		def __init__(self):
			"""
			"""
			self.wareId = None
			self.wareNum = None
			self.wareName = None
			self.afsApplyDetailId = None
			self.wareType = None


class OperatorInfoReq(object):
		def __init__(self):
			"""
			"""
			self.operatorPin = None
			self.operatorNick = None
			self.operatorRemark = None
			self.operatorDate = None
			self.platformSrc = None


class RefuseServiceCmd(object):
		def __init__(self):
			"""
			"""
			self.buId = None
			self.questionTypeCid2 = None
			self.questionTypeCid1 = None
			self.approveNotes = None
			self.afsServiceId = None
			self.remark = None
			self.refuseReasonName = None
			self.sendSmsFlag = None
			self.auditBasisId = None
			self.closeDetailInfo = None
			self.refuseReason = None
			self.operatorInfoReq = None





