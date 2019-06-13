from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
   <a href='www.baidu.com'>你好</a>
   <a id='i1'>老刘</a>
   <div>
        <p>六点多</p>
   </div>
    <p>fffff</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, features="html.parser")

# 属性操作
# tag = soup.find('a')
# tag.attrs['lover'] = '物理老师'
# print(soup)
# del tag.attrs['href']
# print(soup)

# tags = soup.find('body').children
# print(list(tags),len(list(tags)))

# 标签和内容
# for tag in tags:
#     if type(tag) == tag:
#         print(tag,type(tag))
#         print("-------------------")
#     else:
#         print(tag,type(tag))

# tags = soup.find('body').descendants
# print(list(tags))

# tag = soup.find('body')
# tag.clear()
# print(soup)

# tag = soup.find('body')
# tag.decompose()
# print(soup)

# tag = soup.find('body')
# v = tag.extract()
# print(v)

# tag = soup.find('body')
# print(str(tag))
# print(tag.encode()) # 将标签转换为字节
# print(tag.decode())# 将标签转换为字符串

# tag = soup.find('body').find('p',recursive=False)
# print(tag)
#
# tag = soup.find('body').find('p',recursive=True)
# print(tag)
print(soup)
tag = soup.find('body')
tag.append(soup.find('a'))
print(soup)