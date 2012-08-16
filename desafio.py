# -*- coding: utf-8 -*-
# A simple script to extract product prices from Americanas.com
# Usage: desafio.py URL
# It simply connect to the url using requests lib and does a parse using xpath to discover the price inside the page
#!/usr/bin/python
import sys; sys.path.append('modules')
from Challenge import *

challenge = Challenge()
url = challenge.get_url_from_command_line()
data = challenge.do_request(url)['response']
status_code = challenge.do_request(url)['status_code']
results = data.xpath("//span[@class='amount']/text()")
unavailable = data.xpath("//div[@class='unavailProd']/text()")
if (status_code == 301):
	print u"\nInexistent product! Impossible to get price!\n"
else:
	if len(unavailable) > 0:
		print u'\nUnavailable product\n'
	elif len(results) > 0 :
		print "\nOriginal: '"+results[0]+"'\n"
        price = challenge.get_float_price(results[0])
        print "\nFloat: "+str(price)+"\n"

