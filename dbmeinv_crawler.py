# dbmeinv_Crawler.py Version 0.0.4  Created by coreVK
# Python 3.4.3 IDLE - Windows 7 SP1
# 更新日志：
# 0.0.1 源代码创建
# 0.0.2 修正网关错误：502
# 0.0.3 削减非必要功能
# 0.0.4 修正网络错误：403

import re
import os
import socket
import random
import urllib.request
import http.cookiejar

# R.E.
li_re = re.compile(r'<li class="span3">(.+?)</li>', re.DOTALL)
name_re = re.compile(r'<img class="height_min".+?src="http://.+?/bmiddle/(.+?)" />', re.DOTALL)

# TYPE = {'1': '性感妹',
#         '2': '大胸妹',
#         '3': '大长腿',
#         '4': '小清新',
#         '5': '文艺范',
#         '6': '小翘臀',
#         '7': '黑丝袜'}


class Open(object):
    def __init__(self):
        socket.setdefaulttimeout(20)
        cookie_support = urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
        self.opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
        urllib.request.install_opener(self.opener)

    def open(self, url):
        user_agents = [
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11",
            "Opera/9.25 (Windows NT 5.1; U; en)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)",
            "Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "]

        self.opener.addheaders = [("User-agent", random.choice(user_agents)), ("Accept", "*/*"),
                                  ('Referer', 'http://www.monkey.com')]

        try:
            resource = self.opener.open(url)
        except Exception:
            raise Exception
        else:
            return resource


def get(cid, page_num, save_dir):
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    for num in range(1, int(page_num) + 1):
        address = (("http://www.dbmeinv.com/dbgroup/show.htm?cid=%d&pager_offset=%d") % (int(cid), int(num)))

        for li in li_re.findall(Open().open(address).read().decode("utf8")):
            name = ''.join(name_re.findall(li))
            print("page " + str(num) + " : " + name)
            urllib.request.urlretrieve("http://ww2.sinaimg.cn/large/" + name, save_dir + "\%s" % name)
            if not name.strip():
                os._exit(0)

    print("Finish!")


if __name__ == '__main__':
    TYPE = input("类型：1.性感 2.大胸 3.美腿 4.清新 5.文艺范 6.翘臀 7.丝袜 请输入:")
    pageNum = input("最大页面序号：")
    saveDir = "e:\dbm\\" + str(TYPE) + "\mm"
    get(TYPE, pageNum, saveDir)
