import re    #正则表达式
import requests  #第三方http请求
from lxml import etree  #html解析
import pymongo  #MongoDB

# Scool图片爬取
# def spiderHtml(htmlUrl):
#     htmlData = requests.get(htmlUrl)
#     needData = re.findall('src=\"(.*?\.jpg)',htmlData.text)
#     return needData
#
# tempData = spiderHtml("http://www.scool.cc")
# for pData in tempData:
#     print(pData)

lessonPicList = []
lessonTitleList = []
goLoop = True
pageNumber = 1


conn = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = conn['RoyDB']
print(db.collection_names())
collect = db['JKXY']

def spiderJK_Etree(url):
    htmlData = requests.get(url)
    selector = etree.HTML(htmlData.text)
    picPath = selector.xpath('//ul[@class="cf"]/li/div[@class="lessonimg-box"]/a/img/@src')
    picTitle = selector.xpath('//ul[@class="cf"]/li/div[@class="lesson-infor"]/h2/a/text()')
    print(picPath)
    print(picTitle)

    index = 0
    for temp in picPath:
        information = {"picPath": temp, "lessonTitle": picTitle[index]}
        collect.insert(information)
        index+=1


    # if(len(lessonPicList) > 0):
    #     if(len(picPath) > 0):
    #         if lessonPicList[0] == picPath[0]:
    #             print(lessonPicList[0])
    #             print(picPath[0])
    #             print("到头了")
    #         else:
    #             for pic in picPath:
    #                 lessonPicList.append(pic)
    #
    #             for title in picTitle:
    #                 lessonTitleList.append(picTitle)
    #
    # else:
    #     for pic in picPath:
    #         lessonPicList.append(pic)
    #
    #     for title in picTitle:
    #         lessonTitleList.append(picTitle)





def spiderJKLoop(page):
    while(page < 90):
     spiderJK_Etree('http://www.jikexueyuan.com/course/?pageNum=%d' % page)
     page = page + 1




#极客学院图片爬取
def spiderJK_HTML(url):

    htmlData = requests.get(url)

    # 图片爬取
    jkPicUp = '<div class=\"lessonimg-box\">(.*?)</div>'
    jkTPZZ = '<img src=\"(.*?\.jpg)'
    picData = re.findall(jkTPZZ,htmlData.text)
    #Title爬取
    jkTTZZ = '<h2 class="lesson-info-h2">(.*?)</h2>'
    ttUpData = re.findall(jkTTZZ,htmlData.text)

    for tempPic in picData:
        print(tempPic)


    for tempData in ttUpData:
        jkZZ = '>(.*?)</a>'
        temp = re.findall(jkZZ, tempData)
        print(temp)

# spiderJK_HTML("http://www.jikexueyuan.com/")


spiderJKLoop(pageNumber)





# try:
#   from lxml import etree
#   print("running with lxml.etree")
# except ImportError:
#   try:
#     # Python 2.5
#     import xml.etree.cElementTree as etree
#     print("running with cElementTree on Python 2.5+")
#   except ImportError:
#     try:
#       # Python 2.5
#       import xml.etree.ElementTree as etree
#       print("running with ElementTree on Python 2.5+")
#     except ImportError:
#       try:
#         # normal cElementTree install
#         import cElementTree as etree
#         print("running with cElementTree")
#       except ImportError:
#         try:
#           # normal ElementTree install
#           import elementtree.ElementTree as etree
#           print("running with ElementTree")
#         except ImportError:
#           print("Failed to import ElementTree from any known place")