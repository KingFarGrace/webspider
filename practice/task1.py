# !/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
"""
通过这个网址 https://www.tianyancha.com/
爬企业的网址；
随便输入一个企业的名称，得到这个企业的网址；
比如，我输入  中国体育报业总社
得到：www.sportsol.com.cn
"""

search_url = "https://www.tianyancha.com/search"
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                   AppleWebKit/537.36 (KHTML, like Gecko)\
                   Chrome/81.0.4044.138 Safari/537.36'
}
try:
    cmp_name = input("请输入要查询的公司名：")
    param = {'key': cmp_name}
    main_page = requests.get(search_url, headers=header, timeout=20, params=param)
    main_page.raise_for_status()
    soup = BeautifulSoup(main_page.content, "lxml")
    search_res = soup.find("div", attrs={'class': 'search-item sv-search-company'})
    res_head = search_res.find("div", attrs={'class': 'header'})
    res_url = res_head.a['href']

    res_page = requests.get(res_url, headers=header, timeout=20)
    res_page.raise_for_status()
    soup = BeautifulSoup(res_page.content, "lxml")
    cmp_inf = soup.find("div", attrs={'class': 'box -company-box'})\
        .find("div", attrs={'class': 'detail'})
    cmp_link = cmp_inf.find("a", attrs={'class': 'company-link'})
    print("您所查找的公司网址为：{}".format(cmp_link['href']))
except Exception as e:
    print("抓取网页信息失败！")
    print(e)
