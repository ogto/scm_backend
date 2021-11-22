import json

from app import db
from app.storeman.stores.hd.models.category import Category
from app.storeman.stores.hd.models.brand import Brand
from app.storeman.stores.hd.models.hdproduct import HDProduct
from app.storeman.stores.hd.models.product_img import HDProductImg
from app.storeman.stores.hd.models.product_html import HDProductHtml
from app.storeman.stores.hd.models.product_item import HDProductItem
from app.storeman.stores.hd.models.product_price import HDProductPrice
from app.storeman.stores.hd.models.product_sell import HDProductSell
from app.storeman.utils.encoder import AlchemyEncoder


def get_all_products():
    data = HDProduct.query.all()
    return json.loads(json.dumps(data, cls=AlchemyEncoder))


def get_product_detail(store_id, product_id):
    return HDProduct.query.filter_by(store_id=store_id, prd_code=product_id).all()


def update_products_stock(data):
    prd = HDProductPrice.query.filter_by(slitmCd=data['slitmcd']).first()
    if prd:
        prd_stock = HDProductItem(
            slitmCd=data['slitmcd'],
            dluMaxBuyQty=data['dlumaxbuyqty'],
        )
        save_changes(prd_stock)
        response_object = {
            'status': 'success',
            'message': 'Successfully Update Stock Qty.',
            'product': prd_stock
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Failed to update stock Qty. Please Log in.',
        }
        return response_object, 409


