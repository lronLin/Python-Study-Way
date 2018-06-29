
import urllib.request
from urllib import parse
import json


def urllib_open(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(req)
    return res.read().decode('utf-8')


def get_movie_tag(url):
    tag_res = urllib_open(url)
    result = json.loads(tag_res)
    content = result['tags']
    return content


def get_movies(tag_url, movies_url):
    tag_content = get_movie_tag(tag_url)
    tag_list = []
    print(tag_content)
    for tag in tag_content:
        data = {'tag': tag}
        search_tag = parse.urlencode(data)
        tag_list.append(search_tag)

    for search_tag in tag_list:
        search_url = movies_url
        search_url = search_url % (search_tag)
        movies_res = urllib_open(search_url)
        res = json.loads(movies_res)
        result = res['subjects']
        for res in result:
            print('标题:%s, 评分:%s' % (res['title'], res['rate']))


if __name__ == '__main__':
    tag_url = 'https://movie.douban.com/j/search_tags?type=movie&source='
    movies_url = 'https://movie.douban.com/j/search_subjects?type=movie&%s&sort=recommend&page_limit=20&page_start=0'
    get_movies(tag_url, movies_url)
