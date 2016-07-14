import urllib.request
import re

print("Hello World")

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

# html = getHtml("http://tieba.baidu.com/p/2738151262")


def getImg(html):
    # oldHtml = getHtml(html)
    # print(oldHtml)
    # reg = r'src="(.+?\.png)" pic_ext'
    # reg = 'src=(.*?).jpg'
    # imgre = re.compile(reg)

    ddd = "<div src=http://img.scool.cc/www/img/middle.jpg /> src=http://img.scool.cc/www/img/footer.jpg"
    imglist = re.findall('src=(.*?\.jpg)',ddd,re.S)
    print(imglist)
    return imglist




def testRe():
    a = "abcdxxx123xxx"
    tt = re.findall('xxx(.*?)xxx',a)
    print(tt)


getImg("http://www.scool.cc/")