# A simple script to extract product prices from Americanas.com
# Usage: desafio.py URL
# It simply connect to the url using requests lib and does a parse using xpath to discover the price inside the page

#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
from lxml import html,etree

def do_request(url) :
	response = requests.get(url)
	return html.fromstring(response.text)		
def get_url_from_command_line() :
 	url = ""
        for param in sys.argv[1:2] :
                url = param
        return url

url = get_url_from_command_line()
results = do_request(url).xpath("//span[@class='amount']/text()")
print "Original: '"+results[0]+"'"
for index,item in enumerate(results):
	results[index] = results[index][8:].replace(",",".")
print "Float: "+str(map(float,results)[0])
