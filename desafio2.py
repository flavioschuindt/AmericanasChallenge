# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys; sys.path.append('modules')
from Challenge import *

challenge = Challenge()
url = "http://hughes.sieve.com.br:9090/level1/"
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.77 Safari/537.1'}
data = challenge.do_request(url,header)['response']
results = data.xpath("//div/text()")
print "Preço: "+str(challenge.get_float_price(results[0]))