# -*- coding:utf-8 -*-
import sys
import os
import urllib
import urllib2
import re
import csv
import json
from bs4 import BeautifulSoup
import sys
from commondlib import utilities
sys.path.append("..")
from commondlib import stockctl
class thscrawl:
	def __init__(self):
		return
	def test(self):
		print("thscrawl")
	def getlocalpages(self, path):
		filelist = []
		for (root, dirs, files) in os.walk(path):
			for filename in files:
				filelist.append(os.path.join(root,filename))
		return filelist
	def getwebpagefromserver(self,stockdict):
		allstockdict = stockdict
		for no in  allstockdict:
			url = "http://doctor.10jqka.com.cn/%s/"%no
			print "ger url:"+url
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			content = response.read()
			filename=os.path.join(os.getcwd(),"pages","%s.html"%no)
			writetofile(filename,content)
			continue
			pattern = re.compile('<li class="value2"><span class="cur">(.*?)</span><div class="value2ico valueico "></div></li>',re.S)
			items = re.findall(pattern,content)
			for item in items:
				operation = item
			print operation
			pattern = re.compile('<div class="stockvalue"><span class="bignum">(.*?)</span><span class="smallnum">(.*?)</span></div>',re.S)
			items = re.findall(pattern,content)
			for item in items:
				totalscore=item[0]+item[1]
			res = totalscore+","+no+","+allstockdict[no]
			print res
			writetofile("bb.txt",res)
			break
	def crawlstart(self,stockdict):
		getwebpagefromserver(stockdict)
		allinfo =""
		for no in  stockdict:
			pagefilename=os.path.join(os.getcwd(),"tonghuashun","pages","%s.html"%no)
			stockname = no +"," + stockdict[no] +","
			stockinfo = ""
			soup = BeautifulSoup(open(pagefilename),"lxml")
		#	print(soup.prettify())
			ss = soup.find_all("div",class_="stocktotal")
			for s in ss:
				print s.string#综合诊断：5.2分 打败了35%的股票！
				stockinfo= s.string +","
			ss = soup.find_all("span",class_="cur")
			for s in ss:
				print s.string#中性
				stockinfo+=s.string+","
			ss = soup.find_all("div",class_="label",text=re.compile("\d.\d"))
			for s in ss:
				print s.string#4.8分
				stockinfo+=s.string[0:3]+","
			ss = soup.find_all("strong",class_="title")
			for s in ss:
				#stockinfo+=s.string
				pass
			#writetofile("allinfo.txt",stockinfo.encode("utf-8"))
			allinfo=stockinfo +stockname.decode( "GB2312").encode("UTF-8")
			#print allinfo
			writetofile("allinfo.csv",allinfo)
