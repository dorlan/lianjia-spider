#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 板块信息相关函数

from lib.city.district import *
from lib.const.xpath import *
from lib.const.request_headers import *


def get_district_url(city, district):
    """
    拼接指定城市的区县url
    :param city: 城市
    :param district: 区县
    :return:
    """
    return "http://{0}.lianjia.com/xiaoqu/{1}".format(city, district)

def get_district_url2(city, district):
    """
    拼接指定城市的区县url
    :param city: 城市
    :param district: 区县
    :return:
    """
    return "https://{0}.lianjia.com/ershoufang/{1}".format(city, district)

def get_areas(city, district):
    """
    通过城市和区县名获得下级板块名
    :param city: 城市
    :param district: 区县
    :return: 区县列表
    """
    page = get_district_url(city, district)
    areas = list()
    try:
        headers = create_headers()
        response = requests.get(page, timeout=10, headers=headers)
        html = response.content
        root = etree.HTML(html)
        links = root.xpath(DISTRICT_AREA_XPATH)

        # 容错，例如 zh 珠海，没有小区，区域直接从ershoufang/district/返回内容去取
        if len(links) == 0:
            page = get_district_url2(city, district)
            response = requests.get(page, timeout=10, headers=headers)
            html = response.content
            root = etree.HTML(html)
            links = root.xpath(DISTRICT_AREA_XPATH2)

        # 针对a标签的list进行处理
        for link in links:
            relative_link = link.attrib['href']
            # 去掉最后的"/"
            relative_link = relative_link[:-1]
            # 获取最后一节
            area = relative_link.split("/")[-1]
            # 去掉区县名,防止重复
            if area != district:
                chinese_area = link.text
                chinese_area_dict[area] = chinese_area
                # print(chinese_area)
                areas.append(area)
        return areas
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print(get_areas("sh", "huangpu"))

