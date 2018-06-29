# coding=utf-8


import re
import urllib.request

import pymysql


# 传页面信息 - 解码页面内容
def decode_html(html, charsets=('utf-8', 'gbk')):
    # 编码
    page_html = ''
    for charset in charsets:
        try:
            page_html = html.decode(charset)  # 源码编码如果正常解析, 跳出循环
            break
        except Exception as e:
            print(e)
            print('编码出错')
    return page_html


# 正则匹配内容
def pattern_regex(html, pattern, flags=re.S):
    # 正则类型, flags参数 返回网页的正则表达式
    html_regex = re.compile(pattern, flags)
    return html_regex.findall(html) if html else []


# 获取页面(封装源码)
def get_html(url):
    # 请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    # 解析页面
    req = urllib.request.Request(url, headers=header)  # 请求的响应
    res = urllib.request.urlopen(req)  # 打开页面
    page_html = decode_html(res.read())  # 解析网页源码
    return page_html


# 连接数据库
def get_mysql(sql, params_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           password='123456', database='spider', charset='utf8')
    # 游标对象
    cursor = conn.cursor()
    cursor.executemany(sql, params_list)  # 传参,往数据库存储信息
    conn.commit()
    cursor.close()


def start_crawl(url):
    page_html = get_html(url)
    # 正则获取网页信息
    link_list = pattern_regex(page_html, "<a test=a href='(.*?)'")
    params_list = []
    for link_url in link_list:
        # 获取新闻的链接地址
        html = get_html(link_url)
        # 标题
        title = pattern_regex(html, '<h1>(.*?)<span class="article_tag">')
        # 内容
        content = pattern_regex(html, '<article class="article" id="mp-editor">(.*?)</article>')

        params_list.append([title[0], content[0]])

    sql = 'insert into result_souhu values (%s, %s)'
    get_mysql(sql, params_list)


if __name__ == '__main__':
    url = 'http://sports.souhu.com/nba.shtml'  # F12获取链接信息
    start_crawl(url)

