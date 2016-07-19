import re
import urllib.request


def geturl(url):
    page = urllib.request.urlopen(url)
    html = page.read()

    return html


def get_jpg(html):
    r = r'img src=\"http"(.*?\.jpg)"'
    res = re.compile(r)
    html = html.decode()
    img_list = re.findall(res, html)
    x = 0
    for img in img_list:
        print(img)
       # urllib.request.urlretrieve(img, '%s.jpg' % x)
        x += 1


htl = geturl('http://www.imooc.com/')
get_jpg(htl)
