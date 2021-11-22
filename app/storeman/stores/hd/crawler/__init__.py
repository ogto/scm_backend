from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv, datetime, boto3, re

now = datetime.datetime.now()
url = 'https://www.thehyundai.com/front/pda/itemPtc.thd?slitmCd='

def get_images(url, slitmcd):
    _url = urlopen(url + slitmcd)
    bsObject = BeautifulSoup(_url, "html.parser")

    image_path = "https://image.thehyundai.com/static/2/9/2/62/20/"