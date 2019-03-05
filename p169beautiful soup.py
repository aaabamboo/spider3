#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 统一解析器
# from bs4 import BeautifulSoup
# soup = BeautifulSoup('<p>Hello</p>','lxml')
# print(soup.p.string)

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The united states The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href="http:example.com/elsie" class="sister" id ="link1"><!-- Elsie --></a>,
<a href="http:example.com/lacie" class="sister" id ="link2">lacie</a> and
<a href="http:example.com/tillie" class="sister" id ="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 4.基本用法
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())
# print(soup.p)
# print(soup.title.string)

# 5.节点选择器
# 5.1选择元素
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)
# print(soup.a)
# print(soup.b)

# 5.2提取信息
# print(soup.title.name)

# 获取属性
# print(soup.p.attrs)
# print(soup.p.attrs['name'])

# print(soup.p['name'])     # 返回的是字符串类型
# print(soup.p['class'])    # 返回的是列表类型

# print(soup.p.string)

# 嵌套选择
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)

# 关联选择(另建html2文档,切换soup = BeautifulSoup(html,'lxml'))中的html为html2
# 子节点和子孙节点
html2 = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters;and their names were
    <a href="http:example.com/elsie" class="sister" id ="link1">
<span>Elsie</span>
</a>
<a href="http:example.com/lacie" class="sister" id ="link2">lacie</a>
and
<a href="http:example.com/tillie" class="sister" id ="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html2,'lxml')
# print(soup.p.contents)
# print(soup.p.children)
# for i,child in enumerate(soup.p.children):
#       print(i,child)

# 用descendants选择子孙节点,enumerate枚举函数
# print(soup.p.descendants)
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)

# 父节点和祖先节点
# print(soup.a.parent)

# print(type(soup.a.parents))
# print(list(enumerate(soup.a.parents)))

# 兄弟节点
# print('Next Sibling',soup.a.next_sibling)
# print('Prev Sibling',soup.a.previous_sibling)
#
# print('Next Sibling',list(enumerate(soup.a.next_sibling)))
# print()
# print('Prev Sibling',list(enumerate(soup.a.previous_sibling)))

# ***提取信息***
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])


# 6.方法选择器
# find_all()
# find()

# 7.CSS选择器
# 嵌套选择
# 获取属性
# 获取文本




