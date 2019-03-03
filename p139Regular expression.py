# 正则表达式
# 本节主要学习正则表达式（page139---page150)

# 1、实例引入
# import re
# "Hello,my phone number is 010-86432100 and email is cqc@cuiqingcai.com,and my website is https://cuiqingcai.com"

# 2、match()
# import re
# content = "Hello 123 4567 World_This is a Regex Demo"
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content,flags=0)
# print(result)
# print(result.group())
# print(result.span())

# 匹配目标
# import re
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld',content,flags=0)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

# 通用匹配
# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$',content) # 这个必须从字符串的开头与结尾一致才能匹配成功，太死板了。
# print(result)
# print(result.group())
# #print(result.group(1))
# print(result.span())


# 贪婪与非贪婪
# import re
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$',content) #“.*为贪婪模式，.*?为非贪婪模式”
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

# 修饰符re.S
# import re
# content = '''Hello 1234567 World_This
# is a Regex Demo'''
# result = re.match('^He.*?(\d+).*Demo$',content,re.S)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

# 转义匹配
# import re
# content = 'abc百度www.baidu.com'
# result = re.match('^a.*?www\.baidu\.com$',content)
# print(result)

# 3、search()
# import re
# content = 'Extra stings Hello 1234567 World This is a Regex Demo Extra stings'
# result = re.match('^Hello.*?(\d+).*?Demo$',content)
# print(result)  #匹配失败 None

# 换成search()
# import re
# content = 'Extra stings Hello 1234567 World This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo',content,re.S)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

# import re
# html = '''<div id="songs-list">
# <h2 class="title">经典老歌</h2>
# <p class="introduction">
# 经典老歌列表
# </p>
# <ul id="list" class="list-group">
# <li data-view="2">一路上有你</li>
# <li data-view="7">
# <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
# </li>
# <li data-view="4" class="active">
# <a href="/3.mp3" singer="齐秦">往事随风</a>
# </li>
# <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
# <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
# <li data-view="5">
# <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
# <li>
# </ul>
# </div>'''
#
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
# if result:
#     print(result.group(1),result.group(2))

# 4、findall()
# import re
# results = re.findall('<li.*? href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
# print(results)
# print(type(results))
# print()
# for result in results:
#     # print(result)
#     print(result[0],result[1],result[2])

# 5、sub()

# import re
# content = '54ak54yr5oiR54ix5L2g'
# # insert ='笑'
# content = re.sub('\d+','笑',content)
# print(content)

# import re
# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a)?\s*?</li>',html,re.S)
#
# for result in results:
#     print(result[1])
# print(3)
#
# html =re.sub('<a.*?>/</a>','',html)
# print(html)
# print()
# results = re.findall('<li.*?>(.*?)</li>',html,re.S)
# for result in results:
#     print(result.strip())
#
# 6、compile()
import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
content4 = '2019-01-15 20.48'
pattern =re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
result4 = re.sub('\d{2}:\d{2}', '', content4)  # 演化深化
print(result1, result2, result3, result4)
