import codecs
from lxml import etree

import lxml.etree as ETlll
import requests
from io import StringIO, BytesIO
import lxml.html as LH
from selenium import webdriver
import xml.etree.ElementTree as ET


url = 'http://mebli-lviv.com.ua/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
result = requests.get(url, headers=headers)
tree = LH.document_fromstring(result.content)
root = ET.Element("data")
# doc = ET.SubElement(root, "page")
# doc.set ('url' , url)




def analiz_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
    result = requests.get(url, headers=headers)
    tree = LH.document_fromstring(result.content)

    # doc = ET.SubElement(root, "elem")
    # doc.set('url', url)

    img_list = list(tree.xpath("//div[contains(@class, 'clearfix')]/a[contains(@class, 'img')]/img"))
    text_list = list(tree.xpath("//h3[contains(@class, 'name')]/a"))
    price_list = list(tree.xpath("//span[@class = 'price-new' or @class = 'special-price']"))

    count = len(list(price_list))

    for elem in range(count):
        doc = ET.SubElement(root, "elem")
    # for img in img_list:
    #     print(elem)
        ET.SubElement(doc, "image").text = img_list[elem].get('src')
        doc.text = '\n'

    # for text_name in text_list:
        ET.SubElement(doc, "text").text = text_list[elem].text
        doc.text = '\n'

    # for price in price_list:
        ET.SubElement(doc, "price").text = price_list[elem].text
        doc.text = '\n'

    # img_background = tree.xpath("//div/@style")
    # for img in img_background:
    #     val = img.find("url(", 0, len(img_background))
    #     if val is not -1:
    #         first = img.find("url(", 0, len(img_background))
    #         end = img.find(")", first, len(img_background))
    #         new = img[first+4:end]
    #         ET.SubElement(doc, "fragment", type="img").text = new
    #         doc.text = '\n'
    #
    # texttags = tree.xpath("//div")
    # for text_div in texttags:
    #     if text_div.text is not None:
    #         ET.SubElement(doc, "fragment", type="text").text = text_div.text
    #         doc.text = '\n'

    tree = ET.ElementTree(root)
    tree.write("file2.xml")



analiz_page(url)





dom = ETlll.parse("file2.xml")
xslt = ETlll.parse("filwxslt.xsl")
transform = ETlll.XSLT(xslt)
newdom = transform(dom)
# print(newdom)

newdom.write("file_x.html")