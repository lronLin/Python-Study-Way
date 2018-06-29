
import re
import urllib.request
from urllib import parse


# 获取智联页面信息
def get_zhilian_html(url):

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }

    req = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(req)
    return res.read().decode('utf-8')


def get_job_num(html):
    # 正则匹配 获取岗位个数
    result = re.findall('<em>(\d+)</em>', html)
    if result:
        return result[0]
    else:
        return 0


# 匹配公司名称
def get_company_name(html):
    result = re.findall('<td class="gsmc"><a href=.*?>(.*?)</a>', html, re.S)
    print(result)


# 匹配table
def table(html):
    result = re.findall('<table width="853">.*?</table>', html)


# 匹配薪资
def get_salary_num(html):
    result = re.findall('<td class="zwyw">.*.</td>', html, re.S)
    print(result)


# 匹配地址
def get_address(html):
    result = re.findall('<td class="gzdd">.*?</td>', html, re.S)
    print(result)


if __name__ == '__main__':

    # 获取从客户端接收到的参数
    city = input('请输入所搜城市: ')
    job = input('请输入搜索岗位: ')
    # company = input('请输入公司名称: ')
    # salary = input('请输入月薪: ')

    # 输入参数进行解码
    search = parse.urlencode({'jl': city, 'kw': job})

    # urllib进行解析网站的url
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?%s' % search
    html = get_zhilian_html(url)
    # 进行解析地址
    result = get_job_num(html)
    print('城市: %s 岗位: %s 需求量: %s' % (city, job, result))
    print(get_company_name(html))








