from app import db, flask_bcrypt


class HDProduct(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "scm_hd_product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    slitmCd = db.Column(db.String(10))
    sitmCd = db.Column(db.String(10))
    bsitmCd = db.Column(db.String(10))
    slitmNm = db.Column(db.String(100))
    baseCmpsItemNm = db.Column(db.String(100))
    addCmpsItemNm = db.Column(db.String(100))
    engItemNm = db.Column(db.String(100))
    itemUrl = db.Column(db.String(255))
    itemLCsfCd = db.Column(db.String(10))
    itemMCsfCd = db.Column(db.String(10))
    itemSCsfCd = db.Column(db.String(10))
    itemDCsfCd = db.Column(db.String(10))
    itemLCsfNm = db.Column(db.String(100))
    itemMCsfNm = db.Column(db.String(100))
    itemSCsfNm = db.Column(db.String(100))
    itemDCsfNm = db.Column(db.String(100))
    venItemCd = db.Column(db.String(10))
    afcrItemCd = db.Column(db.String(10))
    mkcoGbcd = db.Column(db.String(10))
    mkcoCd = db.Column(db.String(10))
    mkcoNm = db.Column(db.String(100))
    mkcoCnryGbcd = db.Column(db.String(10))
    mkcoCnryNm = db.Column(db.String(100))
    mkcoCsfGbcd = db.Column(db.String(10))
    octyCnryGbcd = db.Column(db.String(10))
    octyCnryNm = db.Column(db.String(100))
    prmrOrgCnryGbcd = db.Column(db.String(10))
    prmrOrgCnryNm = db.Column(db.String(100))
    prmrOrgNm = db.Column(db.String(100))
    itemMemo = db.Column(db.TEXT)
    asGdCntn = db.Column(db.TEXT)
    itemWgt = db.Column(db.DECIMAL(12, 2))
    itemWdthLen = db.Column(db.Integer)
    itemHghtLen = db.Column(db.Integer)
    itemHghLen = db.Column(db.Integer)
    itemAthzGbcd = db.Column(db.String(10))
    itemAthzGbcdNm = db.Column(db.String(100))
    itemGbcd = db.Column(db.String(10))
    itemSellGbcd = db.Column(db.String(10))
    itemSellGbcdNm = db.Column(db.String(100))
    itemBaseImgNm = db.Column(db.String(100))
    nchgStlmItemYn = db.Column(db.String(1))
    rntlItemYn = db.Column(db.String(1))
    adltItemYn = db.Column(db.String(1))
    itemRegTcndAgrYn = db.Column(db.String(1))
    cmisGbcd = db.Column(db.String(10))
    jwlSvrtEnclYn = db.Column(db.String(1))
    rsptUserId = db.Column(db.String(10))
    rsptUserNm = db.Column(db.String(100))
    baseSectId = db.Column(db.String(10))
    baseSectNm = db.Column(db.String(100))
    spexSectId = db.Column(db.String(10))
    spexSectNm = db.Column(db.String(100))
    giftEvntStrtDtm = db.Column(db.DATETIME)
    giftEvntStrtDt = db.Column(db.String(8))
    giftEvntStrtTime = db.Column(db.String(8))
    giftEvntEndDtm = db.Column(db.DATETIME)
    giftEvntEndDt = db.Column(db.String(8))
    giftEvntEndTime = db.Column(db.String(8))
    giftCntn = db.Column(db.TEXT)
    giftImgNm = db.Column(db.String(100))
    giftWtdwMndrYn = db.Column(db.String(1))
    giftUprc = db.Column(db.String(100))
    pgmCmisSlitmCd = db.Column(db.String(10))
    sincMkcoCd = db.Column(db.String(10))
    sincMkcoNm = db.Column(db.String(100))
    slacMkcoCd = db.Column(db.String(10))
    slacMkcoNm = db.Column(db.String(100))
    prchVenMkcoCd = db.Column(db.String(10))
    prchVenMkcoNm = db.Column(db.String(100))
    phdsPrxyMkcoCd = db.Column(db.String(10))
    phdsPrxyMkcoNm = db.Column(db.String(100))
    alliCrdDcYn = db.Column(db.String(1))
    empDcYn = db.Column(db.String(1))
    itntAddSvmtYn = db.Column(db.String(1))
    stckGdYn = db.Column(db.String(1))
    hmallRsvSellYn = db.Column(db.String(1))
    frgnBuyPrxyYn = db.Column(db.String(1))
    frdlvCost = db.Column(db.DECIMAL(12, 2))
    basktUseNdmtYn = db.Column(db.String(1))
    prsnMsgPossYn = db.Column(db.String(1))
    prsnPackPossYn = db.Column(db.String(1))
    stckMngUnitGbcd = db.Column(db.String(10))
    addBuyOptUseYn = db.Column(db.String(1))
    venCd = db.Column(db.String(10))
    venNm = db.Column(db.String(100))
    hdptYn = db.Column(db.String(1))
    cmisYn = db.Column(db.String(1))
    vtltStatGbcd = db.Column(db.String(10))
    dptsBrnCd = db.Column(db.String(10))
    virtDptsYn = db.Column(db.String(1))
    hitemHndlYn = db.Column(db.String(1))
    ven2Cd = db.Column(db.String(10))
    ven2Nm = db.Column(db.String(100))
    oshpVenAdrSeq = db.Column(db.Integer)
    oshpVenPostNo = db.Column(db.String(10))
    oshpVenAdr = db.Column(db.String(255))
    rtpExchVenAdrSeq = db.Column(db.Integer)
    rtpExchVenPostNo = db.Column(db.String(6))
    rtpExchVenAdr = db.Column(db.String(255))
    emgyExchVenAdrSeq = db.Column(db.Integer)
    emgyExchVenPostNo = db.Column(db.String(6))
    emgyExchVenAdr = db.Column(db.String(255))
    itntDispYn = db.Column(db.String(1))
    itntDispStrtDtm = db.Column(db.DATETIME)
    itntDispStrtDt = db.Column(db.String(8))
    itntDispStrtTime = db.Column(db.String(8))
    itntDispEndDtm = db.Column(db.DATETIME)
    itntDispEndDt = db.Column(db.String(8))
    itntDispEndTime = db.Column(db.String(8))
    gnrlCopnUseYn = db.Column(db.String(1))
    useCopnExpsYn = db.Column(db.String(1))
    itemQnaExpsYn = db.Column(db.String(1))
    bbprcCopnDcYn = db.Column(db.String(1))
    bbprcSpymDcYn = db.Column(db.String(1))
    bbprcSpdcYn = db.Column(db.String(1))
    bbprcSvmtPrdcYn = db.Column(db.String(1))
    prcExpsBitVal = db.Column(db.String(255))
    prcExpsBitVal1 = db.Column(db.String(255))
    prcExpsBitVal2 = db.Column(db.String(255))
    prcExpsBitVal4 = db.Column(db.String(255))
    prcExpsBitVal8 = db.Column(db.String(255))
    webExpsPrmoNm = db.Column(db.String(255))
    prmo1TxtCntn = db.Column(db.TEXT)
    prmo2TxtCntn = db.Column(db.TEXT)
    prmoTxtDcCopnYn = db.Column(db.String(1))
    prmoTxtSpdcYn = db.Column(db.String(1))
    prmoTxtSvmtYn = db.Column(db.String(1))
    prmoTxtFamtFxrtGbcd = db.Column(db.String(10))
    prmoTxtSvmtPrdcYn = db.Column(db.String(1))
    prmoTxtWintYn = db.Column(db.String(1))
    prmoTxtSpymDcYn = db.Column(db.String(1))
    prmoExpsStrtDtm = db.Column(db.DATETIME)
    prmoExpsStrtDt = db.Column(db.String(8))
    prmoExpsStrtTime = db.Column(db.String(8))
    prmoExpsEndDtm = db.Column(db.DATETIME)
    prmoExpsEndDt = db.Column(db.String(8))
    prmoExpsEndTime = db.Column(db.String(8))
    frdlvYn = db.Column(db.String(1))
    packOpenRtpNdmtYn = db.Column(db.String(1))
    mdRcmmYn = db.Column(db.String(1))
    ostkYn = db.Column(db.String(1))
    dlvHopeDtDsntYn = db.Column(db.String(1))
    trndhHitTagExpsYn = db.Column(db.String(1))
    trndhSsaleTagExpsYn = db.Column(db.String(1))
    trndhExclTagExpsYn = db.Column(db.String(1))
    itstHtmlYn = db.Column(db.String(1))
    htmlGnrlItstSmexYn = db.Column(db.String(1))
    itstPhotoExpsYn = db.Column(db.String(1))
    dlvItemFormGbcd = db.Column(db.String(10))
    qckDlvPossYn = db.Column(db.String(1))
    lrpyYn = db.Column(db.String(1))
    sameItemMxpkPossQty = db.Column(db.Integer)
    mxpkYn = db.Column(db.String(1))
    packMagnGbcd = db.Column(db.String(10))
    dlvcGbcd = db.Column(db.String(10))
    dlvcPayGbcd = db.Column(db.String(10))
    dlvcPayGbcdNm = db.Column(db.String(100))
    inslItemYn = db.Column(db.String(1))
    arpayDlvGdCntn = db.Column(db.TEXT)
    osbd = db.Column(db.Integer)
    cvstWtdwPossYn = db.Column(db.String(1))
    prpyDlvCost = db.Column(db.DECIMAL(12, 2))
    irgnAreaAddDlvCost = db.Column(db.DECIMAL(12, 2))
    shipInstStopYn = db.Column(db.String(1))
    dlvBoxCmpsQty = db.Column(db.Integer)
    dsrvDlvcoCd = db.Column(db.String(10))
    mngWhNo = db.Column(db.String(10))
    sbctDlvcoCd = db.Column(db.String(10))
    dlvMagnGbcd = db.Column(db.String(10))
    dlvcChmgGbcd = db.Column(db.String(10))
    dlvFormGbcd = db.Column(db.String(10))
    dlvFormGbcdNm = db.Column(db.String(100))
    rtpPossYn = db.Column(db.String(1))
    rtpWdmtGbcd = db.Column(db.String(10))
    rtpDlvCost = db.Column(db.DECIMAL(12, 2))
    exchPossYn = db.Column(db.String(1))
    exchWdmtGbcd = db.Column(db.String(10))
    exchDlvCost = db.Column(db.DECIMAL(12, 2))
    custDlvcWdmtGbcd = db.Column(db.String(10))
    satOffdYn = db.Column(db.String(1))
    ordMakeYn = db.Column(db.String(1))
    ordUnitMaxOrdQty = db.Column(db.Integer)
    stlmWayScopGbcd = db.Column(db.String(10))
    pntStlmNdmtYn = db.Column(db.String(1))
    cmpsOrdQtyGbcd = db.Column(db.String(10))
    enlgSrchTagNm = db.Column(db.String(100))
    prcsExpsExcldYn = db.Column(db.String(1))
    hmallItemSrchExcldYn = db.Column(db.String(1))
    niamtSmsExcldYn = db.Column(db.String(1))
    ostkRishpSmsYn = db.Column(db.String(1))
    oshpSmsExcldYn = db.Column(db.String(1))
    itemImgRtntGbcd = db.Column(db.String(10))
    flashFileNm = db.Column(db.String(100))
    vodFileNm = db.Column(db.String(100))
    slitmAprvlGbcd = db.Column(db.String(10))
    slitmAprvlGbcdNm = db.Column(db.String(100))
    itemQaRstGbcd = db.Column(db.String(10))
    itemQaRstGbcdNm = db.Column(db.String(100))
    askCntn = db.Column(db.TEXT)
    qaRstCntn = db.Column(db.TEXT)
    hmallDlbrStatGbcd = db.Column(db.String(10))
    hmallDlbrStatGbcdNm = db.Column(db.String(100))
    mrgnRateJdgmGbcd = db.Column(db.String(10))
    mrgnRateJdgmGbcdNm = db.Column(db.String(100))
    taxnJdgmYn = db.Column(db.String(1))
    mrgnJdgmCmptYn = db.Column(db.String(1))
    itntSaleYn = db.Column(db.String(1))
    blcwdItemYn = db.Column(db.String(1))
    clhItemNm = db.Column(db.String(100))
    clhStrtDtm = db.Column(db.DATETIME)
    clhStrtDt = db.Column(db.String(8))
    clhStrtTime = db.Column(db.String(8))
    clhEndDtm = db.Column(db.DATETIME)
    clhEndDt = db.Column(db.String(8))
    clhEndTime = db.Column(db.String(8))
    clhMaxQty = db.Column(db.Integer)
    clhMinQty = db.Column(db.Integer)
    itemPackSize = db.Column(db.Integer)
    addDlvCost = db.Column(db.DECIMAL(12, 2))
    bsitmRepYn = db.Column(db.String(1))
    giftItemYn = db.Column(db.String(1))
    frchPrchYn = db.Column(db.String(1))
    bsitmNm = db.Column(db.String(100))
    itemTypeGbcd = db.Column(db.String(10))
    intgItemGbcd = db.Column(db.String(10))
    frstRegMdaGbcd = db.Column(db.String(10))
    prchMdaGbcd = db.Column(db.String(10))
    vatRate = db.Column(db.DECIMAL(12, 2))
    itemTaxnYn = db.Column(db.String(1))
    prchMthdGbcd = db.Column(db.String(10))
    itemTaxnGbcd = db.Column(db.String(10))
    ringItemYn = db.Column(db.String(1))
    brndCd = db.Column(db.String(10))
    brndNm = db.Column(db.String(100))
    itntBrndNm = db.Column(db.String(100))
    dptsPchCd = db.Column(db.String(10))
    dptsPchNm = db.Column(db.String(100))
    rsptMdCd = db.Column(db.String(10))
    rsptMdNm = db.Column(db.String(100))
    uitmCombYn = db.Column(db.String(1))
    uitmChocPossYn = db.Column(db.String(1))
    uitm1AttrTypeNm = db.Column(db.String(100))
    uitm2AttrTypeNm = db.Column(db.String(100))
    uitm3AttrTypeNm = db.Column(db.String(100))
    uitm4AttrTypeNm = db.Column(db.String(100))
    dcRate = db.Column(db.DECIMAL(12, 2))
    dcAmt = db.Column(db.DECIMAL(12, 2))
    svmt = db.Column(db.DECIMAL(12, 2))
    copnDcRate = db.Column(db.DECIMAL(12, 2))
    copnDcAmt = db.Column(db.DECIMAL(12, 2))
    copnNo = db.Column(db.String(100))
    agrYn = db.Column(db.String(1))
    frdlvFormGbcd = db.Column(db.String(10))
    hscd = db.Column(db.String(10))
    rgstId = db.Column(db.String(10))
    rgstIp = db.Column(db.String(15))
    regDtm = db.Column(db.DATETIME)
    chgpId = db.Column(db.String(20))
    chgpIp = db.Column(db.String(15))
    chgDtm = db.Column(db.DATETIME)
    childItemYn = db.Column(db.String(1))
    safeCertTypeGbcd = db.Column(db.String(10))
    storpiupPossYn = db.Column(db.String(1))
    thdyPiupPossYn = db.Column(db.String(1))
    deskRcvnPossYn = db.Column(db.String(1))
    storpiupExclItemYn = db.Column(db.String(1))
    meatHisYn = db.Column(db.String(1))
    chemSafeTrgtYn = db.Column(db.String(1))
    status = db.Column(db.String(1))