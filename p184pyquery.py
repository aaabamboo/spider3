#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# #字符串初始化
# html = '''
# <div>
# <ul>
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# '''

# from pyquery import PyQuery as pq
# doc = pq(html)
# # print(doc('li'))
# # print(doc('a'))
# print(doc('span'))
#
# # URL初始化
# from pyquery import PyQuery as pq
# # doc = pq(url='https://cuiqingcai.com')
# doc = pq(url='https://www.youshang.com')
# print(doc('title'))
#
# from pyquery import PyQuery as pq
# import requests
# doc = pq(requests.get('https://cuiqingcai.com').text)
# print(doc('title'))

# 文件初始化
# from pyquery import PyQuery as pq
# doc = pq(filename='demo.html')
# print(doc('li'))

# 3.基本CSS选择器
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
# from pyquery import PyQuery as pq
# doc = pq(html)
# # print(doc('li'))
# print()
# print(doc("#container .list li"))
# print(type(doc('#container .list li')))
# print()
# print(doc("#container .list span"))

# 4.查找节点
# 子节点
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)

# 优化一下
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list span')  #优化选择方法
# print(items)

# lis = items.children()   # 获取所有list节点下面的子孙节点内容
# print(type(lis))
# print(lis)

# lis = items.children(('.active'))
# print(lis)

# 父节点
# container = items.parent()  # 这里的父节点是该节点的直接父节点，即它不会去查父节点的父节点。
# print()

# container = items.parents()  # 获取所有祖先节点
# print(container)

# container = items.parents('.wrap')  # 筛选某个祖先节点
# print(container)

# 兄弟节点用siblings()方法
li = doc('.list .item-0.active')  # 注意在list和.item-0之间有一个空格，否则反回无数据但又不报错。
print(li.siblings())
print()

print(li.siblings('.active'))

# 5.遍历

