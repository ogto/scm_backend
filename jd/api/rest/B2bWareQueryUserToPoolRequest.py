from jd.api.base import RestApi

class B2bWareQueryUserToPoolRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.businessChannel = None
			self.mappingId = None
			self.endModifyTime = None
			self.userToPoolSortField = None
			self.pageSize = None
			self.startCreateTime = None
			self.attributeId = None
			self.mappingLevel = None
			self.startModifyTime = None
			self.b2bMappingId = None
			self.cateType = None
			self.wareMappingType = None
			self.pageNo = None
			self.bizPoolType = None
			self.b2bUserToPoolQueryTypeEnum = None
			self.editor = None
			self.creator = None
			self.totalItem = None
			self.totalPage = None
			self.sortTypeEnum = None
			self.b2bPoolId = None
			self.endCreateTime = None
			self.b2bPoolName = None
			self.lastB2bMappingId = None
			self.cateId = None
			self.mappingType = None
			self.poolGroupId = None
			self.thirdMappingId = None
			self.outerMappingId = None
			self.dataSource = None

		def getapiname(self):
			return 'jingdong.b2b.ware.queryUserToPool'

			





