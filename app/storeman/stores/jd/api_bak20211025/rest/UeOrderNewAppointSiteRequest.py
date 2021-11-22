from app.main.stores.jd.api.base import RestApi

class UeOrderNewAppointSiteRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.county = None
			self.source = None
			self.deliverCompany = None
			self.deliverArriveDate = None
			self.province = None
			self.assessValue = None
			self.orderNo = None
			self.town = None
			self.level = None
			self.newPartPrice = None
			self.newPartQty = None
			self.barcode2 = None
			self.barcode1 = None
			self.appointTimes = None
			self.engineerCode = None
			self.partStat = None
			self.failureReason = None
			self.bookOperateDate = None
			self.oldPartQty = None
			self.uniqueId = None
			self.oldPartCode = None
			self.bookDate = None
			self.city = None
			self.deliverNo = None
			self.siteName = None
			self.remark = None
			self.contactMan = None
			self.failureName = None
			self.bookTimes = None
			self.engineerName = None
			self.pic1 = None
			self.assessItem = None
			self.venderCode = None
			self.siteMobile = None
			self.processType = None
			self.pic2 = None
			self.pic3 = None
			self.engineerMobile = None
			self.dealRemark = None
			self.pic4 = None
			self.fixMethod = None
			self.siteCode = None
			self.address = None
			self.newPartName = None
			self.oldPartName = None
			self.cancleReason = None
			self.createBy = None
			self.newPartCode = None
			self.appid = None
			self.dealResult = None
			self.settleCode = None
			self.pid = None
			self.sitePhoto = None
			self.insuranceNo = None
			self.insurancePhoto = None
			self.engineerPhoto = None
			self.siteAcceptDate = None
			self.unifiedCode = None
			self.personName = None
			self.personMobile = None
			self.personPib = None
			self.accountName = None
			self.bankCode = None
			self.bankName = None
			self.dutyParagraph = None
			self.bankAccount = None

		def getapiname(self):
			return 'jingdong.ue.order.new.appointSite'

			





