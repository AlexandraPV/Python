import codecs
from lxml import etree
import requests
from io import StringIO, BytesIO
import lxml.html as LH
from selenium import webdriver
import xml.etree.cElementTree as ET
import selenium.webdriver.common.keys
import selenium.webdriver.common.action_chains
from selenium.webdriver.common.by import By

url = 'https://stejka.com/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
result = requests.get(url, headers=headers)
tree = LH.document_fromstring(result.content)
root = ET.Element("data")
doc = ET.SubElement(root, "page")
doc.set ('url' , url)




def analiz_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
    result = requests.get(url, headers=headers)
    tree = LH.document_fromstring(result.content)

    doc = ET.SubElement(root, "page")
    doc.set('url', url)


    imgtags = tree.xpath("//img")
    for img in imgtags:
        ET.SubElement(doc, "fragment", type="img").text = img.get('src')
        doc.text = '\n'


    img_background = tree.xpath("//div/@style")
    for img in img_background:
        val = img.find("url(", 0, len(img_background))
        if val is not -1:
            first = img.find("url(", 0, len(img_background))
            end = img.find(")", first, len(img_background))
            new = img[first+4:end]
            ET.SubElement(doc, "fragment", type="img").text = new
            doc.text = '\n'

    texttags = tree.xpath("//div")
    for text_div in texttags:
        if text_div.text is not None:
            ET.SubElement(doc, "fragment", type="text").text = text_div.text
            doc.text = '\n'

    tree = ET.ElementTree(root)
    tree.write("file1.xml")



def analis_all_pages():
    links = tree.xpath('//a')
    print('All links: \n')
    i = 0
    for link in links[:20]:
        i = i + 1
        new_url = 'https://stejka.com' + link.get('href')
        analiz_page(new_url)
        print('{0} {1}'.format(i , new_url))

analiz_page(url)
analis_all_pages()

