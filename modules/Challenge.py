# -*- coding: utf-8 -*-
import sys
import requests
import re
from lxml import html
class Challenge:
	def do_request(self,url,headers=None,cookie=None) :
		#Level 1 requires to pass the headers. Why?
		response = requests.get(url,headers=headers,cookies=cookie)
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
