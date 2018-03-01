# _*_ coding: utf-8 _*_
from bs4 import *
import requests
import urllib2, re, urllib
import re

class Crawler(object):
    '''
    '''
    def __init__(self, html_url):
        page = urllib2.urlopen(html_url)
        self.text = page.read()

    def multiple_replace(self, text, adict):
        '''
        replace multiple str at one time
        '''
        rx = re.compile('|'.join(map(re.escape, adict)))
        def one_xlat(match):
            return adict[match.group(0)]
        return rx.sub(one_xlat, text)
        
    def get_image_list(self, html_text, re_reg=None):
        '''
        return the image url in a html
        '''
        if not re_reg:
            re_reg = re.compile(r'src="(.*?\.jpg)"')
        image_list = re.findall(re_reg, html_text)
        return image_list
    def get_image_dict(self, html_text, re_reg=None):
        '''
        '''
        image_list = self.get_image_list(html_text, re_reg)
        image_dict = {}
        for image in image_list:
            image_dict.setdefault(image[1], image[0])
        return image_dict
    
    def download_images(self, url_list, file_path):
        '''
        '''
        if isinstance(url_list, str):
            url_list = [url_list]

        for url in url_list:
            data = urllib2.urlopen(url).read()
            filename = url.split('/')[-1]
            print "Download picture %s" % filename
            f = open(file_path + "\\pic\\%s" % filename, 'wb')
            f.write(data)
            f.close()
    def download_use_retrive(self, url_dic, file_path):
        '''
        use urlretrive to download
        @param url_dic: movie name and movie pic url
        '''

        for name, url in url_dic.items():
            print "Download picture %s" % name
            urllib.urlretrieve(url, file_path + "/url/%s.jpg" % str(name).decode('utf-8'))

url = "https://movie.douban.com/"
def download_douban_homepage(url="https://movie.douban.com/", save_page=False):
    '''
    image usl is like:
    https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2369036157.jpg
    '''
    cr = Crawler(url)
    if save_page:
        f = open(r"D:\myPython\urlread\%s.txt" % cr.multiple_replace(url, {':':"", '/':""}), 'w')
        f.write(cr.text)
        f.close()
    # images_urls = cr.get_image_list(cr.text)
    # for image in images_urls:
    #     cr.download_images(image, r"D:\myPython")
    image_dicts = cr.get_image_dict(cr.text, r'src="(.*?\.jpg)".*alt="(.*?)"')
    cr.download_use_retrive(image_dicts, r"D:\myPython")

def multiple_replace(text, adict):
    '''
    replace multiple str at one time
    '''
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

def download_homepage(url, save_page=False):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if save_page:
        f = open(r"D:\myPython\beautiful_soup\%s.txt" % multiple_replace(url, {':':"", '/':""}), 'w')
        f.write(wb_data.text.encode('utf-8'))
        f.close()
    return soup


# download_douban_homepage(save_page=True)
# download_homepage(url, True)
url = "https://www.dianping.com/search/category/2/10/r1489"
soup = download_homepage(url, False)
addr = soup.select('.div.content span.addr')
# "#代表id,.代表class"
print addr

# For 58
url = "http://bj.58.com/pingbandiannao/26088204291258x.shtml"
soup = download_homepage(url, False)
price = soup.select('#content span.price')
times = soup.select('#content li.time')
counts = soup.select('#content li.count')
print price
for time in times:
    print time.name, time.text
print counts


