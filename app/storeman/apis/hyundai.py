from .common import send_request
# from stores.hd.config import Config

base_url_a = "http://openapi.thehyundai.com/front/pd/pda/"
base_url_b = "http://openapi.thehyundai.com/front/pd/pdb/"
_header = {}


def test_get_products_by_brand():
    userid = '004503A02152'
    userkey = 'FF08E75795EBA14E770E713A3CFC844D'
    payload = """<?xml version="1.0" encoding="utf-8" ?>
<Root>
    <Dataset id="dsCond">
        <rows>
            <row>
                <brndCd>022467</brndCd>
            </row>
        </rows>
    </Dataset>
</Root>"""

    res = get_products_by_brand(userid, userkey, payload)

    return res

def test_get_product_detail():
    userid = '013368A02139'
    userkey = '60150C5B79E157FBAD80F827AF62D3D9'
    payload = """<?xml version="1.0" encoding="utf-8" ?>
<Root>
    <Dataset id="dsCond">
        <rows>
            <row>
                <brndCd>022467</brndCd>
                <slitmCd>40A1200301</slitmCd>
            </row>
        </rows>
    </Dataset>
</Root>"""

    res = get_product_detail(userid, userkey, payload)

    return res


def __init__():

    pass


def get_products_by_brand(userid, userkey, payload):
    url = base_url_b + "/selectItemGlobal2List.do"
    _header = {
        "Content-Type": "application/xml",
        "oauserId": userid,
        "oauseKey": userkey
    }
    res = send_request(url, 'POST', header=_header, data=payload)
    return res


def get_product_detail(userid, userkey, payload):
    url = base_url_b + "/selectItemGlobal2Detail.do"
    _header = {
        "Content-Type": "application/xml",
        "oauserId": userid,
        "oauseKey": userkey
    }
    res = send_request(url, 'POST', header=_header, data=payload)
    return res


def get_brand_list(userid, userkey, payload):
    url = base_url_b + "/selectBrndList.do"
    _header = {
        "Content-Type": "application/xml",
        "oauserId": userid,
        "oauseKey": userkey,
        "fetchRow": 10,
        "pageNum": 1,
    }
    res = send_request(url, 'POST', header=_header, data=payload)
    return res

def get_category(userid, userkey, payload):
    url = base_url_a + "/selectItemCsfCdList.do"
    _header = {
        "Content-Type": "application/xml",
        "oauserId": userid,
        "oauseKey": userkey,
    }
    res = send_request(url, 'POST', header=_header, data=payload)
    return res


if __name__ == '__main__':
    test_get_products_by_brand()
