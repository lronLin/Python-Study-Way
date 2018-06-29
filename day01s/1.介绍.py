
import urllib.request
import ssl

# url = 'http://www.baidu.com'

url = 'https://www.12306.cn/mormhweb'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}


req = urllib.request.Request(url, headers=header)
# 忽略未经审核的ssl认证
content = ssl._create_unverified_context()
res = urllib.request.urlopen(url, context=content)

print(res.read().decode('utf-8'))
