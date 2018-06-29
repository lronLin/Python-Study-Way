
import ssl
import urllib.request
from urllib import parse


def main(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(req)  # 读取url的页面源码
    return res.read().decode('utf-8')  # 解码


if __name__ == '__main__':
    msg = input('请输入搜索信息')
    search = parse.urlencode({'wd': msg})
    # url = 'https://www.baidu.com/s?%s' % search
    url = 'http://zhaosheng.fmmu.edu.cn/tjbz.htm' % search
    result = main(url)
    print(result)



