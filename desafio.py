# -*- coding: utf-8 -*-
# A simple script to extract product prices from Americanas.com
# Usage: desafio.py URL
# It simply connect to the url using requests lib and does a parse using xpath to discover the price inside the page
#!/usr/bin/python
from Challenge import *

challenge = Challenge()
url = challenge.get_url_from_command_line()
results = challenge.do_request(url).xpath("//span[@class='amount']/text()")
unavailable = challenge.do_request(url).xpath("//div[@class='unavailProd']/text()")
if len(unavailable) > 0:
	print u'Produto indisponível'
elif len(results) > 0 :
        print "Original: '"+results[0]+"'"
        for index,item in enumerate(results):
        	results[index] = results[index][8:].replace(".","")
                results[index] = results[index].replace(",",".")
      	print "Float: "+str(map(float,results)[0])

