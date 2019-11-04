# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

ip_rule_list = []
with open("ip.txt", encoding="utf-8") as f:
    for line in f:
        start_ip, end_ip, location = line.rstrip().split("|", 2)
        ip_rule_list.append((start_ip, end_ip, location))


def ip2int(ip_str: str) -> int:
    result = 0
    for i in ip_str.split("."):
        result = (result << 8) | int(i)
    return result


ip_rule_list.sort(key=lambda x: ip2int(x[0]))


def ip_to_location(ip: str) -> str:
    low, high = 0, len(ip_rule_list) - 1
    ip_int = ip2int(ip)
    while low <= high:
        mid = (low + high) >> 1
        # 查找最后一个起始IP小于等于这个IP的IP区间
        if ip2int(ip_rule_list[mid][0]) < ip_int:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and ip2int(ip_rule_list[high][0]) <= ip_int <= ip2int(ip_rule_list[high][1]):
        return ip_rule_list[high][2]
    else:
        return ""


to_location = ip_to_location("218.25.46.4")
print(to_location)

# and ip2int(ip) <= ip2int(ip_rule_list[high][1])