def save_new_product_price(data):
    prd = HDProductPrice.query.filter_by(slitmCd=data['slitmcd']).first()
    if not prd:
        new_prd_price = HDProductPrice(
            slitmCd=data['slitmcd'],
            prcAthzSeq=data['prcathzseq'],
            prcAplyStrtDtm=data['prcaplystrtdtm'],
            sellPrc=data['sellprc'],
            prchPrc=data['prchprc'],
            mrgnRate=data['mrgnrate'],
            wintInsmMths=data['wintinsmmths'],
            csmPrc=data['csmprc'],
            svmtPrdcYn=data['svmtprdcyn'],
            spymDcAmt=data['spymdcamt'],
            spymDcYn=data['spymdcyn'],
            gnrlCopnNo=data['gnrlcopnno'],
            svmtRate=data['svmtrate'],
            svmt=data['svmt'],
            prcDcEndDtm=data['prcdcenddtm'],
            stplMths=data['stplmths'],
            insmMths=data['insmmths'],
            venItemCd=data['venitemcd'],
            dptsVenOpCd=data['dptsvenopcd'],
            dptsVenSaleCd=data['dptsvensalecd'],
        )
        save_changes(new_prd_price)
        response_object = {
            'status': 'success',
            'message': 'Successfully insert Hyundai Product HTML.',
            'product': new_prd_price
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def save_new_product_item(slitmcd, data):
    prd = HDProductItem.query.filter_by(slitmCd=slitmcd).first()
    if not prd:
        new_prd_item = HDProductItem(
            slitmCd=slitmcd,
            itemCsfNm=data['itemcsfnm'],
            itemLCsfNm=data['itemlcsfnm'],
            itemMCsfNm=data['itemmcsfnm'],
            itemSCsfNm=data['itemscsfnm'],
            itemDCsfNm=data['itemdcsfnm'],
            itemLCsfCd=data['itemlcsfcd'],
            itemMCsfCd=data['itemmcsfcd'],
            itemSCsfCd=data['itemscsfcd'],
            itemDCsfCd=data['itemdcsfcd'],
            itemCsfGbcd=data['itemcsfgbcd'],
            itemCsfGbcdNm=data['itemcsfgbcdnm'],
            itemCsfLvl=data['itemcsflvl'],
            osbd=data['osbd'],
            sizeCsfGbcd=data['sizecsfgbcd'],
            qaTrgtYn=data['qatrgtyn'],
            safeCertTrgtYn=data['safecerttrgtyn'],
            coreMngYn=data['coremngyn'],
            itstDlbrYn=data['itstdlbryn'],
            infNotfBsicCd=data['infnotfbsiccd'],
            hmallPntAcmRate=data['hmallpntacmrate'],
            hmallPntAcmRateUseYn=data['hmallpntacmrateuseyn'],
            dluMaxBuyQty=data['dlumaxbuyqty'],
            yruMaxBuyQty=data['yrumaxbuyqty'],
            qaCsfCd=data['qacsfcd'],
            itemPupUseYn=data['itempupuseyn'],
            frdlvSellLimtYn=data['frdlvselllimtyn'],
            imdtCnclPossYn=data['imdtcnclpossyn'],
            mnfcSellCoMndrYn=data['mnfcsellcomndryn'],
            satOffdYn=data['satoffdyn'],
            hscd=data['hscd'],
            safeCertTypeGbcd=data['safecerttypegbcd'],
            storpiupPossYn=data['storpiuppossyn'],
        )
        save_changes(new_prd_item)
        response_object = {
            'status': 'success',
            'message': 'Successfully insert Hyundai Product HTML.',
            'product': new_prd_item
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def save_new_product_html(data):
    prd = HDProductHtml.query.filter_by(slitmCd=data['slitmcd']).first()
    if not prd:
        new_prd_html = HDProductHtml(
            slitmCd=data['slitmcd'],
            htmlItstGbdc=data['htmlitstgbcd'],
            htmlItstCntn=json.dumps(data['htmlitstcntn'])
        )
        save_changes(new_prd_html)
        response_object = {
            'status': 'success',
            'message': 'Successfully insert Hyundai Product HTML.',
            'product': new_prd_html
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def save_new_product_img(data):
    prd = HDProductImg.query.filter_by(slitmCd=data['slitmcd']).first()
    code = data['slitmcd']
    if not prd:
        path_1 = code[2:4]
        path_2 = code[4:6]
        path_3 = code[6:7]
        path_4 = code[7:8]
        path_5 = code[8:9]
        img_path = "https://image.thehyundai.com/static/" + path_5 + "/" + path_4 + "/" + path_3 + "/" + path_2 + "/" + path_1 + "/"
        new_prd_img = HDProductImg(
            slitmCd=data['slitmcd'],
            slitmImgSeq=data['slitmimgseq'],
            imgLblNm=data['imglblnm'] if not data['imglblnm'] else img_path + data['imglblnm'],
            orglImgNm=data['orglimgnm'] if not data['orglimgnm'] else img_path + data['orglimgnm'],
            trndhImgNm=data['trndhimgnm'] if not data['trndhimgnm'] else img_path + data['trndhimgnm'],
            sImgNm=data['simgnm'] if not data['simgnm'] else img_path + data['simgnm'],
            mImgNm=data['mimgnm'] if not data['mimgnm'] else img_path + data['mimgnm'],
            lImgNm=data['limgnm'] if not data['limgnm'] else img_path + data['limgnm'],
            enlg1ImgNm=data['enlg1imgnm'] if not data['enlg1imgnm'] else img_path + data['enlg1imgnm'],
            enlg2ImgNm=data['enlg2imgnm'] if not data['enlg2imgnm'] else img_path + data['enlg2imgnm'],
            enlg3ImgNm=data['enlg3imgnm'] if not data['enlg3imgnm'] else img_path + data['enlg3imgnm'],
            enlg1ImgSize=data['enlg1imgsize'],
            enlg2ImgSize=data['enlg2imgsize'],
            enlg3ImgSize=data['enlg3imgsize']
        )
        save_changes(new_prd_img)
        response_object = {
            'status': 'success',
            'message': 'Successfully insert Hyundai Product Images.',
            'product': new_prd_img
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def save_new_product_sell(data):
    prd = HDProductSell.query.filter_by(slitmCd=data['slitmcd']).first()
    if not prd:
        new_prd_sell = HDProductSell(
            bsitmCd=data['bsitmcd'],
            slitmCd=data['slitmcd'],
            uitmCd=data['uitmcd'],
            uitmTmpCd=data['uitmtmpcd'],
            uitmClrGbcd=data['uitmclrgbcd'],
            uitmSizeCd=data['uitmsizecd'],
            uitmPatnGbcd=data['uitmpatngbcd'],
            uitmItemFormCd=data['uitmitemformcd'],
            uitm1AttrNm=data['uitm1attrnm'],
            uitm2AttrNm=data['uitm2attrnm'],
            uitm3AttrNm=data['uitm3attrnm'],
            uitm4AttrNm=data['uitm4attrnm'],
            uitmEtcNm=data['uitmetcnm'],
            uitmTotNm=data['uitmtotnm'],
            sellGbcd=data['sellgbcd'],
            sellStrtDt=data['sellstrtdt'],
            sellEndDt=data['sellenddt'],
            uitmStckSeq=data['uitmstckseq'],
            maxSellPossQty=data['maxsellpossqty'],
            oldMaxSellPossQty=data['oldmaxsellpossqty'],
            totSellQty=data['totsellqty'],
            uitm1HexClrVal=data['uitm1hexclrval'],
            uitm2HexClrVal=data['uitm2hexclrval'],
            uitm3HexClrVal=data['uitm3hexclrval'],
            uitm4HexClrVal=data['uitm4hexclrval'],
            imgNm=data['imgnm'],
            remainQty=data['remainqty'],
        )
        save_changes(new_prd_sell)
        response_object = {
            'status': 'success',
            'message': 'Successfully insert Hyundai Product Sell Info.',
            'product': new_prd_sell
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Failed to insert Product Sell Info',
        }
        return response_object, 409


def save_new_product_detail(data):
    prd = HDProduct.query.filter_by(slitmCd=data['slitmcd']).first()
    if not prd:
        new_prd = HDProduct(
            slitmCd=data['slitmcd'],
            sitmCd=data['sitmcd'],
            bsitmCd=data['bsitmcd'],
            slitmNm=data['slitmnm'],
            baseCmpsItemNm=data['basecmpsitemnm'],
            addCmpsItemNm=data['addcmpsitemnm'],
            engItemNm=data['engitemnm'],
            itemUrl=data['itemurl'],
            itemLCsfCd=data['itemlcsfcd'],
            itemMCsfCd=data['itemmcsfcd'],
            itemSCsfCd=data['itemscsfcd'],
            itemDCsfCd=data['itemdcsfcd'],
            itemLCsfNm=data['itemlcsfnm'],
            itemMCsfNm=data['itemmcsfnm'],
            itemSCsfNm=data['itemscsfnm'],
            itemDCsfNm=data['itemdcsfnm'],
            venItemCd=data['venitemcd'],
            afcrItemCd=data['afcritemcd'],
            mkcoGbcd=data['mkcogbcd'],
            mkcoCd=data['mkcocd'],
            mkcoNm=data['mkconm'],
            mkcoCnryGbcd=data['mkcocnrygbcd'],
            mkcoCnryNm=data['mkcocnrynm'],
            mkcoCsfGbcd=data['mkcocsfgbcd'],
            octyCnryGbcd=data['octycnrygbcd'],
            octyCnryNm=data['octycnrynm'],
            prmrOrgCnryGbcd=data['prmrorgcnrygbcd'],
            prmrOrgCnryNm=data['prmrorgcnrynm'],
            prmrOrgNm=data['prmrorgnm'],
            itemMemo=data['itemmemo'],
            asGdCntn=data['asgdcntn'],
            itemWgt=data['itemwgt'],
            itemWdthLen=data['itemwdthlen'],
            itemHghtLen=data['itemhghtlen'],
            itemHghLen=data['itemhghlen'],
            itemAthzGbcd=data['itemathzgbcd'],
            itemAthzGbcdNm=data['itemathzgbcdnm'],
            itemGbcd=data['itemgbcd'],
            itemSellGbcd=data['itemsellgbcd'],
            itemSellGbcdNm=data['itemsellgbcdnm'],
            itemBaseImgNm=data['itembaseimgnm'],
            nchgStlmItemYn=data['nchgstlmitemyn'],
            rntlItemYn=data['rntlitemyn'],
            adltItemYn=data['adltitemyn'],
            itemRegTcndAgrYn=data['itemregtcndagryn'],
            cmisGbcd=data['cmisgbcd'],
            jwlSvrtEnclYn=data['jwlsvrtenclyn'],
            rsptUserId=data['rsptuserid'],
            rsptUserNm=data['rsptusernm'],
            baseSectId=data['basesectid'],
            baseSectNm=data['basesectnm'],
            spexSectId=data['spexsectid'],
            spexSectNm=data['spexsectnm'],
            giftEvntStrtDtm=data['giftevntstrtdtm'],
            giftEvntStrtDt=data['giftevntstrtdt'],
            giftEvntStrtTime=data['giftevntstrttime'],
            giftEvntEndDtm=data['giftevntenddtm'],
            giftEvntEndDt=data['giftevntenddt'],
            giftEvntEndTime=data['giftevntendtime'],
            giftCntn=data['giftcntn'],
            giftImgNm=data['giftimgnm'],
            giftWtdwMndrYn=data['giftwtdwmndryn'],
            giftUprc=data['giftuprc'],
            pgmCmisSlitmCd=data['pgmcmisslitmcd'],
            sincMkcoCd=data['sincmkcocd'],
            sincMkcoNm=data['sincmkconm'],
            slacMkcoCd=data['slacmkcocd'],
            slacMkcoNm=data['slacmkconm'],
            prchVenMkcoCd=data['prchvenmkcocd'],
            prchVenMkcoNm=data['prchvenmkconm'],
            phdsPrxyMkcoCd=data['phdsprxymkcocd'],
            phdsPrxyMkcoNm=data['phdsprxymkconm'],
            alliCrdDcYn=data['allicrddcyn'],
            empDcYn=data['empdcyn'],
            itntAddSvmtYn=data['itntaddsvmtyn'],
            stckGdYn=data['stckgdyn'],
            hmallRsvSellYn=data['hmallrsvsellyn'],
            frgnBuyPrxyYn=data['frgnbuyprxyyn'],
            frdlvCost=data['frdlvcost'],
            basktUseNdmtYn=data['basktusendmtyn'],
            prsnMsgPossYn=data['prsnmsgpossyn'],
            prsnPackPossYn=data['prsnpackpossyn'],
            stckMngUnitGbcd=data['stckmngunitgbcd'],
            addBuyOptUseYn=data['addbuyoptuseyn'],
            venCd=data['vencd'],
            venNm=data['vennm'],
            hdptYn=data['hdptyn'],
            cmisYn=data['cmisyn'],
            vtltStatGbcd=data['vtltstatgbcd'],
            dptsBrnCd=data['dptsbrncd'],
            virtDptsYn=data['virtdptsyn'],
            hitemHndlYn=data['hitemhndlyn'],
            ven2Cd=data['ven2cd'],
            ven2Nm=data['ven2nm'],
            oshpVenAdrSeq=data['oshpvenadrseq'],
            oshpVenPostNo=data['oshpvenpostno'],
            oshpVenAdr=data['oshpvenadr'],
            rtpExchVenAdrSeq=data['rtpexchvenadrseq'],
            rtpExchVenPostNo=data['rtpexchvenpostno'],
            rtpExchVenAdr=data['rtpexchvenadr'],
            emgyExchVenAdrSeq=data['rtpexchvenadr'],
            emgyExchVenPostNo=data['emgyexchvenpostno'],
            emgyExchVenAdr=data['emgyexchvenadr'],
            itntDispYn=data['itntdispyn'],
            itntDispStrtDtm=data['itntdispstrtdtm'],
            itntDispStrtDt=data['itntdispstrtdt'],
            itntDispStrtTime=data['itntdispstrttime'],
            itntDispEndDtm=data['itntdispenddtm'],
            itntDispEndDt=data['itntdispenddt'],
            itntDispEndTime=data['itntdispendtime'],
            gnrlCopnUseYn=data['gnrlcopnuseyn'],
            useCopnExpsYn=data['usecopnexpsyn'],
            itemQnaExpsYn=data['itemqnaexpsyn'],
            bbprcCopnDcYn=data['bbprccopndcyn'],
            bbprcSpymDcYn=data['bbprcspymdcyn'],
            bbprcSpdcYn=data['bbprcspdcyn'],
            bbprcSvmtPrdcYn=data['bbprcsvmtprdcyn'],
            prcExpsBitVal=data['prcexpsbitval'],
            prcExpsBitVal1=data['prcexpsbitval1'],
            prcExpsBitVal2=data['prcexpsbitval2'],
            prcExpsBitVal4=data['prcexpsbitval4'],
            prcExpsBitVal8=data['prcexpsbitval8'],
            webExpsPrmoNm=data['webexpsprmonm'],
            prmo1TxtCntn=data['prmo1txtcntn'],
            prmo2TxtCntn=data['prmo2txtcntn'],
            prmoTxtDcCopnYn=data['prmotxtdccopnyn'],
            prmoTxtSpdcYn=data['prmotxtspdcyn'],
            prmoTxtSvmtYn=data['prmotxtsvmtyn'],
            prmoTxtFamtFxrtGbcd=data['prmotxtfamtfxrtgbcd'],
            prmoTxtSvmtPrdcYn=data['prmotxtsvmtprdcyn'],
            prmoTxtWintYn=data['prmotxtwintyn'],
            prmoTxtSpymDcYn=data['prmotxtspymdcyn'],
            prmoExpsStrtDtm=data['prmoexpsstrtdtm'],
            prmoExpsStrtDt=data['prmoexpsstrtdt'],
            prmoExpsStrtTime=data['prmoexpsstrttime'],
            prmoExpsEndDtm=data['prmoexpsenddtm'],
            prmoExpsEndDt=data['prmoexpsenddt'],
            prmoExpsEndTime=data['prmoexpsendtime'],
            frdlvYn=data['frdlvyn'],
            packOpenRtpNdmtYn=data['packopenrtpndmtyn'],
            mdRcmmYn=data['mdrcmmyn'],
            ostkYn=data['ostkyn'],
            dlvHopeDtDsntYn=data['dlvhopedtdsntyn'],
            trndhHitTagExpsYn=data['trndhhittagexpsyn'],
            trndhSsaleTagExpsYn=data['trndhssaletagexpsyn'],
            trndhExclTagExpsYn=data['trndhexcltagexpsyn'],
            itstHtmlYn=data['itsthtmlyn'],
            htmlGnrlItstSmexYn=data['htmlgnrlitstsmexyn'],
            itstPhotoExpsYn=data['itstphotoexpsyn'],
            dlvItemFormGbcd=data['dlvitemformgbcd'],
            qckDlvPossYn=data['qckdlvpossyn'],
            lrpyYn=data['lrpyyn'],
            sameItemMxpkPossQty=data['sameitemmxpkpossqty'],
            mxpkYn=data['mxpkyn'],
            packMagnGbcd=data['packmagngbcd'],
            dlvcGbcd=data['dlvcgbcd'],
            dlvcPayGbcd=data['dlvcpaygbcd'],
            dlvcPayGbcdNm=data['dlvcpaygbcdnm'],
            inslItemYn=data['inslitemyn'],
            arpayDlvGdCntn=data['arpaydlvgdcntn'],
            osbd=data['osbd'],
            cvstWtdwPossYn=data['cvstwtdwpossyn'],
            prpyDlvCost=data['prpydlvcost'],
            irgnAreaAddDlvCost=data['irgnareaadddlvcost'],
            shipInstStopYn=data['shipinststopyn'],
            dlvBoxCmpsQty=data['dlvboxcmpsqty'],
            dsrvDlvcoCd=data['dsrvdlvcocd'],
            mngWhNo=data['mngwhno'],
            sbctDlvcoCd=data['sbctdlvcocd'],
            dlvMagnGbcd=data['dlvmagngbcd'],
            dlvcChmgGbcd=data['dlvcchmggbcd'],
            dlvFormGbcd=data['dlvformgbcd'],
            dlvFormGbcdNm=data['dlvformgbcdnm'],
            rtpPossYn=data['rtppossyn'],
            rtpWdmtGbcd=data['rtpwdmtgbcd'],
            rtpDlvCost=data['rtpdlvcost'],
            exchPossYn=data['exchpossyn'],
            exchWdmtGbcd=data['exchwdmtgbcd'],
            exchDlvCost=data['exchdlvcost'],
            custDlvcWdmtGbcd=data['custdlvcwdmtgbcd'],
            satOffdYn=data['satoffdyn'],
            ordMakeYn=data['ordmakeyn'],
            ordUnitMaxOrdQty=data['ordunitmaxordqty'],
            stlmWayScopGbcd=data['stlmwayscopgbcd'],
            pntStlmNdmtYn=data['pntstlmndmtyn'],
            cmpsOrdQtyGbcd=data['cmpsordqtygbcd'],
            enlgSrchTagNm=data['enlgsrchtagnm'],
            prcsExpsExcldYn=data['prcsexpsexcldyn'],
            hmallItemSrchExcldYn=data['hmallitemsrchexcldyn'],
            niamtSmsExcldYn=data['niamtsmsexcldyn'],
            ostkRishpSmsYn=data['ostkrishpsmsyn'],
            oshpSmsExcldYn=data['oshpsmsexcldyn'],
            itemImgRtntGbcd=data['itemimgrtntgbcd'],
            flashFileNm=data['flashfilenm'],
            vodFileNm=data['vodfilenm'],
            slitmAprvlGbcd=data['slitmaprvlgbcd'],
            slitmAprvlGbcdNm=data['slitmaprvlgbcdnm'],
            itemQaRstGbcd=data['itemqarstgbcd'],
            itemQaRstGbcdNm=data['itemqarstgbcdnm'],
            askCntn=data['askcntn'],
            qaRstCntn=data['qarstcntn'],
            hmallDlbrStatGbcd=data['hmalldlbrstatgbcd'],
            hmallDlbrStatGbcdNm=data['hmalldlbrstatgbcdnm'],
            mrgnRateJdgmGbcd=data['mrgnratejdgmgbcd'],
            mrgnRateJdgmGbcdNm=data['mrgnratejdgmgbcdnm'],
            taxnJdgmYn=data['taxnjdgmyn'],
            mrgnJdgmCmptYn=data['mrgnjdgmcmptyn'],
            itntSaleYn=data['itntsaleyn'],
            blcwdItemYn=data['blcwditemyn'],
            clhItemNm=data['clhitemnm'],
            clhStrtDtm=data['clhstrtdtm'],
            clhStrtDt=data['clhstrtdt'],
            clhStrtTime=data['clhstrttime'],
            clhEndDtm=data['clhenddtm'],
            clhEndDt=data['clhenddt'],
            clhEndTime=data['clhendtime'],
            clhMaxQty=data['clhmaxqty'],
            clhMinQty=data['clhminqty'],
            itemPackSize=data['itempacksize'],
            addDlvCost=data['adddlvcost'],
            bsitmRepYn=data['bsitmrepyn'],
            giftItemYn=data['giftitemyn'],
            frchPrchYn=data['frchprchyn'],
            bsitmNm=data['bsitmnm'],
            itemTypeGbcd=data['itemtypegbcd'],
            intgItemGbcd=data['intgitemgbcd'],
            frstRegMdaGbcd=data['frstregmdagbcd'],
            prchMdaGbcd=data['prchmdagbcd'],
            vatRate=data['vatrate'],
            itemTaxnYn=data['itemtaxnyn'],
            prchMthdGbcd=data['prchmthdgbcd'],
            itemTaxnGbcd=data['itemtaxngbcd'],
            ringItemYn=data['ringitemyn'],
            brndCd=data['brndcd'],
            brndNm=data['brndnm'],
            itntBrndNm=data['itntbrndnm'],
            dptsPchCd=data['dptspchcd'],
            dptsPchNm=data['dptspchnm'],
            rsptMdCd=data['rsptmdcd'],
            rsptMdNm=data['rsptmdnm'],
            uitmCombYn=data['uitmcombyn'],
            uitmChocPossYn=data['uitmchocpossyn'],
            uitm1AttrTypeNm=data['uitm1attrtypenm'],
            uitm2AttrTypeNm=data['uitm2attrtypenm'],
            uitm3AttrTypeNm=data['uitm3attrtypenm'],
            uitm4AttrTypeNm=data['uitm4attrtypenm'],
            dcRate=data['dcrate'],
            dcAmt=data['dcamt'],
            svmt=data['svmt'],
            copnDcRate=data['copndcrate'],
            copnDcAmt=data['copndcamt'],
            copnNo=data['copnno'],
            agrYn=data['agryn'],
            frdlvFormGbcd=data['frdlvformgbcd'],
            hscd=data['hscd'],
            rgstId=data['rgstid'],
            rgstIp=data['rgstip'],
            regDtm=data['regdtm'],
            chgpId=data['chgpid'],
            chgpIp=data['chgpip'],
            chgDtm=data['chgdtm'],
            childItemYn=data['childitemyn'],
            safeCertTypeGbcd=data['safecerttypegbcd'],
            storpiupPossYn=data['storpiuppossyn'],
            thdyPiupPossYn=data['thdypiuppossyn'],
            deskRcvnPossYn=data['deskrcvnpossyn'],
            storpiupExclItemYn=data['storpiupexclitemyn'],
            meatHisYn=data['meathisyn'],
            chemSafeTrgtYn=data['chemsafetrgtyn'],
            status=data['status'],
        )
        save_changes(new_prd)
        response_object = {
            'status': 'success',
            'message': 'Successfully insert Hyundai Product.',
            'product': new_prd
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def save_new_brand_prd(data):
    prd = Brand.query.filter_by(slitmCd=data['slitmCd']).first()
    if not prd:
        new_brand = Brand(
            venCd=data['venCd'],
            slitmCd=data['slitmCd'],
            sitmCd=data['sitmCd'],
            bsitmCd=data['bsitmCd'],
            slitmNm=data['slitmNm'],
            brndCd=data['brndCd'],
            brndNm=data['brndNm'],
        )
        save_changes(new_brand)
        response_object = {
            'status': 'success',
            'message': 'Successfully insert Hyundai Product.',
            'product': new_brand
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def save_categories(data):
    prd = Category.query.filter_by(itemCsfCd=data['itemCsfCd']).first()
    if not prd:
        new_category = Category(
            lvl=data['lvl'],
            itemCsfCd=data['itemCsfCd'],
            itemCsfNm=data['itemCsfNm'],
            highItemCsfCd=data['highItemCsfCd'],
            useYn=data['useYn'],
            itemCsfGbcd=data['itemCsfGbcd'],
            itemCsfGbcdNm=data['itemCsfGbcdNm'],
            itemCsfLvl=data['itemCsfLvl'],
            osbd=data['osbd'],
            sizeCsfGbcd=data['sizeCsfGbcd'],
            sizeCsfGbcdNm=data['sizeCsfGbcdNm'],
            qaTrgtYn=data['qaTrgtYn'],
            safeCertTrgtYn=data['safeCertTrgtYn'],
            safeCertTypeGbcd=data['safeCertTypeGbcd'],
            coreMngYn=data['coreMngYn'],
            itstDlbrYn=data['itstDlbrYn'],
            infNotfBsicCd=data['infNotfBsicCd'],
            infNotfBsicNm=data['infNotfBsicNm'],
            hdmalPntAcmRate=data['hdmalPntAcmRate'],
            hdmalPntAcmRateUseYn=data['hdmalPntAcmRateUseYn'],
            dluMaxBuyQty=data['dluMaxBuyQty'],
            yruMaxBuyQty=data['yruMaxBuyQty'],
            qaCsfCd=data['qaCsfCd'],
            qaCsfNm=data['qaCsfNm'],
            itemPupUseYn=data['itemPupUseYn'],
            frdlvSellLimtYn=data['frdlvSellLimtYn'],
            imdtCnclPossYn=data['imdtCnclPossYn'],
            itemTaxnGbcd=data['itemTaxnGbcd'],
            custMskExcpProcYn=data['custMskExcpProcYn'],
            hscd=data['hscd'],
            itemCsfCdL=data['itemCsfCdL'],
            itemCsfCdM=data['itemCsfCdM'],
            itemCsfCdS=data['itemCsfCdS'],
            itemCsfCdD=data['itemCsfCdD'],
            itemCsfNmL=data['itemCsfNmL'],
            itemCsfNmM=data['itemCsfNmM'],
            itemCsfNmS=data['itemCsfNmS'],
            itemCsfNmD=data['itemCsfNmD'],
            storpiupPossYn=data['storpiupPossYn'],
            cvstDlvYn=data['cvstDlvYn'],
            subwDlvYn=data['subwDlvYn'],
        )
        save_changes(new_category)
        response_object = {
            'status': 'success',
            'message': 'Successfully insert new category.',
            'product': new_category
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'It already exists. Please Log in.',
        }
        return response_object, 409



def get_a_product(product_id):
    return Brand.query.filter_by(slitmCd=product_id).first()


def get_new_product_list(brndcd):
    q = db.session.query(Brand.slitmCd)\
        .outerjoin(HDProduct, Brand.slitmCd == HDProduct.slitmCd)\
        .filter(HDProduct.slitmCd == None)\
        .filter(Brand.brndCd == brndcd)

    return q.all()


def save_changes(data: any) -> None:
    db.session.add(data)
    db.session.commit()

