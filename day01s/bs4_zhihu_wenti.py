
import re

import requests
from bs4 import BeautifulSoup


def start_crawl(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    res = requests.get(url, headers=header)

    # 使用lxml的etree去解析
    # html = etree.HTML(res)
    # a = html.xpath('//[@id="zh-recommend-list"]/div[1]/h2/a/text()')
    # a_href = html.xpath('//[@id="zh-recommend-list"]/div[1]/h2/a/@href')
    # print(a)

    # bs4解析
    soup = BeautifulSoup(res.text)
    result = soup.find_all('a', 'question_link')
    questions_list = []
    for i in result:
        # 正则匹配
        # href_result = re.findall('<a .* href="(.*?)"', i)
        href_result = 'https://www.zhihu.com' + i.attrs.get('href')
        a_text = i.get_text().replace('\n', '')
        questions_list.append([href_result, a_text])
    print('知乎发现有多少提问' % len(result))
    print('提问的问题和标题:%s' % questions_list)


if __name__ == '__main__':
    url = 'https://www.zhihu.com/explore'
    start_crawl(url)


