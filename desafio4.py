# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys; sys.path.append('modules')
from Challenge import *

challenge = Challenge()
domain = "http://hughes.sieve.com.br:9090"
url = domain + "/level3/"
data = challenge.do_request(url,None,None)['response']
yes = data.xpath("//a[1]/@href")
url = domain + yes[0]
cookies = challenge.do_request(url,None,None)['cookies'] 
url = domain + "/level3/"
data = challenge.do_request(url,None,cookies)['response']
results = data.xpath("//p/text()")
print "Preço: "+str(challenge.get_float_price(results[0]))