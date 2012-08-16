# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys; sys.path.append('modules')
from Challenge import *

challenge = Challenge()
url = "http://hughes.sieve.com.br:9090/level1/"
data = challenge.do_request(url)['response']
status_code = challenge.do_request(url)['status_code']
results = data.xpath("//div/text()")
print "Preço: "+str(challenge.get_float_price(results[0]))