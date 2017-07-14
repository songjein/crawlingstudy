#-*- coding: utf8 -*-
from bs4 import BeautifulSoup
import urllib.request as req

# 저자:윤동주 검색
url ="https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

a_list = soup.select("#mw-content-text ul li a")

for a in a_list:
	name = a.string
	print("-", name)


