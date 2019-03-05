# 第四章 解析库的使用
#4、1 XPath 使用

from lxml import etree
import re
# text = '''
# <div>
# <ul>
# <li class="item-0"><a href="link1.html">first item</a></li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-inactive"><a href="link3.html">third item</a></li>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a>
# </ul>
# </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# html = etree.parse('./test.html',etree.HTMLParser())   # 以网页文件text.html的方式传入数据并解析。
# result = etree.tostring(html)
# print(result.decode('utf-8'))        # 这里运行结果出现&#13，疑是回车字符。

# 5.所有节点
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//*')
# print(result)
# print(len(result))
# print('--------------------------------------------')
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li')  # 选取所有li节点。
# print(result)
# print(result[2])
#
# print('--------------------------------------------')
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a')  # 选取所有li节点的所有直接a子节点。
# print(result)
# print(result[0])
#
# print('--------------------------------------------')

# # 6.子节点
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//ul//a')  # 选取所有ul节点下的所有子孙a节点。
# print(result)
# print(result[3])

# 7.父节点
# html = etree.parse('./test.html', etree.HTMLParser())
# # 选取所有ul节点下的所有子孙a节点。
# # result = html.xpath('//a[@href="link4.html4"]/../@class')  # 注：本句错误发生的原因在link4.html4上，后面多一个别。
# result = html.xpath('//a/..')  # 获取当前a节点下的所有父节点
# print(result)
# print()
# result = html.xpath('//a[@href="link4.html"]/../@class')  # 获取a节点下，属性为href="link4.html"值的父节点中，属性为class的值为item-1。
# print(result)

# # 8.属性匹配
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')  # 选取所class为item-0的li节点。
# print(result)
# result = html.xpath('//li[@class="item-1"]')
# print(result)


# 9.文本获取
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/text()')  # 使用text()获取节点中的文本内容,但是未成功。
# print(result)
#
# print()
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/a/text()')  # text()获取整洁的节点中的特定文本内容，成功获取。
# print(result)
#
# print()
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]//text()')  # 使用text()获取节点中的所有文本内容，成功获取。
# print(result)         # 注意上面三种方法所获取内容的区别和/与//的区别。

# 10.属性获取
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a/@href')    # 注：此处的@href是获取节点的某个属性，与“属性匹配”不同。
# print(result)
# result = html.xpath('//li/@class')
# print(result)

# 以下需关闭前面所用的text文本
# 11.属性多值匹配
# text11 = """
# <li class="li li-first"><a href="link.html">first item</a></li>
# """
# html = etree.HTML(text11)
# # result = html.xpath('//li[@class="li"]/a/text()')  # 无法匹配 运行的结果为[]
# result = html.xpath('//li[contains(@class,"li")]/a/text()')  # contains()使用范围：此种方式在某个节点的某个属性有多个值时经常用到；第一个参数传入属性名称，第二个参数传入属性值。
# print(result)
#
# result = html.xpath('//li/a/text()')  # 其它可以获取的方法，请比较
# print(result)

# 12.多属性匹配
# text12 = """
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# """
# html = etree.HTML(text12)
# result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')  # 使用运算付and来匹配多个属性
# print(result)

# 13.按序选择
text13 = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
# html = etree.HTML(text13)
# result = html.xpath('//li[1]/a/text()')             # [1]第一个文本
# print(result)
# # print('----------------------------')
# result = html.xpath('//li[last()]/a/text()')        # last()最后一个文本
# print(result)
# # print('----------------------------')
# result = html.xpath('//li[position()<=3]/a/text()')  # position()选择小于（或等于）3的节点
# print(result)
# # print('----------------------------')
# result = html.xpath('//li[last()-2]/a/text()')       # 选择last()-2 等于3的节点，即倒数第三个
# print(result)

# 14.节点轴选择
html = etree.HTML(text13)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)

result = html.xpath('//li[1]/descendant::span')  # ???无span节点
print(result)

result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)

# 15.结语

# 正则表达式获取内容
# print('--------------------------------------------')
# results = re.findall('<li class="(.*?)"><a href="(.*?)">(.*?)</a></li>', text, re.S)
# print(results)    # text文本最后一行缺少</li>尾结点，所以结果只有四个，加上后则全部五个出现。
# print(type(results))
#
# print('------------------------------S--------------')
# for i in results:
#     print(i)
#     print(i[0], i[1], i[2])

