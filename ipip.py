#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,requests,json,time
from datetime import datetime,timedelta



def search_ip(ip):
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1"} 
	url = 'http://freeapi.ipip.net/' + str(ip)
	print(url)
	time.sleep(0.5)
	result=requests.get(url, headers=headers)
	print(result, type(result))
	print(result.json())
	print(type(result.json()))
	res="A"
	for i in range(0,len(result.json())):
		if result.json()[i]:
			res = res + "-" + result.json()[i]

	print(ip, res)
	return res

	#result=requests.get(url, headers=headers)




def send_notify(ip):

    headers={"Accept": "application/json","Content-type": "application/json"}

    out = search_ip(ip)
    print(type(out), out)

    client_source=str(out)
    strrr = str(out) + ") request: http://" + " , client source: " +  ip + client_source + " , responsetime: " + str("responsetime") + 's '
    print(strrr, type(strrr))


    cont = {'msgtype': 'text','text': {'content':strrr}}
    print(cont)
    gao = requests.post('https://oapi.dingtalk.com/robot/send?access_token=6da6823ca996108202188fa09cb525d916438314b6e49863e1f93ecd51239bdb', data=str(cont).encode('utf-8'), headers=headers)
    print(gao, gao.text, gao.json())


if __name__ == '__main__':
     now=datetime.now()
     ips = ["139.0.200.83","84.130.98.29","124.74.69.114","65.27.82.98","88.118.173.250","82.10.59.198","120.5.216.185","218.22.229.37","103.84.213.170","183.186.13.144","66.68.47.62","106.35.92.2","106.34.216.122"]
     for i in ips:
         send_notify(i)
         time.sleep(0.5)
