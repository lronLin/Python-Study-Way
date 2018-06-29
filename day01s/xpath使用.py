
from lxml import etree

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <div>
        <ul>
            <li class="class1"><a href="class1.html">1</a></li>
            <li class="class2"><a href="class2.html">2</a></li>
            <li class="class3"><a href="class3.html">3</a></li>
            <li class="class4"><a href="class4.html">4</a></li>
            <li class="class5"><a href="class5.html">5</a></li>
            <li>
                <ul>
                    <li class="class1"><a href="class6.html">6</a></li>
                    <li class="class7"><a href="class7.html">7</a></li>
                    <li class="class8"><a href="class8.html">8</a></li>
                </ul>
            </li>
        </ul>
    <div>
</body>
</html>
'''

html = etree.HTML(html)

a = html.xpath('/html')  # /表示根节点
print(a)

a1 = html.xpath('//url')  # // 表示从文档中任何一个位置去匹配信息的
print(a1)
for i in a1:
    print(i)  # 打印元素
    print(i.xpath('.'))  # 打印当前节点 - 从文档中获取 - ul
    print(i.xpath('..'))  # 打印当前节点的父节点 - li

# 找当前节点的ul下面的li的信息
# a2 = html.xpath('//ul/li')

# 获取ul下面的li的class=2的信息
a2 = html.xpath('//ul/li[@class="class2"]')  # @ 获取指定某一个class的属性
print(a2)

# 获取li下面的第一个元素
# a3 = html.xpath('//ul/li[1]')
# 获取li下面的a标签的信息
a3 = html.xpath('//ul/li/a/text()')
print(a3)

# 获取href的值
a4 = html.xpath('//ul/li/a/@href')
print(a4)
# 如果不用写, 可以在网页中直接copyXpath


