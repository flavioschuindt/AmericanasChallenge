# -*- coding: utf-8 -*-
import sys
import requests
import re
from lxml import html
class Challenge:
	def do_request(self,url) :
		#Level 1 requires to pass the headers. Why?
		header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.77 Safari/537.1'}
		response = requests.get(url,headers=header)
		status_and_response = {}
		if (len(response.history) > 0):
			#Moved to home or departament page
			status_and_response = dict(status_code=response.history[0].status_code,response=html.fromstring(response.text))
		else:
			status_and_response = dict(status_code=response.status_code,response=html.fromstring(response.text))
		return status_and_response
	def get_url_from_command_line(self) :
 		url = ""
        	for param in sys.argv[1:2] :
       			url = param
		return url
	def get_float_price(self,data):
		price = re.search('.*R\$ ([0-9.,]+).*', data).group(1)
		price = price.replace(".","")
		price = price.replace(",",".")
		price = float(price)
		return price
