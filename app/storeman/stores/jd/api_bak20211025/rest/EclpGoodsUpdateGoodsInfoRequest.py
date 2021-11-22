from app.main.stores.jd.api.base import RestApi

class EclpGoodsUpdateGoodsInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.goodsNo = None
			self.spGoodsNo = None
			self.barcodes = None
			self.abbreviation = None
			self.brandNo = None
			self.brandName = None
			self.manufacturer = None
			self.produceAddress = None
			self.standard = None
			self.color = None
			self.size = None
			self.sizeDefinition = None
			self.grossWeight = None
			self.netWeight = None
			self.length = None
			self.width = None
			self.height = None
			self.batch = None
			self.cheapGift = None
			self.quality = None
			self.expensive = None
			self.luxury = None
			self.breakable = None
			self.liquid = None
			self.consumables = None
			self.abnormal = None
			self.imported = None
			self.health = None
			self.temperature = None
			self.temperatureCeil = None
			self.temperatureFloor = None
			self.humidity = None
			self.humidityCeil = None
			self.humidityFloor = None
			self.movable = None
			self.service3g = None
			self.sample = None
			self.odor = None
			self.sex = None
			self.precious = None
			self.mixedBatch = None
			self.reserve1 = None
			self.reserve2 = None
			self.reserve3 = None
			self.reserve4 = None
			self.reserve5 = None
			self.reserve6 = None
			self.reserve7 = None
			self.reserve8 = None
			self.reserve9 = None
			self.reserve10 = None
			self.fashionNo = None
			self.goodsMess = None
			self.isvGoodsNo = None
			self.deptNo = None
			self.signType = None
			self.overseaPurchase = None
			self.qiRecord = None
			self.customRecord = None
			self.pattern = None
			self.ccProvider = None
			self.bondedArea = None
			self.sellerRecord = None
			self.batAttrIds = None
			self.needJDRecord = None
			self.modelNumber = None
			self.spe = None
			self.vatRate = None
			self.taxRate = None
			self.taxNumberPost = None
			self.postRate = None
			self.hsCode = None
			self.country = None
			self.qiCountry = None
			self.flag = None
			self.legalUnit1 = None
			self.legalAmount1 = None
			self.legalUnit2 = None
			self.legalAmount2 = None
			self.measurement = None
			self.qiMeasurement = None
			self.delivery = None
			self.storeProperty = None
			self.productCategory = None
			self.category = None
			self.approvalNo = None
			self.storage = None
			self.form = None
			self.type = None
			self.specification = None
			self.genericName = None
			self.dosage = None
			self.useMethods = None
			self.packingUnit = None
			self.efficacy = None
			self.manufactory = None
			self.price = None
			self.storeSaleFlag = None
			self.keyMaintenance = None
			self.specialDrugs = None
			self.marketingAuthorizationHolder = None
			self.boxRule = None
			self.warningDay = None
			self.regularAdventDay = None
			self.urgentAdventDay = None
			self.adventDay = None
			self.easyPollute = None
			self.muslim = None
			self.boxRegulations = None
			self.allowedDay = None
			self.sellerFirstCategory = None
			self.sellerSecondCategory = None
			self.sellerThirdCategory = None
			self.sellerFirstCategoryNo = None
			self.sellerSecondCategoryNo = None
			self.sellerThirdCategoryNo = None
			self.athletesUseCaution = None
			self.elecSupervisionCodeFlag = None
			self.hgsbys = None
			self.goodsUnit = None
			self.uniqueCode = None
			self.productLine = None
			self.isStandardInstrument = None
			self.isColdChain = None
			self.isDetachablePackage = None
			self.certificateNo = None
			self.businessTypeName = None
			self.ownerTypeName = None
			self.packageTypeName = None
			self.materialTypeName = None
			self.model = None
			self.clothingAttr = None
			self.clothingStyle = None
			self.clothingVersionType = None
			self.clothingSilhouette = None
			self.clothingThickness = None
			self.clothingWeek = None
			self.bodyParts = None
			self.styleSex = None
			self.listedBand = None
			self.expectListedTime = None
			self.fabric = None
			self.washing = None
			self.year = None
			self.productSeason = None
			self.afterSaleFlag = None
			self.productionLicenseNo = None
			self.transportTemperature = None
			self.boxUniqueCode = None
			self.auxiliary = None
			self.goodsNameEn = None
			self.minSaleQuantity = None
			self.minPackageQuantity = None
			self.packageInstruction = None
			self.texture = None
			self.substrate = None
			self.executiveStandard = None
			self.processTechnology = None
			self.allSerial = None
			self.isRcvDate = None
			self.renewPackage = None

		def getapiname(self):
			return 'jingdong.eclp.goods.updateGoodsInfo'

			





